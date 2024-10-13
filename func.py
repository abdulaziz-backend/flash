from pytubefix import YouTube
from rest_framework.exceptions import ValidationError
import os

MEDIA_ROOT = os.path.join(os.getcwd(), 'media')

def download_audio_from_youtube(url):
    try:
        yt = YouTube(url, use_oauth=True)

        audio_stream = yt.streams.filter(only_audio=True).first()

        if audio_stream:
            output_file = audio_stream.download(output_path=MEDIA_ROOT)
        else:
            video_stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
            if video_stream:
                output_file = video_stream.download(output_path=MEDIA_ROOT)
            else:
                raise Exception("Video stream not available")
        return output_file
    except Exception as e:
        if 'is age restricted' in str(e):
            raise ValidationError({"detail": "Video stream is age restricted"})
        else:
            raise ValidationError({"detail": str(e)}, code="invalid_youtube")
