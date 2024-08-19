import json
import importlib.resources

config_file = importlib.resources.files("attendance").joinpath("config.json")


class ConfigDict(dict):
    def __getattr__(self, item):
        if item in self:
            return self[item]


def load_config():
    with config_file.open("r") as f:
        config = ConfigDict(json.load(f))
    return config


def edit_config(**kwargs):
    with config_file.open("r") as f:
        config = ConfigDict(json.load(f))
        config.update(kwargs)
    with config_file.open("w") as f:
        f.write(json.dumps(config, indent=4))
    print(
        ", ".join(
            [f"{k.replace("_", " ").title()} updated to {v}" for k, v in kwargs.items()]
        )
    )
