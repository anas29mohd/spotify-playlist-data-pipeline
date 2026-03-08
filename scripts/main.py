import requests
import pandas as pd



def extract_playlist():
    print("Starting extraction...")

    url = "https://raw.githubusercontent.com/rushi4git/spotify-playlist-data/main/spotify_playlist.json"

    response = requests.get(url)
    data = response.json()

    df = pd.DataFrame(data["tracks"])

    df.to_csv("playlist_raw.csv", index=False)

    print("Raw playlist data saved to playlist_raw.csv")

    return df


def transform_playlist(df):
    print("Starting transformation...")

    df["duration_minutes"] = df["duration_ms"] / 60000

    df["release_year"] = pd.to_datetime(df["release_date"]).dt.year

    df = df.drop_duplicates(subset="track_name")

    df = df.fillna("Unknown")

    def popularity_category(popularity):
        if popularity <= 40:
            return "Low"
        elif popularity <= 70:
            return "Medium"
        else:
            return "High"

    df["popularity_category"] = df["popularity"].apply(popularity_category)

    print("Transformation completed")

    return df


def load_playlist(df):
    print("Saving transformed dataset...")

    df.to_csv("playlist_transformed.csv", index=False)

    print("Transformed dataset saved to playlist_transformed.csv")


def main():
    print("Spotify ETL Pipeline Started")

    df = extract_playlist()

    transformed_df = transform_playlist(df)

    load_playlist(transformed_df)

    print("Spotify ETL Pipeline Completed")


if __name__ == "__main__":
    main()