from Tkinter import *


class UiElement(object):
    pass


class Question(UiElement):
    def __init__(self, variable, label):
        self.label = label
        self.variable = variable


class CheckBoxQuestion(Question):
    def __init__(self, variable, label):
        self.label = label
        self.variable = variable

class BooleanValue(object):
    def __init__(self, value):
         self.value = BooleanVar(value=value)

class BooleanQuestion(Question):
    def __init__(self, variable, label):
        self.label = label
        self.variable = variable
