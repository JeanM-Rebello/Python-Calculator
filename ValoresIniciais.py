class ValoresInicais():
    def __init__(self):
        self.values = {}
        
    def setValue1(self):
        print("Por Favor insira o Valor Desejado.")
        self.values["Value 1"] = int(input())
        
    def setValue2(self):
        print("Por Favor insira o próximo Valor Desejado.")
        self.values["Value 2"] = int(input())
        
    def getValue(self):
        print(self.values)
        
    def changeValueControl(self):
        print("Você quer alterar algum valor?(S/N)")
        controlInput = input().lower()
        if controlInput == "s":
            self.changeValue()
        elif controlInput == "n":
            pass
        else:
            print("Erro, entrada não valida.")
            self.changeValueControl()
            
    def changeValue(self):
        print("Qual valor você quer alterar? O primeiro valor (1) ou o segundo valor (2)")
        option = int(input())
        if option == 1:
            self.setValue1()
        elif option == 2:
            self.setValue2()
        else:
            print("Opção invalida, repita")
            self.changeValue()
            
    def comeco(self):
        self.setValue1()
        self.setValue2()
        self.changeValueControl()