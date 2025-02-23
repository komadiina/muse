import json
import requests

def fetch_playlist(
        api_key: str,
        playlist_id: str,
        part: str = "snippet",
        include_metadata: bool = False
) -> dict:
    base = f"https://www.googleapis.com/youtube/v3/playlistItems?key={api_key}&part={part}&playlistId={playlist_id}&maxResults=50"
    items = []

    response_data = {}
    flag = "nextPageToken" not in response_data
    while flag:
        response = requests.get(base)
        response_data: dict = response.json()

        if response_data.get("items") is None:
            break

        items.extend(response_data["items"])

        if "nextPageToken" in response_data:
            base = f"{base}&pageToken={response_data['nextPageToken']}"
            flag = True
        else:
            flag = False

    if not include_metadata:
        return {"items": items}
    else:
        response = requests.get(f"https://www.googleapis.com/youtube/v3/playlists?key={api_key}&part=snippet&id={playlist_id}")
        response_data = response.json()
        return {
            "items": items,
            "metadata": response_data["items"][0]["snippet"]
        }

def save_playlist(items: list, playlist_id: str) -> None:
    filename = f"out/raw/{playlist_id}.json"
    with open(filename, "w") as f:
        json.dump(items, f, indent=4)

    print(f"Saved {len(items)} entries to {filename}")


def process_playlist(playlist: list) -> list:
    processed = []
    for item in playlist:
        try:
            processed_item = {
                "title": item["snippet"]["title"],
                "publishedAt": item["snippet"]["publishedAt"],
                "thumbnail": item["snippet"]["thumbnails"]["default"],
                "link": "https://youtube.com/watch?v=" + item["snippet"]["resourceId"]["videoId"],
                "uploadedBy": item["snippet"]["videoOwnerChannelTitle"]
            }

            processed.append(processed_item)
        except KeyError:
            print(f"KeyError occurred while processing playlist item. Item ID: {item["id"]}")
            continue

    return processed
