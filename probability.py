import json
from typing import Mapping, Sequence


def get_probabilities_file(filename: str) -> Mapping[int, Mapping[int, Sequence[int]]]:
    """Gets probabilities from JSON file"""
    with open(filename) as probabilities_json:
        return json.load(
            probabilities_json, object_hook=lambda d: {int(k): d[k] for k in d}
        )


def get_backup_probability(seed: int, opponent: int) -> float:
    """Calculate win probability based on the numeric difference between seeds

    Regression Methodology: Add the results of all games with the given
    seed difference, then divide wins by games. Remove low-accuracy
    (< 10 games) points. Perform a linear
    regression on the wins ratio vs. difference in seeds data set.
    """
    discrepancy = opponent - seed
    team_is_favorite = discrepancy > 0
    p_favorite = 0.0322379162 * abs(discrepancy) + 0.5033561178
    return p_favorite if team_is_favorite else 1 - p_favorite


def _backup_probability_get_regression_set(
    main_probabilities: Mapping[int, Mapping[int, Sequence[int]]],
) -> Mapping[int, Sequence[int]]:
    """Gets win-to-games ratio for each seed discrepancy

    Win ratios are given as lists [n, d] representing a fraction.
    """
    backup_probabilities = {}
    for discrepancy in range(16):
        wins, games = 0, 0
        for seed in range(1, 17 - discrepancy):
            add_wins, add_games = main_probabilities[seed][seed + discrepancy]
            wins += add_wins
            games += add_games
        backup_probabilities[discrepancy] = [wins, games]
    return backup_probabilities
