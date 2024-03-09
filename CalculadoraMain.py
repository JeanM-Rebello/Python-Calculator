from ValoresPosteriores import ValoresPosteriores
class Main(ValoresPosteriores):
    def __init__(self):
        super().__init__()

m = Main()
print("-----Calculadora Python-----")
m.comeco()
m.operations()
while True:
    if m.extraValue() == False:
        break
    else:
        m.extraValue()