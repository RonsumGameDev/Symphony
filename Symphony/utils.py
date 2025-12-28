import re
from unidecode import unidecode
from config import HISTORY_FILE

def make_file_not_a_bastard(name):
    name = unicode(name)
    name = re.sub(r'[\\/*?:"<>|]', "", name)
    #name = name.replace(" ", "_").lower()
    return name.strip()

def log_download(title):
    with open(HISTORY_FILE, "a") as log:
        log.write(f"Downloaded: {title}\n")
