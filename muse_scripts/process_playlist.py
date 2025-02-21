import os
import json

def main() -> None:
    playlists = []

    for file in os.listdir("."):
        if file.endswith(".json") and file.startswith("playlist_"):
            playlists.append(file)

    if len(playlists) == 0:
        print("No playlist files found. Files ust have 'playlist_' prefix and a '.json' extension. Exiting...")
        exit(1)

    processed = []
    for playlist_filename in playlists:
        with open(playlist_filename, "r") as f:
            playlist_data = json.load(f)

        for item in playlist_data:
            try:
                processed_item = {
                    "title": item["snippet"]["title"],
                    "publishedAt": item["snippet"]["publishedAt"],
                    "thumbnail": item["snippet"]["thumbnails"]["default"],
                    "videoId": item["snippet"]["resourceId"]["videoId"]
                }

                processed.append(processed_item)
            except KeyError:
                print(f"KeyError occurred while processing playlist item. Item ID: {item["id"]}")
                continue

        with open(f"processed_{playlist_filename}", "w") as f:
            json.dump(processed, f, indent=4)
            print(f"Saved {len(processed)} processed entries to processed_{playlist_filename}")

if __name__ == "__main__":
    main()