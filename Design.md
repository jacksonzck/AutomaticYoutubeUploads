# Automatic Youtube Uploader
ToDo: Think up a better name for this XD

## Problem:
Currently, I (jazck) have to manually export the VODS from Twitch to Youtube by hand. This is a lot of clicks (like, a minute). And then after that I have to manually schedule them for upload (because youtube doesn't like it when you bulk release videos). This is a minor pain. 

## Solution:
Use python to automate some of that. 

## Particulars:
I have a very ~~uninspired~~ standard naming scheme where I name each video -Name of the Game- + Episode Number. This should be maintained. 

Twitch videos sent to youtube are private by default. I have some videos on my channel that are marked private that I do not want ever to be uploaded. The bot should maintain that. 

Todo: Think of more particulars. 

## Useful Links:
https://developers.google.com/youtube/v3/docs/videos/update
https://github.com/googleapis/google-api-python-client/blob/main/docs/start.md


