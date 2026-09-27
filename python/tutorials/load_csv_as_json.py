"""
Usage:
   data = load_csv_as_json("input.csv")

data is now identical in structure to what you would get from:
    with open("equivalent.json") as f:
        data = json.load(f)
"""
import csv
import json

def load_csv_as_json(csv_path, encoding="utf-8"):
    """
    Read a CSV and return the exact same in-memory structure
    that json.load() would produce from an equivalent .json file.
    """
    with open(csv_path, mode="r", encoding=encoding, newline="") as f:
        return list(csv.DictReader(f))

