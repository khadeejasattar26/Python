import random

# Constants
POPULATION_SIZE = 100
GENERATIONS = 1000
MUTATION_RATE = 0.01
TARGET = 50
ERROR_MARGIN = 2

# Individual class representing (x, y) pair
class Individual:
    def __init__(self, x=None, y=None):
        if x is None:
            self.x = random.uniform(0, TARGET // 3)
        else:
            self.x = x
        if y is None:
            self.y = random.uniform(0, TARGET // 2)
        else:
            self.y = y
        self.fitness = self.calculate_fitness()

    def calculate_fitness(self):
        equation_result = 3 * self.x + 2 * self.y
        return abs(TARGET - equation_result)

    def mutate(self):
        if random.random() < MUTATION_RATE:
            self.x += random.uniform(-1, 1)
        if random.random() < MUTATION_RATE:
            self.y += random.uniform(-1, 1)
        self.fitness = self.calculate_fitness()

# Generate initial population
def generate_initial_population(size):
    return [Individual() for _ in range(size)]

# Selection function to select parents
def selection(population):
    population = sorted(population, key=lambda ind: ind.fitness)
    return population[:2]

# Crossover function to create children from parents
def crossover(parent1, parent2):
    child1 = Individual((parent1.x + parent2.x) / 2, (parent1.y + parent2.y) / 2)
    child2 = Individual((parent1.x + parent2.x) / 2, (parent1.y + parent2.y) / 2)
    return child1, child2

# Main genetic algorithm function
def genetic_algorithm():
    population = generate_initial_population(POPULATION_SIZE)
    
    for generation in range(GENERATIONS):
        # Selection
        parents = selection(population)

        # Crossover
        children = []
        for _ in range(POPULATION_SIZE // 2):
            child1, child2 = crossover(parents[0], parents[1])
            children.append(child1)
            children.append(child2)

        # Mutation
        for child in children:
            child.mutate()

        # Next generation
        population = parents + children

        # Convergence check
        best_individual = min(population, key=lambda ind: ind.fitness)
        if best_individual.fitness <= ERROR_MARGIN:
            print(f"Solution found: x = {best_individual.x}, y = {best_individual.y}, fitness = {best_individual.fitness}")
            return best_individual

        # Print progress
        if generation % 100 == 0:
            print(f"Generation {generation}: Best fitness = {best_individual.fitness}")

    print(f"No exact solution found in {GENERATIONS} generations. Best solution: x = {best_individual.x}, y = {best_individual.y}, fitness = {best_individual.fitness}")
    return best_individual

if __name__ == "__main__":
    genetic_algorithm()
