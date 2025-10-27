class Person:
    def __init__(self, age: int = 0, name: str = ""):
        self.__age = age
        self.__name = name

    def __str__(self):
        return f"{self.__name}:{self.__age}"

    def getAge(self) -> int:
        return self.__age

    def getName(self) -> str:
        return self.__name

    def setAge(self, value: int):
        if value < 0:
            print("fail: idade invalida")
            return

        self.__age = value
    
    def setName(self, value: str):
        self.__name = value

class MotoCycle:
    def __init__(self, power: int = 1):
        self.__person: Person | None = None
        self.__power = power
        self.__time = 0

    def __str__(self):
        person = "empty" if self.__person is None else str(self.__person)
        return f"power:{self.__power}, time:{self.__time}, person:({person})"

    def getPerson(self) -> Person | None:
        return self.__person

    def getPower(self) -> int:
        return self.__power

    def getTime(self) -> int:
        return self.__time
    
    def setPerson(self, person: Person | None):
        self.__person = person

    def setPower(self, value: int):
        if value < 0:
            print("fail: potencia de motoca invalida")
            return
            
        self.__power = value

    def setTime(self, value: int):
        self.__time = value

    def inserir(self, pessoa: Person) -> bool:
        if self.getPerson() is not None:
            print("fail: busy motorcycle")
            return False

        self.setPerson(pessoa)
        return True

    def remover(self) -> Person | None:
        if self.getPerson() is None:
            print("fail: empty motorcycle")
            return None
            
        oldPessoa = self.getPerson()
        self.setPerson(None)
        return oldPessoa

    def buyTime(self, value: int) -> bool:
        if value < 0:
            print("fail: negative time")
            return False
        
        self.setTime(self.getTime() + value)
        return True

    def drive(self, time: int) -> bool:
        if time < 0:
            print("fail: negative time")
            return False

        if self.getTime() == 0:
            print("fail: buy time first")
            return False

        if self.getPerson() is None:
            print("fail: empty motorcycle")
            return False

        if self.getPerson().getAge() > 10:
            print("fail: too old to drive")
            return False

        if time > self.getTime():
            print(f"fail: time finished after {self.getTime()} minutes")
            self.setTime(0)
            return False
            return False
            
        self.setTime(self.getTime() - time)
        return True

    def honk(self):
        power = "e" * self.getPower()
        print(f"P{power}m")
def main():
    motorcycle = MotoCycle()

    while True:
        try:
            line = input()
            print(f"${line}")
            args = line.split()

            if not args:
                continue

            cmd = args[0]
            
            match cmd:
                case "show":
                    print(motorcycle)
                    
                case "init":
                    power = int(args[1])
                    motorcycle = MotoCycle(power=power)
                    
                case "enter":
                    name = args[1]
                    age = int(args[2])
                    person = Person(age=age, name=name)
                    motorcycle.inserir(person)
                    
                case "leave":
                    person = motorcycle.remover()
                    if person is not None:
                        print(person)
                    
                case "buy":
                    time = int(args[1])
                    motorcycle.buyTime(time)
                    
                case "drive":
                    time = int(args[1])
                    motorcycle.drive(time)
                    
                case "honk":
                    motorcycle.honk()
                    
                case "end":
                    break
                    
                case _:
                    print("fail: comando invalido")

        except EOFError:
            break
        except IndexError:
            print("fail: comando invalido")
        except ValueError:
            print("fail: parametro invalido")


if __name__ == "__main__":
    main()
