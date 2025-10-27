class Pessoa:
    def __init__(self, nome, dinheiro):
        self.__nome = nome
        self.__dinheiro = dinheiro

    def getNome(self):
        return self.__nome

    def getDinheiro(self):
        return self.__dinheiro

    def pagar(self, valor):
        if valor > self.__dinheiro:
            pago = self.__dinheiro
            self.__dinheiro = 0
            return pago
        else:
            self.__dinheiro -= valor
            return valor

    def receber(self, valor):
        self.__dinheiro += valor

    def __str__(self):
        return f"{self.__nome}:{self.__dinheiro}"


class Moto:
    def __init__(self):
        self.__custo = 0
        self.__motorista = None
        self.__passageiro = None

    def show(self):
        driver = self.__motorista if self.__motorista else "None"
        passenger = self.__passageiro if self.__passageiro else "None"
        print(f"Cost: {self.__custo}, Driver: {driver}, Passenger: {passenger}")

    def setDriver(self, nome, dinheiro):
        self.__motorista = Pessoa(nome, dinheiro)

    def setPass(self, nome, dinheiro):
        self.__passageiro = Pessoa(nome, dinheiro)

    def drive(self, km):
        if self.__motorista is None or self.__passageiro is None:
            print("fail: cannot drive without driver and passenger")
            return
        self.__custo += km

    def leavePass(self):
        if self.__passageiro is None:
            print("fail: no passenger to leave")
            return

        valor_corrida = self.__custo
        pago = self.__passageiro.pagar(valor_corrida)

        if pago < valor_corrida:
            print("fail: Passenger does not have enough money")

        self.__motorista.receber(valor_corrida)
        print(f"{self.__passageiro.getNome()}:{self.__passageiro.getDinheiro()} left")

        self.__passageiro = None
        self.__custo = 0


def main():
    moto = Moto()
    while True:
        try:
            line = input()
        except EOFError:
            break
        if not line:
            continue

        # Sempre imprimir o comando lido
        print(line)

        if line.startswith("$end"):
            break

        parts = line.split()
        cmd = parts[0]

        if cmd == "$show":
            moto.show()
        elif cmd == "$setDriver":
            nome = parts[1]
            dinheiro = int(parts[2])
            moto.setDriver(nome, dinheiro)
        elif cmd == "$setPass":
            nome = parts[1]
            dinheiro = int(parts[2])
            moto.setPass(nome, dinheiro)
        elif cmd == "$drive":
            km = int(parts[1])
            moto.drive(km)
        elif cmd == "$leavePass":
            moto.leavePass()
        elif cmd.startswith("#"):
            # já foi impresso acima
            continue
        else:
            print("fail: comando inválido")


if __name__ == "__main__":
    main()
