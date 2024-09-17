This is an python implementation of the examples in the book "Mazes for Programmers" by Jamis Buck published by The Pragmatic Programmers.

It contains:
- Different type of cells, e.g. normal, 3d, triangle, etc.
- Grids that are build using these different type of cells
- Algorithms to create mazes
- Algorithm to solve and color the mazes
- Demo programs to demonstrate the funtioning of the algorithms
- Unit tests for a part of the code

For visualization of the mazes the Pilgrim module is used.
Pytest is used as the unit test framework.

The following open topics exist:
- The PolarCell contains a biased random pick (see also the errata sheet for the book). This effects the circular and sperical mazes.
