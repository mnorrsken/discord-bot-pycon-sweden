import boto3
import json
from source.games.repository.strategy import SourceFileStrategy


class S3DataSource(SourceFileStrategy):
    def __init__(self, bucket_name: str, object_key: str):
        self.bucket_name = bucket_name
        self.object_key = object_key  # games.json
        self.s3 = boto3.client("s3")

    def get_games(self):
        try:
            response = self.s3.get_object(Bucket=self.bucket_name, Key=self.object_key)
            data = json.loads(response["Body"].read().decode("utf-8"))
            return [game["game_name"] for game in data]
        except Exception as e:
            print(f"Error: {str(e)}")
            return []

    def get_game(self, game_name: str):
        try:
            response = self.s3.get_object(Bucket=self.bucket_name, Key=self.object_key)
            data = json.loads(response["Body"].read().decode("utf-8"))

            for item in data:
                if item["game_name"] == game_name:
                    return item
                return None
        except Exception as e:
            print(f"Error: {str(e)}")
            return None

    def add_game(
        self,
        game_name: str,
        release_year: int | None = None,
        rating: int | None = None,
        developer: str | None = None,
    ):
        try:
            response = self.s3.get_object(Bucket=self.bucket_name, Key=self.object_key)
            data = json.loads(response["Body"].read().decode("utf-8"))

            new_game = {
                "game_name": game_name,
                "release_year": release_year,
                "rating": rating,
                "developer": developer,
            }
            data.append(new_game)
            self.s3.put_object(
                Bucket=self.bucket_name, Key=self.object_key, Body=json.dumps(data)
            )
        except Exception as e:
            print(f"Error: {str(e)}")

    def update_game(
        self,
        game_name: str,
        new_game_name: str | None = None,
        new_rating: int | None = None,
    ):
        try:
            response = self.s3.get_object(Bucket=self.bucket_name, Key=self.object_key)
            data = json.loads(response["Body"].read().decode("utf-8"))

            for item in data:
                if item["game_name"] == game_name:
                    if new_game_name is not None:
                        item["game_name"] = new_game_name
                    if new_rating is not None:
                        item["rating"] = new_rating
                    break
            self.s3.put_object(
                Bucket=self.bucket_name, Key=self.object_key, Body=json.dumps(data)
            )
        except Exception as e:
            print(f"Error: {str(e)}")

    def delete_game(self, game_name: str):
        try:
            response = self.s3.get_object(Bucket=self.bucket_name, Key=self.object_key)
            data = json.loads(response["Body"].read().decode("utf-8"))

            data = [item for item in data if item["game_name"] != game_name]

            self.s3.put_object(
                Bucket=self.bucket_name, Key=self.object_key, Body=json.dumps(data)
            )
        except Exception as e:
            print(f"Error: {str(e)}")


s3_data_source = S3DataSource("discord-bot-souce-test", "games.json")
s3_data_source.get_games()
