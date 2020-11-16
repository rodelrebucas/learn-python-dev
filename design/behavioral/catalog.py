# Executes a  class's method based on a value


class Catalog(object):
    def __init__(self, param):
        self.param = param
        self._static_method_choices = {
            "option_one": self._option_one,
            "option_two": self._option_two,
        }
        # do param validations

    @staticmethod
    def _option_one():
        print("one")

    @staticmethod
    def _option_two():
        print("two")

    def main_method(self):
        self._static_method_choices[self.param]()


test = Catalog("option_two")
test.main_method()
