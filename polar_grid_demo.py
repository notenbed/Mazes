from maze import PolarGrid

# The algorithm has a tendency to favor the north boundaries to be
# removed.
# It needs an altenative random-Choice which decided between 
# the available neighbors first based on direction and if it
# is the north then between the available north boundaries

grid = PolarGrid(8)

filename = "polar.png"
grid.to_img(filename=filename)

print("saved to ", filename)
