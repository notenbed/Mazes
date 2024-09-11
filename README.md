This is an python implementation of the examples in the book "Mazes for Programmers" by Jamis Buck published by The Pragmatic Programmers.

I used the opportunity the experiment a little with pytest and therefor for a part of the code there are pytests available.

The following open topics exist:
- Wilsons.py does not produce a proper result
- PolarCell throughs an error and therefor PolarGrid and SphereGrid don't work
- Also the PolarCell contains a biased random pick (see also the errate sheet for the book)
- ColoredGrid does not function with that start at an random self determined point
- Mazes with inset don't get colored
- MobiusGrid and CylinderGrid produce a grid with a top with cell with no east-west links
- Cube outlines are overwritten 
