from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFlatButton

from database import models
from screens.TaskGUI import TaskBox


class AddTaskDialog:
    def __init__(self, parent_screen):
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
        if text:

            self.parent_screen.ids.task_list.add_widget(
                TaskBox(text=text)
            )
        self.dialog.dismiss()
        self.text_field.text = ""
        task = models.Task(name = text, date=self.parent_screen.acc_date)
        models.add_task_to_db(task)