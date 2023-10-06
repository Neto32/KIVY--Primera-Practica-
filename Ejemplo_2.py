import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage

class CarruselApp(App):
    def build(self):
        # Crear un carrusel
        carrusel = Carousel(direction='right')
 
        # Agregar imágenes al carrusel
        for i in range(1, 4):  # Asumiendo que las imágenes se llaman 1.jpg, 2.jpg, 3.jpg
            src = f"{i}.jpg"
            imagen = AsyncImage(source=src, allow_stretch=True)
            carrusel.add_widget(imagen)

        return carrusel

if __name__ == '__main__':
    CarruselApp().run()