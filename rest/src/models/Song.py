from sqlmodel import SQLModel


class Song(SQLModel, table=True):
    id: int = SQLModel.field(primary_key=True)
    title: str = SQLModel.field(index=True)
    uploaded_by: str = SQLModel.field(index=True)
    thumbnail: str = SQLModel.field(index=True)
    video_id: str = SQLModel.field(index=True, unique=True)
