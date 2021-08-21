import sys, os
from datetime import datetime
from sysFunctions import sysos, login, setup, userfuncs
from assets import sysAssets
from setupCommands import setupPrg
from sysvars import sysVars
from commands import cmds

sysos = sysos()
login = login()
setup = setup()
userfuncs = userfuncs()
sysAssets = sysAssets()
setupPrg = setupPrg()
sysVars = sysVars()
cmds = cmds()
cmds.clear()
while sysos.power == True:
    if not setup.setcheck():
        setupPrg.setuphalt()
    else:
        pass

    inp = input('sys/-$ ').lower().strip()

    if inp == 'login':
        if login.loginstr():
            while True:
                inp = input('usr/'+sysos.workingusr+'/-$ ').lower().strip()
                
                if inp == 'clear':
                    cmds.clear()
                
                elif inp == 'logout':
                    break

                elif inp == 'help':
                    print(sysAssets.help)

                else:
                    print("'"+inp+"' is not recognized as a valid command or program, please check spelling and capitalisation and try again or run help")
