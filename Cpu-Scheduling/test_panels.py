import matplotlib
matplotlib.use('TkAgg')  # Use TkAgg backend for interactive plots

import matplotlib.pyplot as plt
import matplotlib.animation as animation

lists = [[], [], [], []]  # Example lists
object_name = 'Object_1'

def update(frame):
    # Clear the plot
    plt.clf()

    # Move object to the next list
    current_list = lists[frame % len(lists)]
    current_list.append(object_name)

    # Plot the lists and object
    for i, lst in enumerate(lists):
        plt.text(i * 2, 0, f'Tile {i+1}', ha='center', fontsize=12)
        for j, obj in enumerate(lst):
            plt.text(i * 2, j + 1, obj, ha='center', fontsize=10)

fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, update, frames=range(10), interval=1000)

plt.show()
