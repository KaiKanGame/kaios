import sys, os
from datetime import datetime
from sysvars import sysVars

sysVars = sysVars()

class sysos():

    def __init__(self, **kwargs):
        self.setuptst = open('usr/local/setup.txt')
        self.setup = self.setuptst 
        self.power = True
        self.now = datetime.now()
        self.dt_string = self.now.strftime("%d/%m/%Y %H:%M:%S")

        setup().setuproot('root','toor')


    def powerbtn(self):
        if self.power:
            self.power = False

        else:
            self.power = True
  
 
    def checkperms(self, username):
        self.chkusr = open('usr/',username,'/perms.txt')
        self.usr = self.chkusr.read()
        if self.usr == 'root':
            return True

    def oprint(self, text):
        self.printed = False
        if not self.printed:
            print(text)
            self.printed = True
        else:
            pass


class login():

    def loginstr(self):
        pr = False
        prr = False
        prrr = False
        while True:
            if not pr:
                print('Please enter your Username:')
                pr = True
            sysVars.username = input('sys/-$ ').lower().strip()
            if not prr:
                print('Please enter your Password:')
                sysos.workingusr = sysVars.username
                prr = True
            sysVars.password = input('sys/-$ ').lower().strip()
            if not prrr:
                print('type login to login')
                prrr = True
            inp = input('sys/-$ ').lower().strip()
            if inp == 'login':
                if self.login(sysVars.username, sysVars.password):
                    break
                else:
                    pass
            else:
                print("'"+inp+"' is not recognized as a valid command or program, please check spelling and capitalisation and try again or run help")
        return True
                


    def login(self, username, password):
        self.logpas = open('usr/'+username+'/pass.txt')
        self.logusr = open('usr/'+username+'/usr.txt')
        self.lpass = self.logpas.read()
        self.lusr = self.logusr.read()
        while True:
            if password == self.lpass:
                return True
            else:
                print('incorrect password or username, or both, please try again...')

    def sudo(self, rusername, rpassword):
        self.logpas = open('usr/'+rusername+'/pass.txt')
        self.logusr = open('usr/'+rusername+'/usr.txt')
        self.lpass = self.logpas.read()
        self.lusr = self.logusr.read()
        while True:
            if rpassword == self.lpass:
                return True
            else:
                print('incorrect pausr/ssword, please try again...')

   
class setup():

    def setcheck(self):
        self.setupCheck = open('usr/local/setup.txt')
        self.setChk = self.setupCheck.read()
        if self.setChk == 'True':
            return True
        else:
            return False


    def setuproot(self, rusername, rpassword):
        self.lines = [rusername]
        self.dirusr = './usr/'+rusername+'/'
        if not os.path.exists(self.dirusr):
            os.mkdir(self.dirusr)
        with open('./usr/'+rusername+'/rusr.txt', 'w') as f:
            f.writelines(self.lines)

        self.lines02 = 'root'
        with open('usr/'+rusername+'/perms.txt', 'w') as f:
            f.writelines(self.lines)

        self.lines4 = [rpassword]
        with open('usr/'+rusername+'/rpass.txt','w') as f:
            f.writelines(self.lines4)


    def setupdusr(self, username, password):
        self.dirusr = './usr/'+username+'/'
        if not os.path.exists(self.dirusr):
            os.mkdir(self.dirusr)
        self.lines = [username]
        with open('usr/'+username+'/usr.txt', 'w') as f:
            f.writelines(self.lines)

        self.lines02 = 'default'
        with open('usr/'+username+'/perms.txt', 'w') as f:
            f.writelines(self.lines)

        self.lines4 = [password]
        with open('usr/'+username+'/pass.txt','w') as f:
            f.writelines(self.lines4)   

class userfuncs():

    def __init__(self, **kwargs):
        self.null = 'null'

    
    def addusr(self, **kwargs):
        pass
        



# datetime object containing current date and time
#sysos.power
#print("now =", sysos.now)
# dd/mm/YY H:M:S
#print("date and time =", sysos.dt_string)
