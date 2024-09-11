from maze import Grid

class ColoredGrid(Grid):
    def distances(self, distances):
        self._distances = distances
        self.maximum = max(distances.values())
        farthest = self.maximum

    def background_color_for(self, cell):
        if self._distances[cell] == None:
            distance = 0
        else:
            distance = self._distances[cell]

        intensity = float((self.maximum - distance)) / self.maximum
        dark = round(255 * intensity)
        bright = round(128 + (127 * intensity))
        return (dark, bright, dark)