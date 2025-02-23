from sqlmodel import SQLModel, Field

class Playlist(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    title: str = Field(index=True)
    difficulty: str = Field(index=True)