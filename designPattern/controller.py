import view as view
from model import Person

def showAll():
    people_in_db = Person.getAll()
    view.showAllView(people_in_db)

def start():
    view.startView()
    a=input('Do you want to see everyone in my db?[y/n]')
    if a=='y':
        showAll()
    else:
        view.endView()

if __name__ == '__main__':
    start()