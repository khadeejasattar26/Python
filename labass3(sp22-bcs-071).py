#assignment3
import random
import math

# Number of points and individuals
noof_points = 15
noof_individuals = 45
noof_generations = 100  # Number of generations

# Generate 15 random points with integer coordinates within the range 0-5 for both x and y
def generate_points(noof_points):
    points = set()
    while len(points) < noof_points:
        x = random.randint(0, 5)
        y = random.randint(0, 5)
        points.add((x, y))
    return list(points)

#functions to calculate distance between two points and total distance of a route
def distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

def total_distance(path):
    total = 0
    for i in range(len(path) - 1):
        total += distance(path[i], path[i+1])
    return total

# Generate initial population by randomly permuting the set of points
points = generate_points(noof_points)
population = [random.sample(points, len(points)) for _ in range(noof_individuals)]

# Main genetic algorithm function
def genetic_algorithm(population, noof_generations, num_parents, mutation_rate):
    for generation in range(noof_generations):
        # Calculate fitness 
        fitnesses = [total_distance(route) for route in population]
        print(f"Generation {generation+1}, Best fitness: {min(fitnesses)}")
        
       
        parents = random.sample(population, num_parents)
        
        # Create new routes by combining and mutating parents
        new_population = []
        for _ in range(noof_individuals):
            parent1, parent2 = random.sample(parents, 2)
            cut = random.randint(0, noof_points)
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

genetic_algorithm(population, noof_generations, 20, 0.05)
