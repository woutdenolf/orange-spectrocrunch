import unittest
from Orange.widgets.tests.base import WidgetTest
from orangecontrib.spectrocrunch.widgets.example import Widget as ExampleWidget


class TestExampleWidget(WidgetTest):

    def setUp(self):
        self.widget = self.create_widget(ExampleWidget)

    def test_addition(self):
        self.assertEqual(1 + 1, 2)
