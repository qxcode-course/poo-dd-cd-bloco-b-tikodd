class Pessoa:
    def __init__(self, name: str, money: int):
        self.__name: str = name
        self.__money: int = money

    def getName(self) -> str:
        return self.__name
    
    def getMoney(self) -> int:
        return self.__money

    def setMoney(self, valor: int):
        self.__money = valor

    def pagar(self, valor: int):
        self.__money -= valor

    def receber(self, valor: int):
        self.__money += valor

    def __str__(self) -> str:
        return f"{self.getName()}:{self.getMoney()}"


class Moto:
    def __init__(self, custo: int):
        self.__custo: int = custo
        self.__motorista: Pessoa | None = None
        self.__passageiro: Pessoa | None = None

    def getCusto(self) -> int:
        return self.__custo
    
    def getDriver(self) -> Pessoa | None:
        return self.__motorista
    
    def setDriver(self, motorista: Pessoa):
        self.__motorista = motorista
    
    def getPass(self) -> Pessoa | None:
        return self.__passageiro
    
    def setPass(self, passageiro: Pessoa):
        self.__passageiro = passageiro

    def subir(self, passageiro: Pessoa):
        if self.__motorista is None:
            print("fail: moto sem motorista")
            return
        if self.__passageiro is not None:
            print("fail: moto ja tem passageiro")
            return
        self.__passageiro = passageiro

    def descer(self):
        if self.__passageiro is None:
            print("fail: moto sem passageiro")
            return

        if self.getPass().getMoney() < self.getCusto():
            print("fail: Passenger does not have enough money")
            self.getDriver().receber(self.getCusto())
            self.getPass().setMoney(0)
        else:
            self.getPass().pagar(self.getCusto())
            self.getDriver().receber(self.getCusto())

        print(f"{self.getPass()} left")
        self.__passageiro = None
        self.__custo = 0

    def dirigir(self, km: int):
        if self.__motorista is None:
            print("fail: moto sem motorista")
            return
        if self.__passageiro is None:
            print("fail: moto sem passageiro")
            return
        self.__custo += km

    def __str__(self) -> str:
        return f"Cost: {self.__custo}, Driver: {self.__motorista}, Passenger: {self.__passageiro}"


def main():
    moto = Moto(0)
    while True:
        line = input()
        print("$" + line)
        args = line.split()
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(moto)
        elif args[0] == "setDriver":
            name = args[1]
            money = int(args[2])
            motorista = Pessoa(name, money)
            moto.setDriver(motorista)
        elif args[0] == "setPass":
            name = args[1]
            money = int(args[2])
            passageiro = Pessoa(name, money)
            moto.setPass(passageiro)
        elif args[0] == "drive":
            km = int(args[1])
            moto.dirigir(km)
        elif args[0] == "leavePass":
            moto.descer()
        else:
            print("fail: comando inválido")


main()
