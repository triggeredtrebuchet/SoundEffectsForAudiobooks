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
<iframe width="100%" height="300" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1497527335%3Fsecret_token%3Ds-0ZiDkF0wKBg&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/hubert-baraniak-708283111" title="Hubert Baraniak" target="_blank" style="color: #cccccc; text-decoration: none;">Hubert Baraniak</a> · <a href="https://soundcloud.com/hubert-baraniak-708283111/example-sentences-before/s-0ZiDkF0wKBg" title="Example Sentences Before" target="_blank" style="color: #cccccc; text-decoration: none;">Example Sentences Before</a></div>

after:
<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1497527242%3Fsecret_token%3Ds-hZ7HtEyrHYM&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/hubert-baraniak-708283111" title="Hubert Baraniak" target="_blank" style="color: #cccccc; text-decoration: none;">Hubert Baraniak</a> · <a href="https://soundcloud.com/hubert-baraniak-708283111/example-sentences-after/s-hZ7HtEyrHYM" title="Example Sentences After" target="_blank" style="color: #cccccc; text-decoration: none;">Example Sentences After</a></div>

It uses:
- vosk for speech-to-text
- sound effects from Pixabay
- SentenceTransformers for sentence embedding

To create the dataset for training I used spacy and nltk on BookCorpus. 

The model has low accuracy on more complicated sentences due to overfitting on a small amount of data.