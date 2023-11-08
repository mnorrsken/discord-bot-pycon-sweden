import boto3

from games.repository.strategy import SourceFileStrategy


class DynamoDBDataSource(SourceFileStrategy):
    def __init__(self, table_name: str):
        self.table_name = table_name
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table(table_name)

    def get_games(self):
        response = self.table.scan()
        games = response.get('Items', [])
        return games

    def get_game(self, name: str):
        response = self.table.get_item(Key={'name': name})
        game = response.get('Item')
        return game

    def add_game(
        self,
        name: str,
        release_year: int | None = None,
        rating: int | None = None,
        developer: str | None = None,
    ):
        new_game = {
            'name': name,
            'release_year': release_year,
            'rating': rating,
            'developer': developer,
        }
        response = self.table.put_item(Item=new_game)
        return response

    def update_game(
        self,
        name: str,
        new_game_name: str | None = None,
        new_rating: int | None = None,
    ):
        response = self.table.get_item(Key={'name': name})
        game = response.get('Item')

        if game:
            updated_game = game.copy()
            if new_game_name is not None:
                updated_game['name'] = new_game_name
            if new_rating is not None:
                updated_game['rating'] = new_rating

        self.table.put_item(Item=updated_game)

        if new_game_name != name:
            self.table.delete_item(Key={'name': name})
            print(f'Updated the game information for {name} with {new_game_name}')
        else:
            print(f'No game found with name {name}')

    def delete_game(self, name: str):
        response = self.table.get_item(Key={'name': name})
        game = response.get('Item')

        if game:
            response = self.table.delete_item(Key={'name': name})
            print(f'Deleted the game {name}')
        else:
            print(f'No game found with name {name}')


# dynamo_db_source = DynamoDBDataSource(table_name="games")
# games = dynamo_db_source.delete_game("EAFC-24")
# games = dynamo_db_source.update_game("EAFC24", "EAFC-24")
# print(games)
