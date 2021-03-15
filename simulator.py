from probability import get_backup_probability, get_probabilities_file

GAMES_REQUIRED = 7
PROBABILITIES_FILE = 'probabilities_2021.json'


class Team:
    main_prob = get_probabilities_file(PROBABILITIES_FILE)

    def __init__(self, seed: int | str, name: str):
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
        p_team_a = (games_won / games_played if games_played >= GAMES_REQUIRED
                    else get_backup_probability(team_a.seed, team_b.seed))
        if simulation_value / 1000 < p_team_a:
            return team_a
        return team_b


class Division:
    def __init__(self, teams: Iterable[Team], name):
        self.teams, self.name = {team.seed: team for team in teams}, name

    def play_through(self, random_number_generator: Iterable[int]):
        bracket = [1, 16, 8, 9, 5, 12, 4, 13, 6, 11, 3, 14, 7, 10, 2, 15]
        next_round = list(better_grouper_two(bracket))
        matches = 0
        for rnd in range(4):
            print('\n' + self.name + str(64 // 2 ** rnd))
            this_round = next_round
            next_round = []
            for match in this_round:
                matches += 1
                advances = Team.play_game(self.teams[match[0]],
                                          self.teams[match[1]],
                                          next(random_number_generator))
                print(advances.name, end='')
                next_round.append(advances.seed)
                if matches != 8 / 2 ** rnd:
                    print(', ', end='')
                else:
                    matches = 0
            next_round = list(better_grouper_two(next_round))
        self.winner = advances
        return advances


def better_grouper_two(inputs):
    # Modified from https://realpython.com/python-itertools/
    iters = [iter(inputs)] * 2
    return list(zip(*iters))
