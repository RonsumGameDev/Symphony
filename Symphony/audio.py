import os
from yt_dlp import YoutubeDL
import vlc
from config import DOWNLOAD_DIR
from utils import make_file_not_a_bastard, log_download

player = None

def get_audio_info(query):
    ydl_opts = {'format': 'bestaudio/best', 'noplaylist': True, 'quiet': True, 'default_search': 'ytsearch1'}
    with YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(query, download=False)
        first_result = result['entries'][0]
        return first_result['url'], first_result['title']

def stream_audio(query):
    global player
    if player is not None:
        player.stop()
    url, title = get_audio_info(query)
    instance = vlc.Instance()
    player = instance.media_player_new()
    media = instance.media_new(url)
    player.set_media(media)
    player.play()
    return title

def download_audio(query):
    ydl_opts = {'format': 'bestaudio/best',
        'noplaylist': True,
        'quiet': False,
        'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(query, download=True)
        title = make_file_not_a_bastard(info['title'])
        log_download(title)
        return title

def pause_play():
    global player
    if player is not None:
        player.pause()

def skip_forward():
    global player
    if player is not None:
        current = player.get_time()
        player.set_time(current + 5000)

def rewind_back():
    global player
    if player is not None:
        current = player.get_time()
        player.set_time(current - 5000)

def create_playlist():
    return
