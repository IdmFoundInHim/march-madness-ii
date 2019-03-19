class Team:
    def __init__(self, seed, name):
        self.seed, self.name = seed, name

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
    def play_game(teama, teamb, rd=1):
        matchup_probability = {  # FROM 2018 (except 1-16)
            (1, 1): 0.500,  # irrelevant
            (1, 2): 0.489,
            (1, 3): 0.591,
            (1, 4): 0.712,
            (1, 5): 0.821,
            (1, 6): 0.778,
            (1, 7): 1.000,
            (1, 8): 0.806,
            (1, 9): 0.923,
            (1, 10): 0.800,
            (1, 11): 0.571,
            (1, 12): 1.000,
            (1, 13): 1.000,
            (1, 14): None,
            (1, 15): None,
            (1, 16): 0.993,  # Updated 2019
            (2, 2): 0.500,  # irrelevant
            (2, 3): 0.641,
            (2, 4): 0.333,
            (2, 5): 0.000,
            (2, 6): 0.793,
            (2, 7): 0.705,
            (2, 8): 0.400,
            (2, 9): 0.000,
            (2, 10): 0.609,
            (2, 11): 0.857,
            (2, 12): 1.000,
            (2, 13): None,
            (2, 14): None,
            (2, 15): 0.939,
            (2, 16): None,
            (3, 3): 0.500,  # irrelevant
            (3, 4): 0.400,
            (3, 5): 0.667,
            (3, 6): 0.582,
            (3, 7): 0.571,
            (3, 8): 1.000,
            (3, 9): 1.000,
            (3, 10): 0.692,
            (3, 11): 0.659,
            (3, 12): None,
            (3, 13): None,
            (3, 14): 0.841,
            (3, 15): 1.000,
            (3, 16): None,
            (4, 4): 0.500,  # irrelevant
            (4, 5): 0.557,
            (4, 6): 0.667,
            (4, 7): 0.400,
            (4, 8): 0.444,
            (4, 9): 1.000,
            (4, 10): 1.000,
            (4, 11): None,
            (4, 12): 0.667,
            (4, 13): 0.803,
            (4, 14): None,
            (4, 15): None,
            (4, 16): None,
            (5, 5): 0.500,  # irrelevant
            (5, 6): 1.000,
            (5, 7): None,
            (5, 8): 0.000,
            (5, 9): 0.500,
            (5, 10): 1.000,
            (5, 11): None,
            (5, 12): 0.644,
            (5, 13): 0.800,
            (5, 14): None,
            (5, 15): None,
            (5, 16): None,
            (6, 6): 0.500,  # irrelevant
            (6, 7): 0.571,
            (6, 8): 0.000,
            (6, 9): None,
            (6, 10): 0.714,
            (6, 11): 0.629,
            (6, 12): None,
            (6, 13): None,
            (6, 14): 0.875,
            (6, 15): None,
            (6, 16): None,
            (7, 7): 0.500,  # irrelevant
            (7, 8): 0.000,
            (7, 9): None,
            (7, 10): 0.614,
            (7, 11): 0.000,
            (7, 12): None,
            (7, 13): None,
            (7, 14): 1.000,
            (7, 15): 0.666,
            (7, 16): None,
            (8, 8): 0.500,  # irrelevant
            (8, 9): 0.508,
            (8, 10): None,
            (8, 11): None,
            (8, 12): 0.000,
            (8, 13): 1.000,
            (8, 14): None,
            (8, 15): None,
            (8, 16): None,
            (9, 9): 0.500,  # irrelevant
            (9, 10): None,
            (9, 11): None,
            (9, 12): None,
            (9, 13): 1.000,
            (9, 14): None,
            (9, 15): None,
            (9, 16): None,
            (10, 10): 0.500,  # irrelevant
            (10, 11): 0.333,
            (10, 12): None,
            (10, 13): None,
            (10, 14): 1.000,
            (10, 15): 1.000,
            (10, 16): None,
            (11, 11): 0.500,  # irrelevant
            (11, 12): None,
            (11, 13): None,
            (11, 14): 1.000,
            (11, 15): None,
            (11, 16): None,
            (12, 12): None,
            (12, 13): 0.727,
            (12, 14): None,
            (12, 15): None,
            (12, 16): None,
            (13, 13): 0.500,  # irrelevant
            (13, 14): None,
            (13, 15): None,
            (13, 16): None,
            (14, 14): 0.500,  # irrelevant
            (14, 15): None,
            (14, 16): None,
            (15, 15): 0.500,  # irrelevant
            (15, 16): None,
            (16, 16): 0.500  # irrelevant + IMPOSSIBLE
        }
        teams = [teama, teamb]
        teams.sort(reverse=True)
        favorite_probability = matchup_probability[teams[0].seed,
                                                   teams[1].seed]
        if favorite_probability is None or favorite_probability == 0.0:
            favorite_probability = min(0.996,
                                       ((teams[1].seed - teams[0].seed)
                                        * .065 + rd / 15))
        simulation = next(randomgenerator) / 1000
        if simulation < favorite_probability:
            return teams[0]
        else:
            return teams[1]


