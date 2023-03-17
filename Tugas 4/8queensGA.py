
import random

POPULATION_SIZE = 100
MUTATION_RATE = 0.1
MAX_GENERATIONS = 1000

# Generate an initial population of chromosomes
def generate_population(size):
    population = []
    for i in range(size):
        chromosome = [random.randint(0, 7) for j in range(8)]
        population.append(chromosome)
    return population

# Evaluate the fitness of a chromosome
def evaluate_fitness(chromosome):
    threats = 0
    for i in range(8):
        for j in range(i+1, 8):
            if chromosome[i] == chromosome[j]:
                threats += 1
            elif abs(chromosome[i] - chromosome[j]) == abs(i - j):
                threats += 1
    return 28 - threats

# Perform roulette wheel selection on a population
def selection(population, fitness_values):
    total_fitness = sum(fitness_values)
    probabilities = [fitness / total_fitness for fitness in fitness_values]
    cumulative_probabilities = [sum(probabilities[:i+1]) for i in range(len(probabilities))]
    parents = []
    for i in range(len(population)):
        r = random.random()
        for j in range(len(cumulative_probabilities)):
            if r < cumulative_probabilities[j]:
                parents.append(population[j])
                break
    return parents

# Perform single point crossover between two parents
def crossover(parent1, parent2):
    crossover_point = random.randint(1, 6)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Mutate a chromosome by randomly changing the position of a queen
def mutate(chromosome):
    if random.random() < MUTATION_RATE:
        index = random.randint(0, 7)
        value = random.randint(0, 7)
        chromosome[index] = value
    return chromosome

# Solve the problem using genetic algorithm
def solve():
    population = generate_population(POPULATION_SIZE)
    for generation in range(MAX_GENERATIONS):
        # Evaluate the fitness of each chromosome
        fitness_values = [evaluate_fitness(chromosome) for chromosome in population]

        # Check if a solution is found
        if 28 in fitness_values:
            index = fitness_values.index(28)
            return population[index]

        # Select parents for crossover
        parents = selection(population, fitness_values)

        # Create offspring by crossover and mutation
        offspring = []
        for i in range(POPULATION_SIZE - len(parents)):
            parent1, parent2 = random.sample(parents, 2)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1)
            child2 = mutate(child2)
            offspring.append(child1)
            offspring.append(child2)

        # Replace the old population with the new one
        population = parents + offspring

    # If no solution is found, return the fittest chromosome
    fitness_values = [evaluate_fitness(chromosome) for chromosome in population]
    index = fitness_values.index(max(fitness_values))
    return population[index]

# Print the board with queens
def print_board(board):
    for row in range(8):
        line = ""
        for column in range(8):
            if board[row] == column:
                line += "Q "
            else:
                line += ". "
        print(line)
    print("\n")
        

num_solutions = int(input("Enter the number of solutions you want to generate: "))
for i in range(num_solutions):
    solution = solve()
    print("Solution ", i+1, ":")
    print_board(solution)
