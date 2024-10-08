from maze import Grid

class DistanceGrid(Grid):
    def __init__(self, rows, columns):
        super().__init__(rows, columns)
        self.distances = {}
    
        
    def __base36encode(self, number, alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    #"""  Converts an integer to a base36 string."""
        if not isinstance(number, (int)):
            raise TypeError('number must be an integer')

        base36 = ''
        sign = ''

        if number < 0:
            sign = '-'
            number = -number

        if 0 <= number < len(alphabet):
            return sign + alphabet[number]

        while number != 0:
            number, i = divmod(number, len(alphabet))
            base36 = alphabet[i] + base36

        return sign + base36

    def contents_of(self, cell):
        if cell in self.distances:
            return self.__base36encode(self.distances[cell])
        else:
            return super().contents_of(cell)