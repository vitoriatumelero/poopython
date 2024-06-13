class Calculadora:
    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b


calc = Calculadora()
print(calc.somar(10, 5))  # Output: 15
res= calc.subtrair(10, 5)  # Output: 5
print (res)