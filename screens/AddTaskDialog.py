from kivy.factory import Factory
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFlatButton, MDIconButton

from database import models
from screens.TaskBox import TaskBox
#Builder.load_file('kv/task_dialog.kv')

class AddTaskDialog:
    def __init__(self, parent_screen):
        super().__init__()
        self.parent_screen = parent_screen
        self.text_field = MDTextField(hint_text="Nazwa zadania", mode="rectangle", text="")
        self.show_in_calendar_btn = MDFlatButton(text="Show calendar")
        box = MDBoxLayout(orientation="horizontal", spacing='10dp',padding=(20, 1, 20, 1))
        box.add_widget(self.text_field)
        box.add_widget(MDIconButton(icon="arrow-right",on_release=self.add_weekly_task))
        self.dialog = MDDialog(
            title="Dodaj zadanie",
            type="custom",
            content_cls = box,
            #content_cls=MDBoxLayout([self.text_field, self.show_in_calendar_btn], orientation="vertical"),
            buttons=[
                MDFlatButton(text="Anuluj", on_release=self.close),
                MDFlatButton(text="Dodaj", on_release=self.add_task)
            ]
        )


    def open(self):
        self.dialog.open()

    def close(self, *args):
        self.dialog.dismiss()

    def add_to_calendar(self):
        print("added to calendar")

    def add_weekly_task(self, *args):
        print("adding weekly task")

    def add_task(self, *args):
        text = self.text_field.text.strip()
        task = models.Task(name = text, date=self.parent_screen.acc_date)
        models.add_task_to_db(task)
        self.text_field.text=""
        self.close()
        self.parent_screen.refresh_tasks()
