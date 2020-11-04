class FA:
    def __init__(self):
        self.__states=[]
        self.__alphabet=[]
        self.__initial = []
        self.__final = []
        self.__fa =[]
        self.readFromFile()

    def readFromFile(self):
        filename = "fa.txt"
        f = open(filename,"r")

        self.__states = f.readline().split(" ")
        self.__states[-1] = self.__states[-1].strip("\n")

        self.__alphabet = f.readline().split(" ")
        self.__alphabet[-1] = self.__alphabet[-1].strip("\n")

        self.__initial = f.readline().split(" ")
        self.__initial[-1] = self.__initial[-1].strip("\n")

        self.__final = (f.readline().split(" "))
        self.__final[-1] = self.__final[-1].strip("\n")

        for line in f:
            self.__fa.append(line[:-1].split(" "))

    def printMeniu(self):
        print()
        print("1 - Display states")
        print("2 - Display the alphabet")
        print("3 - Display transitions")
        print("4 - Display initial states")
        print("5 - Display final states")
        print("0 - Quit")
        print()


    def displayStates(self):
        print("\nStates:")
        for state in self.__states:
            print(state)

    def displayAlphabet(self):
        print("\nThe aplhabet:")
        for a in self.__alphabet:
            print(a)

    def displayTransitions(self):
        print("\nTransitions:\n")
        for el in self.__fa:
            print(el[0] + "->" + el[1] + ": " + el[2])

    def displayInititalSt(self):
        print("\nInitial states:\n")
        for f in self.__initial:
            print(f)

    def displayFinalSt(self):
        print("\nFinal states:\n")
        for f in self.__final:
            print(f)

    def start(self):
        com = -1
        while com != "0":
            self.printMeniu()
            com = input("\tEnter your command: ")
            if com == "1":
                self.displayStates()
            elif com == "2":
                self.displayAlphabet()
            elif com == "3":
                self.displayTransitions()
            elif com  == "4":
                self.displayInititalSt()
            elif com == "5":
                self.displayFinalSt()
            elif com == "0":
                print("\nGoodbye! :)")
            else:
                print("\nUnknown command")

fa = FA()
fa.start()
