from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button 

from kivy.uix.screenmanager import Screen ,ScreenManager


from kivy.lang import Builder
from kivy.core.window import Window




Builder.load_file('app.kv')
Window.size=(500 ,400 )
class Home(Screen):
    pass

class WinLogin(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        
        self.UserName=Label(text="username : ",pos_hint={'right':.6,'center_y':.9})
        self.password=Label(text="password : ",pos_hint={'right':.6,'center_y':.7})

        self.username_input=TextInput(pos_hint={'right':0.5,'center_y':.9},size_hint=(.3,.1),multiline=False)
        print(self.username_input.text)
        self.password_input=TextInput(pos_hint={'right':0.5,'center_y':.7},size_hint=(.3,.1),multiline=False,password=True)

        self.btn_send=Button(text ='send',pos_hint={'right':0.5,'center_y':.5},size_hint=(.3,.1))
        self.add_widget(self.password)
        self.add_widget(self.UserName)
        self.add_widget(self.username_input)
        self.add_widget(self.password_input)
        self.add_widget(self.btn_send)

        self.btn_send.bind(on_press =self.callback)

    def callback(self,event):
        username=""
        password=""
        if self.username_input.text != username or self.password_input.text != password :
            print(f"{self.username_input.text} not found ")

        else:
            print("wellcome to page ")
            self.newwin()

    def newwin(self):
        sm=ScreenManager()
        sm.add_widget(Home(name='home'))
        return sm
        
        
        
           
        

class MyApp(App):
    def build(self):
        sm=ScreenManager()
        sm.add_widget(WinLogin(name='Login'))
        sm.add_widget(Home(name='home'))

        return sm
      
        
        
    
    



if __name__ == "__main__":
    MyApp().run()





