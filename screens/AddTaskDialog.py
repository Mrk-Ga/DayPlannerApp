from datetime import datetime, timedelta

from kivy.lang import Builder
from kivy.factory import Factory
from kivy.properties import partial
from kivy.uix.widget import Widget
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.dialog import MDDialog, MDDialogHeadlineText, MDDialogSupportingText, MDDialogButtonContainer, \
    MDDialogContentContainer
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField

from database import models
from screens import HomeScreen
from screens.TaskBox import TaskBox

class AddTaskContent(MDBoxLayout):

    def __init__(self, parentDialog, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parentDialog = parentDialog



Builder.load_file("kv/add_task_dialog.kv")

class AddTaskDialog:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.content = AddTaskContent(self)

        self.dates_to_add_tasks = [self.parent_screen.acc_date]



        #this must be declarated here in code, because .kv file couldn't handle it...
        self.textField = MDTextField(hint_text="dodaj zadanie")
        # Stwórz dialog, podając content i buttons jako sloty
        self.dialog = MDDialog(
            MDDialogHeadlineText(
                text="Dodaj zadanie",
                halign="left",
            ),
            MDDialogContentContainer(

                self.textField,
                MDButton(
                    MDButtonText(text="Dodaj\ncyklicznie" , pos_hint={"center_x":0.5}),
                    style="filled",
                    pos_hint={"center_y": 0.5},
                    on_release=self.add_weekly_task),
                spacing=15,
            ),
            MDDialogButtonContainer(
                Widget(),

                MDButton(
                    MDButtonText(text="Powrót"),
                    style="outlined",
                    on_release=self.close
                ),
                MDButton(
                    MDButtonText(text="Dodaj"),
                    style="outlined",
                    on_release=self.add_task
                ),
                spacing="8dp",
            ),
        )

    def open(self):
        self.dialog.open()

    def close(self, *args):
        self.dialog.dismiss()


    def add_task(self, *args):
        text = self.textField.text.strip()

        if text:
            for date in self.dates_to_add_tasks:
                task = models.Task(name=text, date=date)
                models.add_task_to_db(task)
                self.close()
                self.parent_screen.refresh_tasks()

    def add_weekly_task(self, *args):
        print("adding weekly task")
        dates = []
        date_obj = datetime.strptime(self.parent_screen.acc_date, "%Y-%m-%d").date()

        for weeks in range(0, 31, 7):
            new_date = date_obj + timedelta(days=weeks)
            new_date_str = new_date.strftime("%Y-%m-%d")
            dates.append(new_date_str)

        self.dates_to_add_tasks = dates
