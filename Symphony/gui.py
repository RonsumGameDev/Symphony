import tkinter as tk
from tkinter import messagebox
from audio import stream_audio, download_audio, pause_play, skip_forward, rewind_back, create_playlist
from config import APP_NAME

def launch_gui():
    def stream_song():
        query = entry.get()
        if not query:
            messagebox.showerror("Error", "Please enter a song name.")
            return
        title = stream_audio(query)
        status_var.set(f"Now streaming: {title}")

    def download_song():
        query = entry.get()
        if not query:
            messagebox.showerror("Error", "Please enter a song name.")
            return
        title = download_audio(query)
        status_var.set(f"Downloaded: {title}")

    def pause_play_song():
        pause_play()

    def rewind():
        rewind_back()

    def forward():
        skip_forward()

    def c_playlist():
        playlist_win = tk.Toplevel(root)
        playlist_win.title("Create Playlist")
        playlist_win.geometry("300x200")

        label = tk.Label(playlist_win, text="This is a new window!")
        label.pack(pady=20)
        create_playlist()

    root = tk.Tk()
    root.title(APP_NAME)

    entry = tk.Entry(root, width=40, font=("Arial", 12))
    entry.pack(pady=10)

    button_frame = tk.Frame(root)
    button_frame.pack()

    stream_btn = tk.Button(button_frame, text="Stream", command=stream_song, width=15)
    stream_btn.grid(row=0, column=0, padx=5)

    download_btn = tk.Button(button_frame, text="Download", command=download_song, width=15)
    download_btn.grid(row=0, column=1, padx=5)

    pauseplay_btn = tk.Button(button_frame, text="Pause / Play", command=pause_play_song, width=15)
    pauseplay_btn.grid(row=1, column=0, padx=5)

    rewind_btn = tk.Button(button_frame, text="<<<", command=rewind, width=15)
    rewind_btn.grid(row=1, column=1, padx=5)

    forward_btn = tk.Button(button_frame, text=">>>", command=forward, width=15)
    forward_btn.grid(row=2, column=0, padx=5)

    make_playlist = tk.Button(button_frame, text="+Playlist", command = c_playlist, width = 15)
    make_playlist.grid(row=2, column=0, padx=5)

    global status_var
    status_var = tk.StringVar()
    status_label = tk.Label(root, textvariable=status_var, font=("Arial", 10), fg="green")
    status_label.pack(pady=10)

    root.mainloop()
