import pygad
import numpy
import math

x = -11
y = 3.5

function_inputs = [x, y] 
desired_output = -7*x + 3*x*math.sin(y) - 786*y + 989

def fitness_func(ga_instance, solution, solution_idx):
    output = numpy.dot(solution, function_inputs)
    fitness = 1.0 / (numpy.abs(output - desired_output) + 0.000001) # Adding a small value to avoid division by zero.
    return fitness

fitness_function = fitness_func

num_generations = 100 # Number of generations.
num_parents_mating = 7 # Number of solutions to be selected as parents in the mating pool.

sol_per_pop = 50 # Number of solutions in the population.
num_genes = len(function_inputs)

last_fitness = 0
def callback_generation(ga_instance):
    global last_fitness
    print(f"Generation = {ga_instance.generations_completed}")
    print(f"Fitness    = {ga_instance.best_solution()[1]}")
    print(f"Change     = {ga_instance.best_solution()[1] - last_fitness}")
    last_fitness = ga_instance.best_solution()[1]


ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating, 
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop, 
                       num_genes=num_genes,
                       on_generation=callback_generation)

ga_instance.run()

# After Generation, plot will show 
ga_instance.plot_fitness()

# Returning the details of the best solution.
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print(f"Parameters of the best solution : {solution}")
print(f"Fitness value of the best solution = {solution_fitness}")
print(f"Index of the best solution : {solution_idx}")

prediction = numpy.dot(numpy.array(function_inputs), solution)
print(f"Predicted output based on the best solution : {prediction}")

if ga_instance.best_solution_generation != -1:
    print(f"Best fitness value reached after {ga_instance.best_solution_generation} generations.")

filename = 'genetic'
ga_instance.save(filename=filename)

loaded_ga_instance = pygad.load(filename=filename)
loaded_ga_instance.plot_fitness()
