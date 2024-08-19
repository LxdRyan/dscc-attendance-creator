import json
import importlib.resources

consts_file = importlib.resources.files(__package__).joinpath("consts.json")


class ConstsDict(dict):
    def __getattr__(self, item):
        if item in self:
            return self[item]


def load_consts():
    with consts_file.open("r") as f:
        consts = ConstsDict(json.load(f))
    return consts


def edit_consts(**kwargs):
    with consts_file.open("r") as f:
        consts = ConstsDict(json.load(f))
        consts.update(kwargs)
    with consts_file.open("w") as f:
        f.write(json.dumps(consts, indent=4))
    print(
        ", ".join(
            [f"{k.replace("_", " ").title()} updated to {v}" for k, v in kwargs.items()]
        )
    )
