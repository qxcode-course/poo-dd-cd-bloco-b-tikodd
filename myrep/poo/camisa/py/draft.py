class Camisa:
    def __init__(self):
        self.__tamanho = ""

    def getTamanho(self) -> str:
        return self.__tamanho

    def setTamanho(self, valor: str):
        tamanhosValidos = ["PP", "P", "M", "G", "GG", "XG"]
        if valor not in tamanhosValidos:
            print("erro: tamanho inválido")
            return

        self.__tamanho = valor


if __name__ == "__main__":
    camisa = Camisa()

    while camisa.getTamanho() == "":
        camisa.setTamanho(input("Tamanho da camisa:\n").upper())
        
    print(f"Sua camisa tem tamanho {camisa.getTamanho()}")






    

