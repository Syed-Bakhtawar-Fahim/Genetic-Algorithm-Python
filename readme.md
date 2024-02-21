## Genetic Algorithm Optimization with Python

This repository contains Python code implementing a genetic algorithm (GA) to optimize the weights for a given equation. The GA is implemented using the `pygad` library.

### Equation to Optimize

The equation we aim to optimize is:

\[ z = -7x_2 + 3x \cdot \sin(y) - 786y + 989 \]

Where:

- x = -11
- y = 3.5

### Fitness Function

The fitness of each solution in the population is calculated using the absolute difference between the output of the equation and the desired output. The fitness function is defined as:

```python
def fitness_func(ga_instance, solution, solution_idx):
    output = numpy.dot(solution, function_inputs)
    fitness = 1.0 / (numpy.abs(output - desired_output) + 0.000001) # Adding a small value to avoid division by zero.
    return fitness

```

## Genetic Algorithm Parameters

- **num_generations**: Number of generations.
- **num_parents_mating**: Number of solutions to be selected as parents in the mating pool.
- **sol_per_pop**: Number of solutions in the population.
- **num_genes**: Number of genes in each solution (equal to the number of function inputs).

## Callback Function

A callback function `callback_generation` is defined to print the generation number, best fitness value, and change in fitness value compared to the previous generation.

## Running the Genetic Algorithm

1. Create an instance of the `pygad.GA` class with the specified parameters and fitness function.
2. Run the GA using the `run()` method.

## Results

- After each generation, a plot showing the fitness values' evolution is displayed.
- The best solution's parameters, fitness value, and index are printed.
- The predicted output based on the best solution is computed.

## Saving and Loading the GA Instance

- The GA instance is saved to a file using the `save()` method.
- The saved GA instance is loaded from the file, and its fitness evolution is plotted.

## Dependencies

- `pygad`: A library for implementing genetic algorithms.
- `numpy`: A library for numerical computations.
- `math`: A library for mathematical functions.

## Running the Code

1. Clone this repository.
2. Ensure you have the required dependencies installed (`pygad`, `numpy`, `math`).
3. Run the Python script.
