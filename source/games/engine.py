from source.games.repository.strategy import SourceFileStrategy
from source.games.repository.json_source import JsonFileStrategy

games_source: SourceFileStrategy = JsonFileStrategy()
