
from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
from datetime import datetime
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.config import Config

class PlannerScreen(MDScreen):
    pass

class PlannerApp(MDApp):
    def build(self):
        return PlannerScreen()

    def on_start(self):
        self.set_accuall_date()
        sample_tasks = ["Zadanie 1", "Spotkanie o 13:00", "Wysłać raport", "Zakupy"]
        for task in sample_tasks:
            self.add_task_to_list(task)

    def add_task(self):
        self.add_task_to_list("Nowe zadanie")

    def add_task_to_list(self, task_text):
        from kivymd.uix.list import OneLineListItem
        self.root.ids.task_list.add_widget(
            OneLineListItem(text=task_text)
        )

    def set_accuall_date(self):
        dzis = datetime.now().strftime("%Y-%m-%d")
        self.root.ids.header.title = f"Dziś: {dzis}"

if __name__ == "__main__":
    PlannerApp().run()