import random


POPULATION_SIZE=8
MUTATION_RATE=0.04
NUM_GENERATIONS = 50
ERROR_RANGE=3

# generate a initail random population
def initialize_population(size):
    return [(random.randint(0, 50), random.randint(0, 50)) for _ in range(size)] 

#function for fitness
def fitness(individual):
    p,q= individual
    return abs(4 *p + 3 *q - 60)  #4p+3q=60
   

#selection function
def select_parents(population , fitnesses):
    total_fitnesses = sum(fitnesses)
    probabilities = [1 - (f / total_fitnesses) for f in fitnesses]
    parent1 = population[random.choices(range(len(population)), weights=probabilities, k=1)[0]]
    parent2=parent1
    while parent2== parent1:
        # parent2=population[random.choices(range(len(population)),weights=probabilities.k=1)[1]]
        return parent1,parent2

def to_binary(individual):
   x,y=individual
   return f"{x:06b}{y:06b}"




def from_binary(binary_str):
    x = int(binary_str[:6], 2)
    y = int(binary_str[6:], 2)
    return x, y

def crossover(parent1,parent2):
    binary1 =to_binary(parent1)
    binary2 =to_binary(parent2)
    crossover_point=random.randint(0,len(binary1) - 1) 
    child_binary1= binary1[:crossover_point] + binary2[crossover_point:]
    child_binary2= binary2[:crossover_point] + binary1[crossover_point:]
    return from_binary(child_binary1),from_binary(child_binary2)
    
def mutate(individual,mutation_rate):
    binary = to_binary(individual)
    binary = list(binary)
    for i in range(len(binary)):
        if random.random() < mutation_rate:
            binary[i] = '1' if binary[i] == '0' else '0'
    mutated_individual =from_binary("".join(binary))
    return mutated_individual
   

def genetic_algorithm():
    population = initialize_population(POPULATION_SIZE)
    print(f"Initial population: {population}")
    
    for generation in range(NUM_GENERATIONS):
        fitnesses=[fitness(individual) for individual in population]
        print(f"Fitnesses: {fitnesses}")
          
        
        print(f"Generation {generation}:Best fitness = {min(fitnesses)}")

        if min(fitnesses) <= ERROR_RANGE:
            best_index =fitnesses.index(min(fitnesses))
            return population[best_index],generation
       
        new_population = []

        for _ in range(POPULATION_SIZE //2):
            parent1,parent2 = select_parents(population,fitnesses)
            print(f"Selected parents: {parent1},{parent2}")
            child1,child2=crossover(parent1,parent2)
            child1= mutate(child1, MUTATION_RATE)
            child2 = mutate(child2,MUTATION_RATE)
            new_population.extend([child1,child2])
            
        population =new_population

    best_index=fitnesses.index(min(fitnesses))
    return population[best_index],NUM_GENERATIONS
    
solution,generations=genetic_algorithm()
print(f"Solution is found:x = {solution[0]},y = {solution[1]} in {generations} generations")
