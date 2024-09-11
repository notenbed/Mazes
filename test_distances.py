from maze import Cell
from maze import Distances

def test_initialize_distance():
    c = Cell(2, 3)
    d = Distances(c)
    assert d.root == c
    assert d.cells[c] == 0

def test_get_item():
    c = Cell(2, 3)
    d = Distances(c)
    e = Cell(4, 5)
    assert d[c] == 0
    assert d[e] == None

def test_set_item():
    c = Cell(2, 3)
    e = Cell(3 ,4)
    d = Distances(c)
    d[e] = 3
    assert d[e] == 3

def test_get_keys():
    c = Cell(2, 3)
    e = Cell(3, 4)
    d = Distances(c)
    d[e] = 3
    assert d.all_cells() == list((c, e))