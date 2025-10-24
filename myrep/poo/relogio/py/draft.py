class Watch:
    def __init__(self, hour: int = 0, minute: int = 0, seconds: int = 0):
        self.__hour = 0
        self.__minute = 0
        self.__seconds = 0

        self.setHour(hour)
        self.setMinute(minute)
        self.setSeconds(seconds)

    def __str__(self) -> str:
        hour = self.getHour()
        minute = self.getMinute()
        seconds = self.getSeconds()
        return f"{hour:02}:{minute:02}:{seconds:02}"

    def getHour(self) -> int:
        return self.__hour

    def getMinute(self) -> int:
        return self.__minute

    def getSeconds(self) -> int:
        return self.__seconds

    def setHour(self, value: int):
        if value < 0 or value > 23:
            print("fail: hora invalida")
            return

        self.__hour = value

    def setMinute(self, value: int):
        if value < 0 or value > 59:
            print("fail: minuto invalido")
            return
            
        self.__minute = value

    def setSeconds(self, value: int):
        if value < 0 or value > 59:
            print("fail: segundo invalido")
            return
            
        self.__seconds = value

    def nextSecond(self):
        self.__seconds += 1
        if self.__seconds > 59:
            self.__seconds = 0
            self.__minute += 1
            if self.__minute > 59:
                self.__minute = 0
                self.__hour += 1
                if self.__hour > 23:
                    self.__hour = 0

def main():
    watch = Watch()

    while True:
        line = input()
        args = line.split()
        print(f"${line}")

        match args[0]:
            case "show":
                print(watch)

            case "init":
                watch = Watch(int(args[1]), int(args[2]), int(args[3]))

            case "set":
                watch.setHour(int(args[1]))
                watch.setMinute(int(args[2]))
                watch.setSeconds(int(args[3]))

            case "next":
                watch.nextSecond()

            case "end":
                break

if __name__ == "__main__":
    main()
