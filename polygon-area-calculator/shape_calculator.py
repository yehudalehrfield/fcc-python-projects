class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return (2 * self.height) + (2 * self.width)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        # filled in or border?
        picString = ''
        # # BORDER:
        # picString += '*' * self.width + '\n'
        # for unit in range(self.height):
        #     picString += '*' + ' ' * (self.width - 2) + '*\n'
        # picString += '*' * self.width + '\n'
        # # FILLED IN
        for unit in range(self.height):
            picString += '*' * self.width + '\n'
        return picString

    def get_amount_inside(self, otherRect):
        otherRectW = otherRect.width
        otherRectH = otherRect.height

        # 1. We don't need this. 2. Is the logic correct?
        if (otherRect.width > self.width and otherRect.width > self.height and otherRect.height > self.height and otherRect.width > self.height):
            return 0

        # 1. Orientation 1
        # 2. Check how many fit width-wise, save as fitWide
        # 3. Check how many fit height-wise, save as fitHigh
        # 4. orientation1Fit = fitWide * fitHigh
        # 5. Flip orientation
        # 6. Repeat calcs, save as orientation2Fit
        # 7. return max(orienation1Fit, orientation2Fit)

        fitWide = self.width // otherRect.width
        fitHigh = self.height // otherRect.height
        orientation1Fit = fitWide * fitHigh

        fitWide = self.width // otherRect.height
        fitHigh = self.height // otherRect.width
        orientation2Fit = fitWide * fitHigh

        return max(orientation1Fit, orientation2Fit)

    def __str__(self):
        return 'Rectangle(width={}, height={})'.format(self.width, self.height)


class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def set_side(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return 'Square(side={})'.format(self.width)
