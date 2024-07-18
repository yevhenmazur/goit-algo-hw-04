'''

This module calculates the execution time of the sorting algorithms,
depending on the size of the array, as well as how much data in this array is already sorted.
The calculation results are displayed on the Heatmap.

!!! Attention! It can take for a long time !!!

'''
import timeit
import random
import matplotlib.pyplot as plt
import numpy as np
from sorting_algorithms import insertion_sort
from sorting_algorithms import merge_sort


def measure_execution_time(algorithm: str, unsorted_list: list) -> float:
    if algorithm == "timsort":
        t = timeit.Timer(lambda: unsorted_list.sort())
    else:
        func = getattr(__import__('__main__'), algorithm)
        t = timeit.Timer(lambda: func(unsorted_list))
    execution_time = t.timeit(number=1)

    return execution_time


def generate_unsorted_list(size: int, mixing_factor: int) -> list:
    """
    Generates a list of specified size with elements partially shuffled according to the mixing factor.

    Args:
        size (int): The size of the list to generate.
        mixing_factor (int): The number of chunks to divide the list into. The larger the mixing factor,
                             the fewer elements are shuffled within the list. A mixing_factor of 1 means no shuffling,
                             while a mixing_factor equal to size means the entire list is shuffled.

    Returns:
        list: The resulting list with elements partially shuffled.
    """

    lst = list(range(size))
    chunk_size = size // mixing_factor

    # Create sublists
    chunks = list()
    for i in range(mixing_factor):
        sublist = lst[i:i + chunk_size]
        chunks.append(sublist)

    # Select random 'mixing_factor - 1' items from chunks and mix their content
    mixed_list = list()
    for _ in range(len(chunks) - 1):
        random_chunk = random.choice(chunks)
        chunks.remove(random_chunk)
        random.shuffle(random_chunk)
        mixed_list.extend(random_chunk)

    # Paste an unmixed fragment to a random position
    insert_position = random.randint(0, len(mixed_list))
    mixed_list[insert_position:insert_position] = chunks[0]

    return mixed_list


def create_heatmap(algorithm, ax):

    size_range = range(1, 10_001, 1000)
    mix_factor_range = range(1, 101, 10)
    execution_times = np.zeros((len(size_range), len(mix_factor_range)))

    for i, size in enumerate(size_range):
        for j, mix_factor in enumerate(mix_factor_range):
            unsorted_list = generate_unsorted_list(size, mix_factor)
            execution_time = measure_execution_time(
                algorithm=algorithm, unsorted_list=unsorted_list)
            execution_times[i, j] = execution_time

    # Plot the heatmap
    im = ax.imshow(execution_times, aspect='auto', origin='lower',
                   cmap='viridis', extent=[1, 100, 1, 10_000])
    ax.set_title(f'Execution Time of {algorithm} Algorithm')
    ax.set_xlabel('Mixing Factor')
    ax.set_ylabel('Array size')
    ax.set_xticks(range(0, 101, 10))
    ax.set_yticks(range(0, 10001, 1000))

    # Add execution times as text annotations
    for i in range(len(size_range)):
        for j in range(len(mix_factor_range)):
            text = ax.text(j * 10 + 5, i * 1000 + 500, f"{execution_times[i, j]*1000:.2f}",
                           color="white", ha="center", va="center", fontsize=8)

    return im


def main():

    # Create subplots for each algorithm
    algorithms = ['timsort', 'insertion_sort', 'merge_sort']
    fig, axs = plt.subplots(1, len(algorithms), figsize=(
        15, 6), sharey=True, subplot_kw={'aspect': 'auto'})

    for idx, algorithm in enumerate(algorithms):
        ax = axs[idx]
        im = create_heatmap(algorithm, ax)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
