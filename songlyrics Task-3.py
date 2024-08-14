import tkinter as tk
from tkinter import messagebox
import lyricsgenius

# Function to fetch and display lyrics
def fetch_lyrics():
    song_title = title_entry.get()
    artist_name = artist_entry.get()
    
    if not song_title or not artist_name:
        messagebox.showwarning("Input Error", "Please enter both song title and artist name")
        return
    
    try:
        genius = lyricsgenius.Genius("YOUR_GENIUS_API_KEY")
        song = genius.search_song(song_title, artist_name)
        if song:
            lyrics_text.delete(1.0, tk.END)
            lyrics_text.insert(tk.END, song.lyrics)
        else:
            lyrics_text.delete(1.0, tk.END)
            lyrics_text.insert(tk.END, "Lyrics not found")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Lyrics Extractor")

# Create and place the labels, entries, and buttons
tk.Label(root, text="Song Title:").grid(row=0, column=0, padx=10, pady=10)
title_entry = tk.Entry(root)
title_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Artist Name:").grid(row=1, column=0, padx=10, pady=10)
artist_entry = tk.Entry(root)
artist_entry.grid(row=1, column=1, padx=10, pady=10)

fetch_button = tk.Button(root, text="Fetch Lyrics", command=fetch_lyrics)
fetch_button.grid(row=2, column=0, columnspan=2, pady=20)

lyrics_text = tk.Text(root, wrap=tk.WORD, width=60, height=20)
lyrics_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Start the main event loop
root.mainloop()

