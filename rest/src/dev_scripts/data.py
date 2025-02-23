import os
import sys

from sqlalchemy import *
from sqlalchemy.orm import *

class Base(DeclarativeBase):
    pass

class Playlist(Base):
    __tablename__ = "playlists"

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = Column(String, index=True)
    difficulty: Mapped[str] = Column(String, index=True)
    playlist_id: Mapped[str] = Column("playlistId", Integer, index=True)

class Song(Base):
    __tablename__ = "songs"

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = Column(String, index=True)
    uploaded_by: Mapped[str] = Column("uploadedBy", String, index=True)
    uploaded_at: Mapped[str] = Column("uploadedAt", DateTime, index=True)
    # thumbnail: Mapped[str] = Column(String) # can be retrieved in the format of https://i.ytimg.com/vi/{id}/default.jpg
    video_id: Mapped[str] = Column("videoId", String, unique=True)

class PlaylistSongs(Base):
    __tablename__ = "playlist_songs"

    playlist_id: Mapped[int] = Column("playlistId", Integer, ForeignKey("playlists.id"), primary_key=True)
    song_id: Mapped[int] = Column("songId", Integer, ForeignKey("songs.id"), primary_key=True)

sys.path.append(os.path.join(os.path.dirname(__file__), "..", '.'))

from dotenv import load_dotenv
from utils.playlist import fetch_playlist, process_playlist

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

if __name__ == "__main__":
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
            api_key=os.getenv("YOUTUBE_DATA_V3_API_KEY"),
            include_metadata=True
        )

        url = URL.create(
            "mysql+mysqlconnector",
            username=os.getenv("DB_USERNAME"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("MYSQL_SCHEMA"),
        )
        engine = create_engine(url, echo=False)

        with Session(engine) as session:
            playlist_model = Playlist(
                playlist_id=playlist_id,
                title=playlist["metadata"]["title"],
                difficulty="easy"
            )

            session.add(playlist_model)
            session.commit()
            processed = process_playlist(playlist["items"])
            for item in processed:
                # print(item)
                song_model = Song(
                    title=item["title"],
                    uploaded_by=item["uploadedBy"],
                    uploaded_at= " ".join(item["publishedAt"].split("T")).strip().replace("Z", ''),
                    # thumbnail=item["thumbnail"]["url"],
                    video_id=item["link"].split("?v=")[1]
                )
                try:
                    session.add(song_model)
                    session.commit()

                    pls_model = PlaylistSongs(
                        playlist_id=playlist_model.id,
                        song_id=song_model.id
                    )
                    session.add(pls_model)
                    session.commit()
                except Exception as e:
                    # possibly duplicate video, skip
                    print(e)
                    continue