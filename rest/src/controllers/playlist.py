import json

import fastapi
from typing import Union
from os import getenv

from ..utils.connection_pool import ConnectionPool
from ..utils.playlist import fetch_playlist, process_playlist

router = fastapi.routing.APIRouter()
router.yt_key = getenv("YOUTUBE_DATA_V3_API_KEY")
router.tags = ["Playlist"]

print(f"Using YouTube API Key: {router.yt_key[:5]}..."
      if router.yt_key is not None
      else "No YouTube API Key detected. Certain features will not work. (name=YOUTUBE_DATA_V3_API_KEY)")


@router.get("/playlist/random")
def fetch_random_playlist(difficulty: Union[str, None] = "easy"):
    cnx = ConnectionPool().get_connection()
    cnx.close()


@router.get("/playlist/scrape/{playlist_id}")
def fetch_playlist_by_id(playlist_id: str, process: Union[bool, None] = True):
    if router.yt_key is None:
        return fastapi.Response(
            content=json.dumps({"error": "Youtube Data v3 API key not set in envvars."}, sort_keys=True, indent=4),
            status_code=fastapi.status.HTTP_500_INTERNAL_SERVER_ERROR)

    result = fetch_playlist(api_key=router.yt_key, playlist_id=playlist_id, part="snippet")["items"]
    if len(result) == 0:
        return fastapi.Response(
            content=json.dumps({"error": "No playlist items found."}, sort_keys=True, indent=4),
            status_code=fastapi.status.HTTP_404_NOT_FOUND)

    return process_playlist(result) if process == True else result
