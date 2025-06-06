from kivymd.uix.pickers import MDModalDatePicker
from kivymd.uix.screen import MDScreen
from database import crud
from screens.eventBus import EventBus


class DatePicker(MDScreen):

    def __init__(self, parentScreen, taskID, **kwargs): #inicializing calendar window to change task date
        super().__init__(**kwargs)
        date_dialog = MDModalDatePicker()
        date_dialog.bind(on_ok= self.update_task_date)
        date_dialog.bind(on_cancel= date_dialog.dismiss)
        date_dialog.open()
        self.taskID = taskID
        self.parentScreen = parentScreen

    def update_task_date(self, instance):   #updating task date, using db methods

        crud.update_task_date(self.taskID, instance.get_date()[0].strftime("%Y-%m-%d"))
        EventBus.emit("tasks_updated")
        instance.dismiss()





