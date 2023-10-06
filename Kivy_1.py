import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp

class TextApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        input_label = Label(text='Ingrese el texto:')
        text_input = TextInput(font_size=20, size_hint=(1, None), height=100)

        output_label = Label(font_size=20, size_hint=(1, None), height=300, valign='top', markup=True)
        output_label.bind(size=output_label.setter('text_size'))

        apply_button = Button(text='Aplicar Cambios', size_hint=(None, None), size=(200, 50))

        def apply_changes(instance):
            input_text = text_input.text
            output_label.text = input_text

        apply_button.bind(on_release=apply_changes)

        layout.add_widget(input_label)
        layout.add_widget(text_input)
        layout.add_widget(apply_button)
        layout.add_widget(output_label)

        return layout

if __name__ == '__main__':
    TextApp().run()