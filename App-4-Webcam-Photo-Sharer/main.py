from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import wikipedia
import requests

Builder.load_file('frontend.kv')

class FirstScreen(Screen):
    def getImageLink(self):
        query = self.manager.current_screen.ids.user_query.text
        print("Searching for " + query + "...")

        #Get wikipedia page and download img
        page = wikipedia.page(query)
        imgLink = page.images[0]
        return imgLink

    def downloadImage(self):
        headers = {'User-agent': 'Mozilla/5.0'}
        response = requests.get(self.getImageLink(), headers=headers)

        #create img file
        imageName = 'files/image.jpg'
        with open(imageName, 'wb') as file:
            file.write(response.content)
        return imageName

    def setImage(self):
        #set image as response
        self.manager.current_screen.ids.img.source = self.downloadImage()

class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()