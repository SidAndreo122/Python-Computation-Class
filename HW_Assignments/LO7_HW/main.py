from menu import *

mainMenu = Menu()

mainMenu.addOption("Check available memory")
mainMenu.addOption("View network connections")
mainMenu.addOption("Display free ram and swap")
mainMenu.addOption("Quit")

choice = mainMenu.getInput()
