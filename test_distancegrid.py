from maze import DistanceGrid
from maze import Cell

def test_initialize_distancegrid():
    g = DistanceGrid(4, 5)
    assert g.distances == {}

def test_contents_of():
    g = DistanceGrid(4, 5)
    c = Cell(3, 4)
    assert g.contents_of(c) == " "
    g.distances[c] = 4
    assert g.distances[c] == 4
    assert g.contents_of(c) == "4"
    g.distances[c] = 10
    assert g.contents_of(c) == "A"