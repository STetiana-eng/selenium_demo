from HW17.controls.base_control import BaseControl


class Button(BaseControl):
    def __init__(self, button_element):
        super().__init__(self, button_element)


    def click(self):
        self.element.click()

    def is_enabled(self):
        self.element.is_enabled()

