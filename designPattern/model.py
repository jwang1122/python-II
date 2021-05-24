import json

class Person(object):
    def __init__(self, first_name = None, last_name = None):
        self.first_name = first_name
        self.last_name = last_name

    #returns Person name, ex: John Doe
    def name(self):
        return ("%s %s" % (self.first_name,self.last_name))
        
    @classmethod
    #returns all people inside db.txt as list of Person objects
    def getAll(self):
        result = []
        with open('db.json') as f:
            students = json.load(f)
        for item in students:
            person = Person(item['first_name'], item['last_name'])
            result.append(person)
        return result