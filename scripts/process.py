import os
import csv

POPULATION_DATA = "world_population.csv"
SPENDING_DATA = "pharmaceutical_spending.csv"
SPENDING_TOTAL_USD = "pharmaceutical_total_spending.csv"


def load_population_data():
    population_data = {}
    with open(os.path.join("../raw_data", POPULATION_DATA), 'rb') as csv_file:
        population_reader = csv.reader(csv_file, delimiter=',', quotechar='|')
        next(population_reader, None)
        for line in population_reader:
            country, year, population = line[0].replace('"', ''), line[5].replace('"', ''), line[6].replace('"', '')
            if country not in population_data:
                population_data[country] = {}
            population_data[country][int(year)] = float(population)

    return population_data


def load_spending_data():
    spending_data = {}
    with open(os.path.join("../raw_data", SPENDING_DATA), 'rb') as csv_file:
        spending_reader = csv.reader(csv_file, delimiter=',', quotechar='|')
        next(spending_reader, None)
        for line in spending_reader:
            country = line[0].replace('"', '')
            if country not in spending_data:
                spending_data[country] = {}

    return spending_data


def generate_spending_data(population):
    final_data = []
    with open(os.path.join("../raw_data", SPENDING_DATA), 'rb') as csv_file:
        spending_reader = csv.reader(csv_file, delimiter=',', quotechar='|')
        header = next(spending_reader)
        header.append('"TotalValue"')
        new_header = ",".join(header)
        final_data.append(new_header)
        for line in spending_reader:
            measure = line[3].replace('"', '')
            if measure == 'USD_CAP':
                country, year, spend_per_cap = line[0].replace('"', ''), \
                                               int(line[5].replace('"', '')), \
                                               float(line[6].replace('"', ''))
                if country in population and year in population[country]:
                    total = spend_per_cap * population[country][year]
                    line.append(str(total))

                else:
                    line.append('0')
                final_data.append(",".join(line))
    with open(os.path.join("../data", SPENDING_TOTAL_USD), 'wt') as final_file:
        for l in final_data:
            final_file.write(l.replace('"', '') + '\n')


if __name__ == "__main__":
    p = load_population_data()
    generate_spending_data(p)
