#Assignment 3
import random
import math

# Generate 15 random points (cities) within the range (0-5, 0-5).
cities = [(random.uniform(0, 5), random.uniform(0, 5)) for _ in range(15)]

# Define functions for calculating distance, creating an initial population, evaluating fitness,
# selecting parents for crossover, performing crossover, and mutating individuals.
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def createPopulation(size):
    return [[random.randint(0, 1) for _ in range(15)] for _ in range(size)]

def evaluateFitness(population):
    return [sum([distance(cities[i], cities[j]) for j in range(15)]) for i in range(15)]

def selectParents(population, fitness):
    totalFitness = sum(fitness)
    index1 = random.uniform(0, totalFitness)
    index2 = random.uniform(0, totalFitness)
    parent1 = 0
    parent2 = 0
    for i in range(15):
        if index1 < fitness[i]:
            parent1 = i
            break
        index1 -= fitness[i]
    for i in range(15):
        if index2 < fitness[i]:
            parent2 = i
            break
        index2 -= fitness[i]
    return parent1, parent2

def crossover(parent1, parent2):
    child = [0] * 15
    for i in range(15):
        if random.random() < 0.5:
            child[i] = parent1[i]
        else:
            child[i] = parent2[i]
    return child

def mutate(individual):
    for i in range(15):
        if random.random() < 0.1:
            individual[i] = 1 - individual[i]
    return individual

# Implement the genetic algorithm loop to evolve the population over generations
population = createPopulation(50)
fitness = evaluateFitness(population)
for generation in range(100):
    offspring = []
    while len(offspring) < len(population):
        parent1, parent2 = selectParents(population, fitness)
        child = crossover(population[parent1], population[parent2])
        if random.random() < 0.1:
            child = mutate(child)
        offspring.append(child)
    population = offspring
    fitness = evaluateFitness(population)

# Print the best solution found
best = min(fitness)
print("Best solution:")
for i in range(15):
    if population[fitness.index(best)][i] == 1:
        print(cities[i])

# Print the total distance of the best solution
print("Total distance:", best)
