from maze import Kruskals
from maze import WeaveGrid
import pytest

@pytest.fixture
def grid_prepare():
    grid = WeaveGrid(4, 4)
    state = Kruskals().State(grid)
    return grid, state


def test_state(grid_prepare):
    grid, state = grid_prepare
    assert state.grid == grid
    assert len(state.neighbors) == 24
    assert state.set_for_cell[grid[0, 0]] == 0
    assert state.set_for_cell[grid[0, 1]] == 1
    assert state.set_for_cell[grid[3, 3]] == 15
    assert state.cells_in_set[0] == [grid[0, 0]]
    assert state.cells_in_set[3] == [grid[0, 3]]
    assert [grid[0, 0], grid[0, 0].neighbor("east")] in state.neighbors
    assert [grid[0, 0], grid[0, 0].neighbor("south")] in state.neighbors
    assert [grid[3, 3], grid[3, 3].neighbor("east")] not in state.neighbors
    assert [grid[3, 3], grid[ 3, 3].neighbor("south")] not in state.neighbors

def test_state_merge(grid_prepare):
    grid, state = grid_prepare
    left = grid[0, 0]
    rank_left = state.set_for_cell[left]
    right = grid[0, 1]
    rank_right =state.set_for_cell[right]

    state.merge(left, right)
    assert left.contains_link(right)
    assert rank_right not in state.cells_in_set.keys()
    assert state.cells_in_set[rank_left] == [left, right]
    assert state.set_for_cell[right] == rank_left

    left = grid[0, 1]
    rank_left = state.set_for_cell[left]
    right = grid[0, 2]
    rank_right = state.set_for_cell[right]
    state.merge(left, right)
    assert rank_right not in state.cells_in_set.keys()
    assert state.cells_in_set[rank_left] == [grid[0, 0], left, right]
    assert state.set_for_cell[right] == rank_left

def test_can_merge(grid_prepare):
    grid, state = grid_prepare
    left = grid[0, 0]
    right = grid[0, 1]

    assert state.can_merge(left, right)

    state.merge(left, right)
    assert not state.can_merge(left, right)

def test_add_crossing(grid_prepare):
    grid, state = grid_prepare
    left = grid[2, 1]
    mid = grid[2, 2]
    right = grid[2, 3]
    state = Kruskals.State(grid)
    state.merge(left, mid)
    state.merge(mid, right)
    assert not state.add_crossing(left)
    assert state.add_crossing(grid[1, 2])