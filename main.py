from MatrixCalc import Calc
#Task: determinate Berechnen
#Task: Gaußverfahren
#Task: Invertieren
#Task: Diagonalisieren
#Task: Kern bestimmen

TestMatrix = [[1, 2, 3],
              [4, 10, 6],
              [7, 8, 9]]

calc = Calc(TestMatrix)

print(f"det is {calc.getDet()}")

print(f"Has it a kern: {calc.it_has_a_kern()}")
calc.Gauß_on()
calc.print()
