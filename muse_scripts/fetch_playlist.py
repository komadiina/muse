import argparse
import json
import os
import sys
from os.path import join, dirname
import dotenv
import requests

# PyCharm hinting
# from sphinx.cmd.build import SupportsWrite

dotenv_path = join(dirname(__file__), ".env")
dotenv.load_dotenv(dotenv_path)


def fetch_playlist(
        api_key: str,
        playlist_id: str,
        part: str = "snippet"
) -> list:
    base = f"https://www.googleapis.com/youtube/v3/playlistItems?key={api_key}&part={part}&playlistId={playlist_id}&maxResults=50"
    items = []

    response_data = {}
    flag = "nextPageToken" not in response_data
    while flag:
        response = requests.get(base)
        response_data = response.json()
        items.extend(response_data["items"])

        if "nextPageToken" in response_data:
            base = f"{base}&pageToken={response_data['nextPageToken']}"
            flag = True
        else:
            flag = False

    return items


def save(items: list, playlist_id: str) -> None:
    filename = f"playlist_{playlist_id}.json"
    with open(filename, "w") as f:
        json.dump(items, f, indent=4)

    print(f"Saved {len(items)} entries to {filename}")


def main() -> None:
    parser = argparse.ArgumentParser(description="MUSE playlist fetcher utility")
    parser.add_argument("-k", "--api_key", help="Your API key from the Google Developers Cloud Console. Required.",
                        required=False)

    parser.add_argument("-p", "--playlist_id",
                        help="The Playlist ID, usually identified with the 'list' query parameter. Required.",
                        required=False)

    parser.add_argument("-l", "--list_collection",
                        help="Playlist ID collection relative path. Represented as a row-separated collection. Optional - required if 'playlist_id' is not provided.",
                        required=False)

    parser.add_argument("-r", "--response_type",
                        help="Response details type. Available values: snippet, contentDetails, id, status. Default is 'snippet'. See the relevant YouTube API docs for more information.",
                        default="snippet")

    args = parser.parse_args()

    api_key = args.api_key
    playlist_id = args.playlist_id
    response_type = args.response_type
    list_collection = args.list_collection

    if playlist_id is None and list_collection is None:
        print(
            "Playlist ID nor list collection path are not provided.\nRun the script with '-h' parameter for additional help.\nExiting...")
        exit(1)

    if api_key is None:
        print(
            "API Key not provided via argument command line.\nRun the script with '-h' parameter for additional help.\nSearching in environment...")

        api_key = os.getenv("YOUTUBE_API_KEY")
        if api_key is None:
            print("API Key not found in environment (YOUTUBE_V3_DATA_API_KEY), exiting...")
            sys.exit(1)

    playlist_ids = []
    if playlist_id is not None:
        playlist_ids.append(playlist_id)

    if playlist_id is not None and list_collection is not None:
        print(
            "Playlist ID and list collection path are both provided. Merging...")
        with open(list_collection, "r") as f:
            playlist_ids.extend(f.read().splitlines(keepends=False))

    if playlist_id is None and list_collection is not None:
        with open(list_collection, "r") as f:
            playlist_ids = f.read().splitlines(keepends=False)

    for playlist_id in playlist_ids:
        print(f"Fetching playlist {playlist_id}...")
        result = fetch_playlist(api_key, playlist_id, response_type)

        try:
            save(result, playlist_id)
        except IOError as e:
            print(f"Failed to save playlist {playlist_id} due to an IOError, reason: {e}")
        except Exception as e:
            print(f"Failed to save playlist {playlist_id} due to an unknown error, reason: {e}")


if __name__ == "__main__":
    main()
