from maze import CubeGrid
import pytest

@pytest.fixture
def prepare_grid():
    grid = CubeGrid(4)
    return grid

def test_init(prepare_grid):
    grid = prepare_grid
    assert grid.rows == 4
    assert grid.columns == 4
    assert len(grid.grid) == 6
