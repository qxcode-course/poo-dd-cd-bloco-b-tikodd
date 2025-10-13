class Chinela:
    def __init__(self):    
        self.__tamanho = 0  

    def getTamanho(self):
        return self.__tamanho

    def setTamanho(self, valor: int):
        if 20 <= valor <= 50:
            self.__tamanho = valor
            print("Tamanho definido com sucesso!")
        else:
            print("Valor inválido! O tamanho deve estar entre 20 e 50.")

# loop principal
chinela = Chinela()

while chinela.getTamanho() == 0:
    print("Digite seu tamanho de chinela:")
    try:
        tamanho = int(input()) 
        chinela.setTamanho(tamanho)
    except ValueError:
        print("Por favor, digite apenas números inteiros.")

print("🎉 Parabéns, você comprou uma chinela tamanho", chinela.getTamanho())