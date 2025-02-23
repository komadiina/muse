import json

import fastapi
from typing import Union
from os import getenv
from os.path import join, dirname
from dotenv import load_dotenv
from ..utils.playlist import fetch, process as process_playlist

load_dotenv(join(dirname(__file__), ".env"))

app = fastapi.FastAPI()
app.yt_key = getenv("YOUTUBE_DATA_V3_API_KEY")
print(f"Using YouTube API Key: {app.yt_key[:5]}..."
      if app.yt_key is not None
      else "No YouTube API Key detected. Certain features will not work. (name=YOUTUBE_DATA_V3_API_KEY)")


@app.get("/api/v1/playlist/{playlist_id}")
def fetch_playlist(playlist_id: str, process: Union[bool, None] = True):
    if app.yt_key is None:
        return fastapi.Response(
            content=json.dumps({"error": "Youtube Data v3 API key not set in envvars."}, sort_keys=True, indent=4),
            status_code=fastapi.status.HTTP_500_INTERNAL_SERVER_ERROR)

    result = fetch(playlist_id=playlist_id, api_key=app.yt_key, part="snippet")
    return process_playlist(result) if process == True else result
