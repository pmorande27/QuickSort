import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import time

def swap(A, i, j):

    if i != j:
        A[i], A[j] = A[j], A[i]

def quicksort(A, start, end):
    if start >= end:
        return

    pivot = A[end]
    pivotIdx = start

    for i in range(start, end):
        if A[i] < pivot:
            swap(A, i, pivotIdx)
            pivotIdx += 1
        yield A
    swap(A, end, pivotIdx)
    yield A

    yield from quicksort(A, start, pivotIdx - 1)
    yield from quicksort(A, pivotIdx + 1, end)
N =200
A = [x + 1 for x in range(N)]

random.seed(time.time())
random.shuffle(A)
generator = quicksort(A, 0, N - 1)
title = "A"
# Initialize figure and axis.
fig, ax = plt.subplots()
ax.set_title(title)

# Initialize a bar plot. Note that matplotlib.pyplot.bar() returns a
# list of rectangles (with each bar in the bar plot corresponding
# to one rectangle), which we store in bar_rects.
bar_rects = ax.bar(range(len(A)), A, align="edge")

# Set axis limits. Set y axis upper limit high enough that the tops of
# the bars won't overlap with the text label.
ax.set_xlim(0, N)
ax.set_ylim(0, int(1.07 * N))

# Place a text label in the upper-left corner of the plot to display
# number of operations performed by the sorting algorithm (each "yield"
# is treated as 1 operation).
text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

# Define function update_fig() for use with matplotlib.pyplot.FuncAnimation().
# To track the number of operations, i.e., iterations through which the
# animation has gone, define a variable "iteration". This variable will
# be passed to update_fig() to update the text label, and will also be
# incremented in update_fig(). For this increment to be reflected outside
# the function, we make "iteration" a list of 1 element, since lists (and
# other mutable objects) are passed by reference (but an integer would be
# passed by value).
# NOTE: Alternatively, iteration could be re-declared within update_fig()
# with the "global" keyword (or "nonlocal" keyword).
iteration = [0]
def update_fig(A, rects, iteration):
    for rect, val in zip(rects, A):
        rect.set_height(val)
    iteration[0] += 1
    text.set_text("# of operations: {}".format(iteration[0]))

anim = animation.FuncAnimation(fig, func=update_fig,
    fargs=(bar_rects, iteration), frames=generator, interval=1,
    repeat=False)
plt.show()