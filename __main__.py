from teams import get_teams_file
from simulator import Team

TEAMS_FILENAME = 'teams_2021.json'
DIVISION_MATCHUPS = [['East', 'West'], ['Midwest', 'South']]

def randomnumbers(provided_numbers: Iterable[str]):
    # Recommended: Get your random numbers from
    # https://www.random.org/integers/?num=63&min=0&max=999&col=63&base=10&format=plain&rnd=new
    for x in provided_numbers:
        yield int(x)


number_entry = input("Random Number Table (63 numbers):\n")
number_entry = number_entry.split()
random_generator = randomnumbers(number_entry)

divisions = get_teams_file(TEAMS_FILENAME)
final_four = {division.name: division.play_through(random_generator)
              for division in divisions}
championship = [Team.play_game(final_four[div_a], final_four[div_b],
                               next(random_generator))
                for div_a, div_b in DIVISION_MATCHUPS]
champion = Team.play_game(*championship, next(random_generator))

print('\n\nFinalFour\n' + championship[0].name + ', ' + championship[1].name)
print('\nChamp: ' + champion.name)
