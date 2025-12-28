import os

APP_NAME = "Spotlessiphy 🎵"
DOWNLOAD_DIR = "music"
HISTORY_FILE = "history.log"

if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)
