import os

POPULATION_DATA = "world_population.csv"


def load_population_data():
    with open(os.path.join("backup_data", POPULATION_DATA), "r") as r:

        for line in r:
            print(line)

if __name__ == "__main__":
    load_population_data()
