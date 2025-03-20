import json

from simulator import Division, Team


def get_teams_file(filename: str) -> list[Division]:
    try:
        teams_json = open(filename)
    except FileNotFoundError:
        teams_json = open("teams_fallback.json")
    # {"DIVISION": {"SEED": "TEAM", ...}, ...}
    schedule = json.load(teams_json)
    teams_json.close()
    divisions = []
    for division in schedule:
        divisions.append(
            Division(
                [Team(seed, schedule[division][seed]) for seed in schedule[division]],
                division.capitalize(),
            )
        )
    return divisions
