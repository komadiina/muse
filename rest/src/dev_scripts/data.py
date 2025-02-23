import os
from dotenv import load_dotenv

from ..utils.connection_pool import ConnectionPool
from ..utils.playlist import fetch_playlist, process_playlist

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

ex_playlists = []

with open("data/playlists.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        ex_playlists.append(line.strip())

for playlist_id in ex_playlists:
    print(f"Feeding {playlist_id} into database...")
    playlist = fetch_playlist(
        playlist_id=playlist_id,
        part="snippet",
        api_key=os.getenv("YOUTUBE_DATA_V3_API_KEY")
    )

    cnx = ConnectionPool().get_connection()
    cnx.cursor().execute(
        "INSERT INTO playlists (title, difficulty, playlistId) VALUES (%s, %s, %s)",
        playlist[""]
    )

    playlist = process_playlist(playlist)
    for item in playlist:
        try:
            cnx.cursor().execute(

            )
        except Exception as e:
            print(e)
    cnx.close()
