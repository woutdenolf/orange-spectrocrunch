from AnyQt import QtWidgets
from Orange.widgets.utils import getdeepattr
from Orange.widgets.settings import Setting
import numbers


class SettingForm(QtWidgets.QWidget):

    def __init__(self, parent=None, margin=0, spacing=-100):
        super(SettingForm, self).__init__(parent)
        layout = QtWidgets.QFormLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(spacing)
        self.layout = layout

    def sizeHint(self):
        width, height = super(SettingForm, self).sizeHint()
        return QtWidgets.QSize(int(1.8 * width), height)

    def addSetting(self, owner, name, label=None):
        """
        :param owner: setting owner
        :type owner: OWWidget or OWComponent
        :param name: setting name
        :type name: str
        :param label: setting label
        :type label: str or None
        """
        # Label
        if label is None:
            label = '{}:'.format(name)
        # Field
        value = getdeepattr(owner, name)
        if isinstance(value, str):
            field = QtWidgets.QLineEdit()
            field.setText(value)
        elif isinstance(value, numbers.Number):
            if isinstance(value, numbers.Integral):
                field = QtWidgets.QSpinBox()
            else:
                field = QtWidgets.QDoubleSpinBox()
            field.setValue(value)
        else:
            raise ValueError('{} does not have a Qt widget'
                             .format(repr(type(value).__qualname__)))
        # Append
        self.layout.addRow(label, field)
