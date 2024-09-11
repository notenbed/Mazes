from maze import TriangleGrid

def test_triangle_grid():
    grid = TriangleGrid(4, 4)
    assert grid[0, 0].neighbor("north") == None
    assert grid[0, 0].neighbor("south") == grid[1, 0]

    assert grid[0, 1].neighbor("north") == None
    assert grid[0, 1].neighbor("south") == None

    assert grid[3, 0].neighbor("north") == grid[2, 0]
    assert grid[3, 0].neighbor("soutn") == None

    assert grid[0, 0].neighbor("west") == None
    assert grid[0, 0].neighbor("east") == grid[0, 1]
    assert grid[0, 3].neighbor("west") == grid[0, 2]
    assert grid[0, 3].neighbor("east") == None
