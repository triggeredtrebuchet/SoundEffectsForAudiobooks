# SoundEffectsForAudiobooks

I would like to introduce a small program for automatically adding sound effects to audiobooks. For right now it can detect and apply the following:
* indoor footsteps
* sound of opening a door
* sound of closing a door
* sound of locking a mechanism
* sound of lighting a cigarette
* sound of filling a cup
* sound of booting a computer
* sounds of a gun


before: 

https://user-images.githubusercontent.com/55845430/233625838-e989fa7a-4fda-4eab-a904-7df8d1c3d8b6.mov

after:

https://user-images.githubusercontent.com/55845430/233625924-3eb69e7a-7908-49c8-880d-5c2288a055ae.mov

It uses:
- vosk for speech-to-text
- sound effects from Pixabay
- SentenceTransformers for sentence embedding

To create the dataset for training I used spacy and nltk on BookCorpus. 

The idea for this project is a part of the bigger plan to create a game master assistant for tabletop RPGs - Software that would analyze players' and master's speech for world information. For example: creating a map of the world, distinguishing PCs/NPCs and creating their descriptions, and playing sounds of the world in which players' characters act.
