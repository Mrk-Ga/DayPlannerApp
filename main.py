from kivy.config import Config

Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
from kivymd.app import MDApp
from screens.HomeScreen import HomeScreen

class PlannerApp(MDApp):
    def build(self):
        return HomeScreen()

if __name__ == "__main__":
    PlannerApp().run()