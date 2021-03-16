import json

from simulator import Division, Team


def get_teams_file(filename: str):
    with open(filename) as teams_json:
        schedule = json.load(teams_json)
    # {"DIVISION": {"SEED": "TEAM", ...}, ...}
    divisions = []
    for division in schedule:
        divisions.append(
            Division(
                [Team(seed, schedule[division][seed]) for seed in schedule[division]],
                division.capitalize(),
            )
        )
    return divisions
