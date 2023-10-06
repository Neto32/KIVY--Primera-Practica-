from kivy.app import App
from kivy.uix.boxlayout import  BoxLayout
from kivy.uix.button import Button

class LayoutEj(App):
    def build(self):
        Padre=BoxLayout(orientation='vertical')

        horizontal=BoxLayout(orientation='horizontal')
        btn1=Button(text='Boton 1')
        btn2=Button(text='Boton 2')
        horizontal.add_widget(btn1)
        horizontal.add_widget(btn2)

        vertical=BoxLayout(orientation='vertical')
        btn3=Button(text='Boton 3')
        btn4=Button(text='Boton 4')
        vertical.add_widget(btn3)
        vertical.add_widget(btn4)

        Padre.add_widget(horizontal)
        Padre.add_widget(vertical)

        return Padre
    
if __name__ == '__main__':
    LayoutEj().run()