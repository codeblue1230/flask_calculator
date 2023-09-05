class Calculator():
    def __init__(self, numOne, numTwo):
        self.num1 = numOne
        self.num2 = numTwo

    def add_the_numbers(self):
        return self.num1 + self.num2

    def subtract_the_numbers(self):
        return self.num1 - self.num2

    def multiply_the_numbers(self):
        return self.num1 * self.num2

    def divide_the_numbers(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Division by zero is not allowed."