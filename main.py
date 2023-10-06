import kivy
from kivy.app import App
kivy.require('1.9.0')
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder

class AppEjemplo(App):
    def build(self):
        # Creamos un BoxLayout vertical como raíz de la aplicación
        bl = BoxLayout(orientation='vertical')
        
        # Creamos un campo de entrada de texto (TextInput)
        ti = TextInput(font_size=35, height=100)
        
        # Creamos un FloatLayout para contener la etiqueta y el botón
        fl = FloatLayout()
        
        # Creamos una etiqueta (Label) inicial con un texto predefinido
        l = Label(text="El jorge me la pela", font_size=50, size_hint=(None, None), size=(500, 200), text_size=(500, None))
        
        # Configuramos el tamaño y posición del FloatLayout
        fl.size_hint = (None, None)
        fl.size = l.size
        fl.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        
        # Agregamos la etiqueta al FloatLayout
        fl.add_widget(l)
        
        # Creamos un botón con el texto "Actualizar Texto"
        button = Button(text="Actualizar Texto")
        
        # Configuramos el tamaño y posición del botón
        button.size_hint = (None, None)
        button.size = (200, 50)
        button.pos_hint = {"center_x": 0.5}
        
        # Vinculamos el evento on_release del botón para actualizar el texto de la etiqueta
        button.bind(on_release=lambda instance: self.update_label_text(l, ti.text))
        
        # Agregamos el campo de entrada, el FloatLayout y el botón al BoxLayout
        bl.add_widget(ti)
        bl.add_widget(fl)
        bl.add_widget(button)

        return bl

    # Función para actualizar el texto de la etiqueta con el texto del campo de entrada
    def update_label_text(self, label, new_text):
        label.text = new_text

if __name__ == '__main__':
    AppEjemplo().run()
