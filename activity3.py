import random
import math

# Number of points and individuals
num_points = 15
num_individuals = 45
num_generations = 100  # Number of generations

# Generate 15 random points with integer coordinates within the range 0-5 for both x and y
points = [(random.randint(0, 5), random.randint(0, 5)) for _ in range(num_points)]

# Define functions to calculate distance between two points and total distance of a route
def distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

def total_distance(route):
    return sum(distance(route[i-1], route[i]) for i in range(1, len(route)))

# Generate initial population by randomly permuting the set of points
population = [random.sample(points, len(points)) for _ in range(num_individuals)]

# Main genetic algorithm function
def genetic_algorithm(population, num_generations, num_parents, mutation_rate):
    for generation in range(num_generations):
        # Calculate fitness of each route
        fitnesses = [total_distance(route) for route in population]
        print(f"Generation {generation+1}, Best fitness: {min(fitnesses)}")
        
        # Randomly select parents for crossover
        parents = random.sample(population, num_parents)
        
        #  Create new routes by combining and mutating parents
        new_population = []
        for _ in range(num_individuals):
            parent1, parent2 = random.sample(parents, 2)
            cut = random.randint(0, num_points)
            child = parent1[:cut] + [p for p in parent2 if p not in parent1[:cut]]
            child = mutate(child, mutation_rate)
            new_population.append(child)
        
        population = new_population

# Mutation function
def mutate(individual, mutation_rate=0.1):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(len(individual)), 2)
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
    return individual


print("Initial population:")
for route in population:
    print(route)


genetic_algorithm(population, num_generations, 20, 0.05)
