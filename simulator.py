from __future__ import annotations

import sys
from datetime import date
from os.path import isfile
from typing import Iterable, SupportsInt

from probability import get_backup_probability, get_probabilities_file

gender = "m"
if "-w" in sys.argv:
    gender = "w"
elif "-m" in sys.argv:
    gender = "m"

GAMES_REQUIRED = 7
year = date.today().year
while (
    not isfile(probabilities_file := f"data/probabilities_{year}{gender}.json")
) and year > 1985:  # First year of tournament
    year -= 1
PROBABILITIES_FILE = probabilities_file


class Team:
    main_prob = get_probabilities_file(PROBABILITIES_FILE)

    def __init__(self, seed: SupportsInt, name: str):
        self.seed, self.name = int(seed), name

    def __lt__(self, other):
        if self.seed > other.seed:
            return True
        elif self.seed < other.seed:
            return False
        elif self.seed == other.seed:
            return None

    def __gt__(self, other):
        if self.seed < other.seed:
            return True
        elif self.seed > other.seed:
            return False
        elif self.seed == other.seed:
            return None

    @staticmethod
    def play_game(team_a: Team, team_b: Team, simulation_value: int):
        games_won, games_played = Team.main_prob[team_a.seed][team_b.seed]
        p_team_a = (
            games_won / games_played
            if games_played >= GAMES_REQUIRED
            else get_backup_probability(team_a.seed, team_b.seed)
        )
        if simulation_value / 1000 < p_team_a:
            return team_a
        return team_b


class Division:
    def __init__(self, teams: Iterable[Team], name):
        self.teams, self.name = {team.seed: team for team in teams}, name
        self.next_round = [1, 16, 8, 9, 5, 12, 4, 13, 6, 11, 3, 14, 7, 10, 2, 15]

    def play_round(self, random_number_generator: Iterable[int]):
        results = []
        teams = len(self.next_round)
        print("\n" + self.name + str(teams * 4))
        for i in range(0, teams, 2):
            if i:
                print(", ", end="")
            advances = Team.play_game(
                self.teams[self.next_round[i]],
                self.teams[self.next_round[i + 1]],
                next(random_number_generator),
            )
            print(advances.name, end="")
            results.append(advances.seed)
        self.next_round = results

    def winner(self):
        return self.teams[self.next_round[0]]
