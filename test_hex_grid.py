from maze import HexGrid

def test_neighbors():
    grid = HexGrid(8, 8)

    assert grid[0, 0].neighbor("northwest") == None
    assert grid[0, 0].neighbor("northeast") == None
    assert grid[0, 0].neighbor("southwest") == None
    assert grid[7, 7].neighbor("southeast") == None
    assert grid[7, 0].neighbor("southwest") == None

    assert grid[0, 0].neighbor("southeast") == grid[0, 1]

    assert grid[1, 1].neighbor("northwest") == grid[1, 0]
    assert grid[1, 1].neighbor("northeast") == grid[1, 2]
    assert grid[1, 1].neighbor("southeast") == grid[2, 2]
    assert grid[1, 1].neighbor("southwest") == grid[2, 0]

    assert grid[1, 2].neighbor("northwest") == grid[0, 1]
    assert grid[1, 2].neighbor("northeast") == grid[0, 3]
    assert grid[1, 2].neighbor("southwest") == grid[1, 1]
    assert grid[1, 2].neighbor('southeast') == grid[1, 3]