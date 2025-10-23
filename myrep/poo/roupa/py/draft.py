class Roupa:
    def __init__(self):
        self.__tamanho = ""

    def getTamanho(self) -> str:
        return self.__tamanho

    def setTamanho(self, valor: str):
        tamanhosValidos = ["PP", "P", "M", "G", "GG", "XG"]
        if valor not in tamanhosValidos:
            print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")
            return

        self.__tamanho = valor

roupa = Roupa()
while True:
    try:
        line = input()
    except EOFError:
        break

    if not line.strip():
        continue

    args: list[str] = line.split()
    print(f"${line}")

    cmd = args[0].lower()
    match cmd:
        case "show":
            print(f"size: ({roupa.getTamanho()})")

        case "size":
            if len(args) < 2:
                print("fail: informe o tamanho. Ex: size M")
                continue
            roupa.setTamanho(args[1].upper())

        case "end":
            break

        case _:
                print(f"size: {roupa.getTamanho()}")
            