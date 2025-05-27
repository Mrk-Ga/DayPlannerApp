from kivy.factory import Factory
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFlatButton

from database import models
from screens.TaskBox import TaskBox
#Builder.load_file('kv/task_dialog.kv')

class AddTaskDialog:
    def __init__(self, parent_screen):
        super().__init__()
        self.parent_screen = parent_screen
        self.text_field = MDTextField(hint_text="Nazwa zadania", mode="rectangle")
        self.dialog = MDDialog(
            title="Dodaj zadanie",
            type="custom",
            content_cls=self.text_field,
            buttons=[
                MDFlatButton(text="Anuluj", on_release=self.close),
                MDFlatButton(text="Dodaj", on_release=self.add_task)
            ]
        )


    def open(self):
        self.dialog.open()

    def close(self, *args):
        self.dialog.dismiss()

    def add_task(self, *args):
        text = self.text_field.text.strip()
        task = models.Task(name = text, date=self.parent_screen.acc_date)
        models.add_task_to_db(task)
        self.parent_screen.refresh_tasks()
