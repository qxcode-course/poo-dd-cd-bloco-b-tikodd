class Lead:
    def __init__(self, thickness: float, hardness: str, size: int):
        self.thickness = thickness
        self.hardness = hardness
        self.size = size

    def __str__(self):
        return f"[{self.thickness}:{self.hardness}:{self.size}]"


class Pencil:
    def __init__(self, thickness: float):
        self.thickness = thickness
        self.tip = None

    def insert(self, lead: Lead):
        if self.tip is not None:
            print("fail: ja existe grafite")
            return
        if lead.thickness != self.thickness:
            print("fail: calibre incompativel")
            return
        self.tip = lead

    def remove(self):
        self.tip = None

    def write(self):
        if self.tip is None:
            print("fail: nao existe grafite")
            return
        
        if self.tip.size <= 10:
            print("fail: tamanho insuficiente")
            return
        
        # Define o gasto baseado na dureza
        gasto = 0
        if self.tip.hardness == "HB":
            gasto = 1
        elif self.tip.hardness == "2B":
            gasto = 2
        elif self.tip.hardness == "4B":
            gasto = 4
        elif self.tip.hardness == "6B":
            gasto = 6
        
        # Verifica se após escrever ficaria abaixo de 10
        if self.tip.size - gasto < 10:
            print("fail: folha incompleta")
            self.tip.size = 10
            return
        
        self.tip.size -= gasto

    def __str__(self):
        tip_str = self.tip if self.tip else "null"
        return f"calibre: {self.thickness}, grafite: {tip_str}"


pencil = None

while True:
    line = input()
    print(f"${line}")
    args = line.split()
    
    if args[0] == "end":
        break
    elif args[0] == "show":
        print(pencil)
    elif args[0] == "init":
        pencil = Pencil(float(args[1]))
    elif args[0] == "insert":
        lead = Lead(float(args[1]), args[2], int(args[3]))
        pencil.insert(lead)
    elif args[0] == "remove":
        pencil.remove()
    elif args[0] == "write":
        pencil.write()            


