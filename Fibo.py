class Fibonacci:
    def __init__(self,input):
        self.input = input
    def fib2(self):
        result = []
        a = 0
        b = 1
        while b < self.input:
            result.append(b)
            a = b
            b = a+ b
        return result