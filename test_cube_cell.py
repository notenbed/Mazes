from maze import CubeCell

def test_init():
    cell = CubeCell(5, 0, 1)
    assert cell.row == 0
    assert cell.column == 1
    assert cell.face == 5

def test_neighbors():
    cell = CubeCell(5, 0, 5)
    assert cell.neighbors() == []

    cell_south = CubeCell(5, 1, 5)
    cell.add_neighbor("south", cell_south)
    assert cell.neighbors() == [cell_south]
    assert cell.neighbor("south") == cell_south

    cell.remove_neighbor("south")
    assert cell.neighbors() == []
    assert cell.neighbor("south") == None