"""Configuration loader for ZohoCRMFaker"""
import yaml


CONFIG_FILE = 'config.yml'


def load_config():
    """Load the configuration from the file."""
    with open(CONFIG_FILE, 'r', encoding='utf8') as file:
        load = yaml.safe_load(file)
    return load


config = load_config()
