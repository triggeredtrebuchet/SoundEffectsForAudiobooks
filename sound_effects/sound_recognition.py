import tensorflow as tf
from sentence_transformers import SentenceTransformer


class SoundRecognizer:

    def __init__(self):
        self.model = tf.keras.models.load_model("sound_effects/sound_recog")
        self.sentence_model = SentenceTransformer('paraphrase-albert-small-v2')

    def recognize(self, sen):
        cat, conf = self.__post_process(self.model(self.sentence_model.encode([sen])))[0]
        if conf > .55:
            return cat
        else:
            return None

    def __post_process(self, results):
        ret = []
        for res in results:
            label = ""
            conf = 0.0
            for i, val in enumerate(res):
                if val.numpy() > conf:
                    label = ['not_shut_door', 'not_ start_vechicle_engine', 'open_door', 'not_start_computer', 'nail',
                             'not_start_vechicle_engine', 'shut_door', 'not_light_cigarette', 'fill_cup',
                             'not_open_door_car', 'not_unlock_gun', 'light_cigarette', 'lock_door', 'not_open_door',
                             'start_computer', 'open_door_car ', " None", 'fire_gun', 'not_dig_ground',
                             'start_vechicle_engine', 'not_indoor_steps', 'open_door_car', 'None', 'indoor_steps',
                             "None", 'not_lock_door', 'not_fill_cup', 'dig_ground', 'not_fire_gun'][i]
                    conf = val.numpy()
            ret.append((label, conf))
        return ret
