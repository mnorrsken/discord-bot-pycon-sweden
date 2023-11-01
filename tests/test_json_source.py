import json
import os
from typing import Literal
import pytest
from source.games.repository.json_source import JsonFileStrategy


@pytest.fixture
def json_source(tmp_path) -> JsonFileStrategy:
    test_file = tmp_path / "test_data.json"
    with open(test_file, "w") as file:
        test_data = [{"game_name": "Game1"}, {"game_name": "Game2"}]
        json.dump(test_data, file)

    json_source = JsonFileStrategy()
    json_source.file = str(test_file)
    return json_source


def test_get_games(json_source: JsonFileStrategy):
    games = json_source.get_games()
    assert games == ["Game1", "Game2"]


@pytest.mark.parametrize(
    "game_name, expected_game",
    [
        (
            "Game1",
            {"game_name": "Game1"},
        ),
        ("NonExistentGame", None),
    ],
)
def test_get_game(
    json_source: JsonFileStrategy,
    game_name: Literal["Game1", "NoneExistentGame"],
    expected_game: dict[str, str] | None,
):
    game = json_source.get_game(game_name)
    assert game == expected_game


def test_update_game(json_source: JsonFileStrategy):
    game_name, new_game_name = "Game1", "NewGame1"
    json_source.update_game(game_name, new_game_name)
    updated_game = json_source.get_game(new_game_name)
    assert updated_game["game_name"] == new_game_name


def test_delete_game(json_source: JsonFileStrategy):
    json_source.delete_game("Game1")
    games = json_source.get_games()
    assert "Game1" not in games
