# Subject - the one to be observed
# Observers - the one monitoring or observing the subject for changes


class Subject:
    def __init__(self):
        self.__observers = []

    def register(self, observer):
        self.__observers.append(observer)

    def notifyAll(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)


class Observer1:
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        pass


class Observer2:
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        pass


subject = Subject()
observer1 = Observer1(subject)
Observer2 = Observer2(subject)
subject.notifyAll("notification")
