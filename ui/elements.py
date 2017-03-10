from Tkinter import *


class UiElement(object):
    pass


class Question(UiElement):
    pass


class CheckBoxQuestion(Question):
    def __init__(self, variable, label, value):
        self.label = label
        self.question = variable # should be set in a lookup table
        self.value = value
