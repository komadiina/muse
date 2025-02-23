from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlmodel import SQLModel, Field

class Song(DeclarativeBase):
    __tablename__ = "songs"

    id: Mapped[int] = Field(primary_key=True)
    title: Mapped[str] = Field(index=True)
    uploaded_by: Mapped[str] = Field(index=True)
    uploaded_at: Mapped[str] = Field(index=True)
    thumbnail: Mapped[str] = Field()
    video_id: Mapped[str] = Field()
