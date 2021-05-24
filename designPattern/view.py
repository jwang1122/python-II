from model import Person

def showAllView(list):
    print ('In our db we have %i users. Here they are:' % len(list))
    for item in list:
        print (item.name())

def startView():
    print ('MVC - the simplest example')

def endView():
    print('Goodbye!')