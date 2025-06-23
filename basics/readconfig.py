import tomllib
import yaml
from pprint import pprint


def readtoml(file):
    with open(file, "rb") as f:
        return tomllib.load(f)


def readyml(file):
    with open(file, "rb") as f:
        return yaml.safe_load(f)


def main():
    # data = readtoml("config/config.toml")
    data = readyml("config/config.yml")
    pprint(data, sort_dicts=False)


if __name__ == "__main__":
    main()
