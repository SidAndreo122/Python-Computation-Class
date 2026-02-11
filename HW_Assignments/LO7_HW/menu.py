from run_bash_cmd_function import run_bash_cmd

class Menu():
    def __init__(self):
        """
        Constructs an empty menu for each instance that has no options.
        """
        self._options = []


    def addOption(self, option):
        """
        Adds an options to the end of an menu instance.
        
        :param option: the menu option to add
        """
        self._options.append(option)


    def getInput(self):
        """
        Displays the numbered menu system, as well as takes input from the user.
        This will repeat until the user quits.

        :return userChoice: the number that the user choose from the menu
        """
        userChoice = 0
        
        while userChoice != 4:
            for index, option in enumerate(self._options, start=1):
                print(f"{index}. {option}")
        
            userChoice = int(input("Please enter a choice: "))

            match userChoice:
                case 1:
                    run_bash_cmd(userChoice)
                    
                case 2:
                    run_bash_cmd(userChoice)
                    
                case 3:
                    run_bash_cmd(userChoice)
                    
                case 4:
                    print('Quitting...')
                    break
                case _:
                    print(f"Invalid input. Please enter a value between 1 - {len(self._options)}.")
        return userChoice