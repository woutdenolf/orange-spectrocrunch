from Orange.widgets.widget import OWWidget
from Orange.widgets.settings import Setting
from . import widgetutils
from Orange.widgets import gui

class Widget(OWWidget):
    # Widget needs a name, or it is considered an abstract widget
    # and not shown in the menu.
    name = 'Example'
    description = 'Description'
    icon = 'icons/example.svg'
    want_basic_layout = False

    number = Setting(42)
    string = Setting("test")

    def __init__(self):
        super().__init__()
        form = widgetutils.SettingForm(parent=self)
        self.stringWidget = form.addSetting(self, 'string', updateCallback=self.editString)
        self.numberWidget = form.addSetting(self, 'number', updateCallback=self.editNumber)

    def editString(self):
        print(self.stringWidget.text())

    def editNumber(self):
        print(self.numberWidget.value())
