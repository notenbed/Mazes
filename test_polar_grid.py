from maze import PolarGrid

def test_initialize():
    grid = PolarGrid(4)
    assert grid.rows == 4
    assert grid.columns == 1