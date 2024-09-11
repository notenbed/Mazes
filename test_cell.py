from maze import Cell

def test_creation():
    c = Cell(2, 3)
    assert c.row == 2
    assert c. column == 3
    assert c.links == []

def test_link_unlink():
    c = Cell(2, 3)
    d = Cell(2, 4)
    c.link(d)
    assert c.links == [d]
    assert d.links == [c]

    c.unlink(d)
    assert c.links == []
    assert d.links == []

    c.link(d, bidi=False)
    assert c.links == [d]
    assert d.links == []

    c.unlink(d, bidi = False)
    assert c.links == []
    assert d.links == []

def test_retrieve_links():
    c = Cell(2,3)
    d = Cell(2,4)
    e = Cell(1,3)
    f = Cell(1,2)
    c.link(d)
    c.link(e)
    assert c.get_links() == [d, e]
    assert f.get_links() == []

def test_contains_link():
    c = Cell(2,3)
    d = Cell(2,4)
    e = Cell(1,3)
    c.link(d)
    
    assert c.contains_link(d) == True
    assert c.contains_link(e) == False

def test_neighbors():
    c = Cell(2, 3)
    d = Cell(1, 3)
    c.add_neighbor("north", d)
    assert c.neighbor("south") == None
    assert c.neighbor("north") == d

def test_each_neighbor():
    c = Cell(2, 3)
    d = Cell(1, 3)
    c.add_neighbor("north", d)
    assert list(c.each_neighbor()) == [d]
    assert list(d.each_neighbor()) == []

def test_neighbors():
    c = Cell(2, 3)
    d = Cell(1, 3)
    c.add_neighbor("north", d)
    assert c.neighbors() == [d]
    assert d.neighbors() == []

def test_neighbors_second_degree():
    a = Cell(1, 2)
    b = Cell(2, 2)
    c = Cell(3, 2)
    c.add_neighbor("north", b)
    b.add_neighbor("north", a)
    b.add_neighbor("south", c)
    assert c.neighbor("north").neighbor("north") == a