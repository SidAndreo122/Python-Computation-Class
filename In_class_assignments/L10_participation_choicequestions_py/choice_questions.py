class Menu:
    ## Constructs a menu with no options.
    #
    def __init__(self):
        self._options = []

    ## Adds an option to the end of menu.
    #  @param option the option to add
    #
    def addOption(self, option):
        self._options.append(option)

    ## Displays the menu, with options numbered starting with 1, and prompts
    #  the user for input. Repeats until a valid input is supplied.
    #  @return the number that the user supplied
    #
    def getInput(self):
        done = False
        while not done:
            print('-' * 80, '\n')
            for i in range(len(self._options)):
                print("%d %s" % (i + 1, self._options[i]))

            userChoice = int(input())
            #if userChoice >= 1 and userChoice < len(self._options):
            if userChoice < 1 or userChoice > len(self._options):
                print('Enter a 1-4 only')
                continue
            #place holder
                    
            else:
                done = True
                quit()

        return userChoice

def main():
    mainMenu = Menu()

    def buildOptions():
        mainMenu.addOption("What is the * operator called in python? ")
        mainMenu.addOption("What is it called when you get a value from a pointer (*Ptr)? ")
        mainMenu.addOption("What is the multiplcation operator in python? ")

    buildOptions()
    choice = mainMenu.getInput()

if __name__ == '__main__':
    main()
