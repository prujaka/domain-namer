from configparser import ConfigParser
from pathlib import Path

CONFIG_NAME = "config.ini"
CONFIG_PATH = Path(__file__).resolve().parent.parent / CONFIG_NAME

config = ConfigParser()
config.read(CONFIG_PATH)

DEEPINFRA_API_KEY_AUTO = config['secrets']['deepinfra_api_key_auto']
OPENAI_API_KEY = config['secrets']['openai_api_key']
