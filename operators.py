
class Calc_Test:

    def modulo(self, num1, num2):
        return num1 % num2

    def cm_inch(self, num1):
        return num1 * 2.54

    def inch_cm(self, num1):
        return num1 * 0.393901

sharp = Calc_Test()

print(sharp.modulo(10, 5))