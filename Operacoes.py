from ValoresIniciais import ValoresInicais
class Operacoes(ValoresInicais):
    def __init__(self):
        self.operation = {}
        super().__init__()
        
    def operations(self):
        print("Qual Operação você deseja realizar?")
        print("As Operações disponiveis são:")  
        print("Soma(+)")
        print("Subtração(-)")
        print("Multiplicação(*)")
        print("Divisão(/)")
        print("Expoente(^)")
        print("Selecione a Operação por meio do simbolo:")
        self.operation["Operation"] = input()
        self.confirmOperation()
        
    def confirmOperation(self):
        print("Essa é a operação que você quer realizar?(S/N)", self.operation)
        controlInput = input().lower()
        if controlInput == "s":
            self.operationsMatch()
        elif controlInput == "n":
            self.operations()
        else:
            print("Erro, entrada não valida.")
            self.confirmOperation()
    
    def operationsMatch(self):
        result = None
        match self.operation["Operation"]:
                case "+":
                        result = self.values["Value 1"] + self.values["Value 2"]
                case "-":
                        result = self.values["Value 1"] - self.values["Value 2"]
                case "*":
                        result = (self.values["Value 1"])*(self.values["Value 2"])
                case "/":
                    if self.values["Value 2"] != 0:
                        result = (self.values["Value 1"])/(self.values["Value 2"])
                    else:
                        print("Divisões com zero não são possiveis.")
                case "^":
                        result = (self.values["Value 1"])**(self.values["Value 2"])
        if result != None:
            self.values["Value 1"] = result
            print("O resultado foi de",self.values["Value 1"] )
        else:
            print("Nenhuma operação foi realizada.")