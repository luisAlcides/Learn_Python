class Calculate:
    def add(self, x, y):
        return x+y

    def div (self, x, y):
        if y == 0:
            raise ValueError('Division by zero error')
        return x / y