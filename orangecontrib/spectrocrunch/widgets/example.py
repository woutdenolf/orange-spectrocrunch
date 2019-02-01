from Orange.widgets.widget import OWWidget
from Orange.widgets.settings import Setting
from . import widgetutils

class Widget(OWWidget):
    # Widget needs a name, or it is considered an abstract widget
    # and not shown in the menu.
    name = 'Example'
    description = 'Description'
    icon = 'icons/example.svg'
    want_main_area = False

    number = Setting(42)
    string = Setting("test")

    def __init__(self):
        super().__init__()

        form = widgetutils.SettingForm(self.controlArea)
        form.addSetting(self, 'string')
        form.addSetting(self, 'number')

        #main_layout = QtGui.QVBoxLayout()
        #self.setLayout(main_layout)


        #layout = QtGui.QHBoxLayout()
        #label = QtGui.QLabel("Line:")
        #linedit = QtGui.QLineEdit()
        #horizontalLayout1.addWidget(treelist1)
        #horizontalLayout1.addWidget(treelist2)
        #horizontalLayout2.addWidget(label)
        #horizontalLayout2.addWidget(linedit)


        #label = QtGui.QLabel('Hello, World!')
        #self.controlArea.layout().addWidget(
        #    label, QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)

    def editString(self):
        print(self.stringWidget.value())

    def editNumber(self):
        print(self.numberWidget.value())