"""
Factory pattern:
1. get class name string
2. use the name to generate instance of the class (globals()[<class name string>])
"""
class Button(object):
   html = ""
   def get_html(self):
      return self.html

class Image(Button):
   html = '<img src=""></img>'

class Input(Button):
   html = '<input type="text">User Name</input>'

class Flash(Button):
   html = "<obj></obj>"

class ButtonFactory():
   def create_button(self, typ):
      targetclass = typ.capitalize()
      return globals()[targetclass]()

if __name__ == '__main__':    
    button_obj = ButtonFactory()

    x = button_obj.create_button("Input")
    print(type(x))
    print(x.get_html())

    button = ['image', 'input', 'flash'] # use name to create instance of the class
    for b in button:
        print (button_obj.create_button(b).get_html())

