# from
class Manager(Employee):
    def __init__(self, name, id, grade):
        # fields from superclass
        self.name = name
        self.id = id

        self.grade = grade

    # ...


# to
class Manager(Employee):
    def __init__(self, name, id, grade):
        super().__init__(name, id)  # with superclass
        self.grade = grade

    # ...
