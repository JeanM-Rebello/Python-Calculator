from Operacoes import Operacoes
class ValoresPosteriores(Operacoes):
    def __init__(self):
        super().__init__()
        
    def extravalueTradeOperation(self):
        print("Você deseja trocar a operacao?(S/N)")
        controlInput = input().lower()
        if controlInput=="s":
            self.operations()
        elif controlInput == "n":
            self.operationsMatch()
        else:
            print("Erro, entrada não valida.")
            self.extravalueTradeOperation()
            
    def extraValue(self):
        print("Você deseja adicionar algum outro valor?(S/N)")
        controlInput = input().lower()
        if controlInput=="s":
            print("Por favor insira o valor adicional desejado")
            self.values["Value 2"] = int(input())
            self.extravalueTradeOperation()
        elif controlInput == "n":
            return False
        else:
            print("Erro, entrada não valida.")
            self.extraValue()