class Division:
    def __init__(self, team_list, name):
        self.teams, self.name = {}, name
        for team in team_list:
            self.teams[team[0]] = Team(team[0], team[1])

    def play_through(self):
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
                                          rd=rnd+1)
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


def randomnumbers(provided_numbers):
    for x in provided_numbers:
        yield float(x)


east = [
    (1, 'Duke'),
    (2, 'Michigan State'),
    (3, 'LSU'),
    (4, 'Virginia Tech'),
    (5, 'Mississippi State'),
    (6, 'Maryland'),
    (7, 'Louisville'),
    (8, 'VCU'),
    (9, 'UCF'),
    (10, 'Minnesota'),
    (11, 'Temple/Belmont'),
    (12, 'Liberty'),
    (13, 'Saint Louis'),
    (14, 'Yale'),
    (15, 'Bradley'),
    (16, 'North Carolina Central/North Dakota State'),
]
west = [
    (1, 'Gonzaga'),
    (2, 'Michigan'),
    (3, 'Texas Tech'),
    (4, 'Florida State'),
    (5, 'Marquette'),
    (6, 'Buffalo'),
    (7, 'Nevada'),
    (8, 'Syracuse'),
    (9, 'Baylor'),
    (10, 'Florida'),
    (11, 'Arizona State/St. John\'s'),
    (12, 'Murray State'),
    (13, 'Vermont'),
    (14, 'Northern Kentucky'),
    (15, 'Montana'),
    (16, 'Fairleigh Dickinson/Prairie View A&M'),
]
midwest = [
    (1, 'North Carolina'),
    (2, 'Kentucky'),
    (3, 'Houston'),
    (4, 'Kansas'),
    (5, 'Auburn'),
    (6, 'Iowa State'),
    (7, 'Wofford'),
    (8, 'Utah State'),
    (9, 'Washington'),
    (10, 'Seton Hall'),
    (11, 'Ohio State'),
    (12, 'New Mexico State'),
    (13, 'Northeastern'),
    (14, 'Georgia State'),
    (15, 'Abilene Christian'),
    (16, 'Iona'),
]
south = [
    (1, 'Virginia'),
    (2, 'Tennessee'),
    (3, 'Purdue'),
    (4, 'Kansas State'),
    (5, 'Wisconsin'),
    (6, 'Villanova'),
    (7, 'Cincinnati'),
    (8, 'Ole Miss'),
    (9, 'Oklahoma'),
    (10, 'Iowa'),
    (11, 'Saint Mary\'s'),
    (12, 'Oregon'),
    (13, 'UC Irvine'),
    (14, 'Old Dominion'),
    (15, 'Colgate'),
    (16, 'Gardner–Webb'),
]
divisions = []
divison_winners = {}
number_entry = input("Random Number Table (63 numbers):\n")
number_entry = number_entry.split('\t')
randomgenerator = randomnumbers(number_entry)

for name, team_list in [('EAST', east), ('WEST', west), ('MIDWEST', midwest),
                        ('SOUTH', south)]:
    div = Division(team_list, name)
    div.play_through()
    divisions.append(div)

for div in divisions:
    divison_winners[div.name] = div.winner
champ1 = Team.play_game(divison_winners['EAST'], divison_winners['WEST'])
champ2 = Team.play_game(divison_winners['MIDWEST'], divison_winners['SOUTH'])
print('\n\nFinalFour\n' + champ1.name + ', ' + champ2.name)
print('\nChamp: ' + Team.play_game(champ1, champ2).name)