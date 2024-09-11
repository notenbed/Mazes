import random
from PIL import Image

class Mask:
    def __init__(self, rows, columns):
        self.rows, self.columns = rows, columns
        self.bits = [[True for i in range(self.columns)] for i in range(self.rows)]

    def __getitem__(self, x):
        if x[0] in range(0, self.rows) and x[1] in range(0, self.columns):
            return self.bits[x[0]][x[1]]
        else:
            return False
        
    def __setitem__(self, x, val):
        self.bits[x[0]][x[1]] = val

    def count(self):
        total = 0
        for row in self.rows:
            for col in self.columns:
                total += 1 if self.bits[row][col] else total

        return total
    
    def random_location(self):
        while True:
            row = random.randint(0, self.rows-1)
            col = random.randint(0, self.columns-1)

            if self.bits[row][col]:
                return [row, col] 
            
    def from_txt(file):
        with open(file) as f:
            line = f.readline()
            txt = []
            while line:
                line = line.strip()
                txt.append(line)
                line = f.readline()
            columns = len(txt[0])
            rows = len(txt)

            mask = Mask(rows, columns)
            for row, line in enumerate(txt):
                for col in range(len(line)):
                    if txt[row][col] == "X":
                        mask[row, col] = False
                    else:
                        mask[row, col] = True
        return mask

    def from_png(file):
        image = Image.open(file)
        mask = Mask(image.height, image.width)
        for row in range(0, mask.rows):
            for col in range(0, mask.columns):
                #image has its dimensions widthxheight
                data = image.getpixel((col, row))
                if data[0] == 0 and data[1] == 0 and data[2] == 0:
                    mask[row, col] = False
                else:
                    mask[row, col] = True
    
        return mask
    

                
