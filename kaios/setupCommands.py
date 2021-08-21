import sys, os
from datetime import datetime
from sysFunctions import sysos, login, setup, userfuncs
from assets import sysAssets
from sysvars import sysVars
sysos = sysos()
login = login()
setup = setup()
userfuncs = userfuncs()
sysAssets = sysAssets()
sysVars = sysVars()


class setupPrg():
    def setuphalt(self):
        setup01 = False
        while setup.setcheck() == False:
            if not setup01:
                print(sysAssets.setup01)
                setup01 = True

            inp = input('sys/-$ ').lower().strip()

            if inp == 'help':
                print(sysAssets.help)

            elif inp == 'setupmen':
                setup01 = False

            elif inp == 'clear':
                os.system('clear')
                setup01 = False

            elif inp == 'setup':
                self.setup()

            else:
                print("'"+inp+"' is not recognized as a valid command or program, please check spelling and capitalisation and try again or run help")

    def setup(self):
        setup02 = False
        setup03 = False
        setup04 = False
        setup05 = False
        setup06 = False

        while setup.setcheck() == False:
            if not setup02:
                print(sysAssets.setup02)
                setup02 = True

            inp = input('sys/-$ ').lower().strip()
            if inp != '':
                sysVars.rusername = inp

            if not setup03:
                print(sysAssets.setup03)
                setup03 = True
            
            inp = input('sys/-$ ').lower().strip()
            if inp != '':
                sysVars.rpassword = inp

            if not setup04:
                print(sysAssets.setup04)
                setup04 = True
            sysVars.username = input('sys/-$ ').lower().strip()
            if not setup05:
                print(sysAssets.setup05)
                setup05 = True
            sysVars.password = input('sys/-$ ').lower().strip()
            if not setup06:
                print(sysAssets.setup06)
                setup06 = True
            inp = input('sys/-$ ').lower().strip()

            if inp == 'done':
                setup.setuproot(sysVars.rusername, sysVars.rpassword)
                setup.setupdusr(sysVars.username, sysVars.password)
                lines = 'True'
                with open('usr/local/setup.txt', 'w') as f:
                    f.writelines(lines)
            else:
                print("'"+inp+"' is not recognized as a valid command or program, please check spelling and capitalisation and try again or run help")

