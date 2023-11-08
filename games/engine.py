from games.repository.json_source import JsonFileStrategy
from games.repository.strategy import SourceFileStrategy

games_source: SourceFileStrategy = JsonFileStrategy()
