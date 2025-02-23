from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlmodel import SQLModel, Field

class Playlist(DeclarativeBase):
    __tablename__ = "playlists"

    id: Mapped[int] = Field(primary_key=True)
    title: Mapped[str] = Field(index=True)
    difficulty: Mapped[str] = Field(index=True)
    playlist_id: Mapped[str] = Field(index=True)