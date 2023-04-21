import wave
import json
from pydub import AudioSegment
import librosa
from vosk import Model, KaldiRecognizer
import os
import numpy as np
from . import sound_recognition


def add_sound_effects(audio_filename):
    sens = __split_text_into_sens(__analyze_audiofile(audio_filename))
    app_sound_sig = []
    with open('sound_effects/sound_phrases.json', 'r') as file:
        sound_phrases = json.load(file)
    sound_recognizer = sound_recognition.SoundRecognizer()
    for sen in sens:
        text = " ".join([w['word'] for w in sen])
        cat = sound_recognizer.recognize(text)
        if cat in sound_phrases:
            is_added = False
            for phrase in sound_phrases[cat]:
                if is_added:
                    break
                for word in sen[::-1]:
                    if word['word'] == phrase:
                        is_added = True
                        app_sound_sig.append((cat, word['end']))
                        break

    app_sound_sig = list(set(app_sound_sig))

    audiobook_y, audiobook_sr = librosa.load(audio_filename, sr=None)
    slf = __create_sound_effects_layer(audiobook_y, audiobook_sr, app_sound_sig)
    result = __add_sf_layer(slf, audiobook_y, 0.5)
    return audiobook_y, result, audiobook_sr


def __analyze_audiofile(audio_filename):
    if audio_filename.endswith('.mp3'):
        audio_filename = __mp3_to_wav(audio_filename)

    model = Model("sound_effects/vosk-model-small-en-us-0.15")
    wf = wave.open(audio_filename, "rb")
    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)

    # get the list of JSON dictionaries
    results = []
    # recognize speech using vosk model
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            part_result = json.loads(rec.Result())
            results.append(part_result)
    part_result = json.loads(rec.FinalResult())
    results.append(part_result)
    wf.close()  # close audiofile
    words: list[dict] = []
    for part in results:
        words.extend(part['result'])
    return words


def __convert_from_mp3(audio_filename):
    audio = AudioSegment.from_file(audio_filename, format="mp3")
    audio.export("temp.wav", format="wav")
    return "temp.wav"


def __mp3_to_wav(source, skip=0):
    sound = AudioSegment.from_mp3(source)  # load source
    sound = sound.set_channels(1)  # mono
    sound = sound.set_frame_rate(16000)  # 16000Hz

    audio = sound[skip * 1000:]
    output_path = os.path.splitext(source)[0] + ".wav"
    audio.export(output_path, format="wav")

    return output_path

def __split_text_into_sens(words, sen_len=10, padding=5):
    sens = []
    start, end = 0, sen_len
    while True:
        sens.append(words[start:end])
        start += sen_len - padding
        end += sen_len - padding
        if end > len(words):
            break
    return sens


def __add_sf_layer(sound_effects_layer, audiobook_y, sound_volume):
    result_audio = sound_effects_layer * sound_volume + audiobook_y * (1 - sound_volume)
    result_audio = librosa.util.normalize(result_audio)
    return result_audio


def __create_sound_effects_layer(audiobook_y, audiobook_sr, app_sound_sig):
    audio_dir = 'sound_effects/sounds'
    audio_data = {}

    for filename in os.listdir(audio_dir):
        filepath = os.path.join(audio_dir, filename)
        y, sr = librosa.load(filepath, sr=audiobook_sr)
        audio_data[filename[:-4]] = y

    sound_effects_layer = np.zeros_like(audiobook_y)

    for sound_sig in app_sound_sig:
        idx = int(audiobook_sr * sound_sig[1])
        sound_effects_layer[idx: idx + len(audio_data[sound_sig[0]])] += audio_data[sound_sig[0]]

    return sound_effects_layer
