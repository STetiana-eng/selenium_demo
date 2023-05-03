from driver import Driver


class BasePage:
    def __init__(self):
        self._driver = Driver.get_ChromiumEdge_driver()