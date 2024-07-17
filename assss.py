import random
import math

# Generate random points
def generate_points(num_points):
    points = set()
    while len(points) < num_points:
        x = random.randint(0, 5)
        y = random.randint(0, 5)
        points.add((x, y))
    return points

# Calculate distance between two points
def distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Calculate total distance of a path
def total_distance(path):
    total = 0
    for i in range(len(path) - 1):
        total += distance(path[i], path[i+1])
    return total

# Generate initial population
def generate_population(pop_size, num_points):
    population = []
    for _ in range(pop_size):
        points = generate_points(num_points)
        population.append(list(points))
    return population

# Calculate fitness of each individual in the population
def calculate_fitness(population):
    fitness_values = []
    for individual in population:
        fitness_values.append(total_distance(individual))
    return fitness_values

# Main function
def main():
    random.seed(42)  # For reproducibility
    num_points = 15
    pop_size = 45
    num_generations = 10

    population = generate_population(pop_size, num_points)
    print("Initial population:")
    for ind in population:
        print(ind)

    for generation in range(num_generations):
        fitness_values = calculate_fitness(population)
        print(f"Generation {generation+1} - Average Fitness: {sum(fitness_values)/len(fitness_values)}")
        # Perform selection, crossover, and mutation here
        # For simplicity, skipping those steps in this example

if __name__ == "__main__":
    main()
