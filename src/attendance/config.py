import json
import importlib.resources

config_file = importlib.resources.files("attendance").joinpath("config.json")


class ConfigDict(dict):
    def __getattr__(self, item):
        if item in self:
            return self[item]

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, item):
        if item in self:
            del self[item]


def load_config():
    with config_file.open("r") as f:
        config = json.load(f)
    return ConfigDict(config)

def edit_config(**kwargs):
    