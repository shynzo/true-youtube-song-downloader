from pytube import YouTube, Playlist
from pytube.cli import on_progress
import re
import os

DOWNLOAD_PATH = os.path.join(os.path.expanduser('~'), 'Downloads')
BASE_URL_VIDEOS = 'https://www.youtube.com/watch?v='
BASE_URL_PLAYLIST = 'https://www.youtube.com/playlist?list='

def download_video(video_id: str, title: str) -> bool:
    '''Download video from YouTube.
    
    Args:
        video_id (str): Video ID.
        title (str): Video title.
    '''
    try:
        url = BASE_URL_VIDEOS + video_id
        # regex to remove invalid characters from filename
        title_extension = re.sub(r'[\\\/*?:"<>|]', '', title) + '.mp3'
        song = YouTube(url, on_progress_callback=on_progress)
        print(f'Downloading {title}...')
        audio = song.streams.filter(only_audio=True).first().download(DOWNLOAD_PATH, filename=title_extension)
        if not audio:
            print('Erro ao baixar a música! Possivelmente o vídeo não está disponível ou já foi baixado.')
            return False
        return True
    except Exception as e:
        print(e)
        return False

def download_playlist(playlist_id: str, title: str) -> bool:
    '''Download playlist from YouTube.
    
    Args:
        playlist_id (str): Playlist ID.
        title (str): Playlist
    '''
    url = BASE_URL_PLAYLIST + playlist_id
    try:
        playlist = Playlist(url)
        for video in playlist.videos:
            download_video(video.video_id, video.title)
        return True
    except Exception as e:
        print(e)
        return False