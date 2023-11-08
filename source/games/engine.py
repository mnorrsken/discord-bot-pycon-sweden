from source.games.repository.json_source import JsonFileStrategy
from source.games.repository.strategy import SourceFileStrategy

games_source: SourceFileStrategy = JsonFileStrategy()
