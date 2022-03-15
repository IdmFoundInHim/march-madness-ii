import sys
from typing import Iterable, SupportsInt

from teams import get_teams_file
from simulator import Team, better_grouper_two

gender = 'm'
if '-w' in sys.argv:
    gender = 'w'
elif '-m' in sys.argv:
    gender = 'm'

TEAMS_FILENAME = f'teams_2022{gender}.json'
DIVISION_MATCHUPS_MEN = [['East', 'West'], ['Midwest', 'South']]
DIVISION_MATCHUPS_WOMEN = [['Greensboro', 'Wichita'], ['Spokane', 'Bridgeport']]

def randomnumbers(provided_numbers: Iterable[SupportsInt]):
    # Recommended: Get your random numbers from
    # https://www.random.org/integers/?num=63&min=0&max=999&col=63&base=10&format=plain&rnd=new
    for x in provided_numbers:
        yield int(x)


number_entry = input("Random Number Table (63 numbers):\n")
number_entry = number_entry.split()
random_generator = randomnumbers(number_entry)

divisions = get_teams_file(TEAMS_FILENAME)
division_matchups = better_grouper_two(d.name for d in divisions)
final_four = {division.name: division.play_through(random_generator)
              for division in divisions}
championship = [Team.play_game(final_four[div_a], final_four[div_b],
                               next(random_generator))
                for div_a, div_b in division_matchups]
champion = Team.play_game(*championship, next(random_generator))

print("\n\nFinalFour\n" + championship[0].name + ", " + championship[1].name)
print("\nChamp: " + champion.name)
