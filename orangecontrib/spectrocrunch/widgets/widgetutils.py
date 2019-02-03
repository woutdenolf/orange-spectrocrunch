from AnyQt import QtWidgets, QtCore
from AnyQt.QtCore import Qt
from Orange.widgets.utils import getdeepattr
from Orange.widgets.settings import Setting
import numbers
import sys


class SettingForm(QtWidgets.QWidget):

    def __init__(self, parent=None, **kwargs):
        super().__init__(parent=parent)
        self.initUI(**kwargs)

    def initUIParent(self):
        parent = self.parent()
        if parent is None:
            return
        layout = parent.layout()
        if layout is None:
            layout = QtWidgets.QVBoxLayout()
            parent.setLayout(layout)
        layout.addWidget(self)

    def initUI(self, margin=0, spacing=4):
        self.initUIParent()
        layout = QtWidgets.QFormLayout()
        layout.setContentsMargins(margin, margin, margin, margin)
        layout.setSpacing(spacing)
        policy = QtWidgets.QFormLayout.AllNonFixedFieldsGrow
        layout.setFieldGrowthPolicy(policy)
        #layout.setFormAlignment(Qt.AlignHCenter | Qt.AlignTop)
        layout.setLabelAlignment(Qt.AlignLeft)
        self.setLayout(layout)

    #def sizeHint(self):
    #    s = super().sizeHint()
    #    return QtCore.QSize(int(1.5 * s.width()), s.height())

    def addSetting(self, owner, name, label=None, updateCallback=None):
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
            if updateCallback:
                field.textChanged.connect(updateCallback)
        elif isinstance(value, numbers.Number):
            if isinstance(value, numbers.Integral):
                field = QtWidgets.QSpinBox()
                ma = sys.maxsize
                field.setRange(-ma-1, ma)
            else:
                field = QtWidgets.QDoubleSpinBox()
            field.setValue(value)
            if updateCallback:
                field.valueChanged.connect(updateCallback)
        else:
            raise ValueError('{} does not have a Qt widget'
                             .format(repr(type(value).__qualname__)))
        # Append
        policy = QtWidgets.QSizePolicy.Expanding
        field.setSizePolicy(policy, policy)
        self.layout().addRow(label, field)
        return field
