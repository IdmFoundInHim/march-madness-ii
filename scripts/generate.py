import json
from datetime import date

import requests


def get_seed_data(postfix: str, title: str) -> dict:
    page: str = requests.get(f"https://mcubed.net/ncaab{postfix}/seeds.shtml").text
    page = page[
        page.find(f"{title}&#39;s NCAA Basketball Tournament :  : Records By Seed") :
    ]
    seed_data = {}
    for i in range(16):
        seed_data[i + 1] = {}
        for j in range(16):
            page = page[page.find("vs. #") + 4 :]
            page = page[page.find("(") + 1 :]
            wins = int(page[: page.find("-")])
            page = page[page.find("-") + 1 :]
            games = wins + int(page[: page.find(")")])
            seed_data[i + 1][j + 1] = (wins, games)
    return seed_data


with open(f"data/probabilities_{date.today().year}m.json", "x") as seed_data_file:
    json.dump(get_seed_data("", "Men"), seed_data_file)
with open(f"data/probabilities_{date.today().year}w.json", "x") as seed_data_file:
    json.dump(get_seed_data("w", "Women"), seed_data_file)
