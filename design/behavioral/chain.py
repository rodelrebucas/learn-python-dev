# A pattern that decouples and hides a sender to its receivers, a sender may not
# know about the receiver. There can be multiple receivers a sender that
# doesn't need to know , as long a the message is passed to the appropriate reciever

from contextlib import contextmanager
import os
import sys
import time
import abc


class AbstractHandler(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, successor=None):
        # Accepts a successor of type AbstractHandler
        self._successor = successor

    def handle(self, request):
        res = self._handle(request)
        # Handlers return true
        # if the request is handled
        # otherwise pass the request to the next handler/succesor
        if not res:
            self._successor.handle(request)

    @abc.abstractmethod
    def _handle(self, request):
        raise NotImplementedError("Must provide implementation in subclass.")


class ConcreteHandler1(AbstractHandler):
    def _handle(self, request):
        if 0 < request <= 10:
            print("request {} handled in handler 1".format(request))
            return True


class ConcreteHandler2(AbstractHandler):
    def _handle(self, request):
        if 10 < request <= 20:
            print("request {} handled in handler 2".format(request))
            return True


class ConcreteHandler3(AbstractHandler):
    def _handle(self, request):
        if 20 < request <= 30:
            print("request {} handled in handler 3".format(request))
            return True


class DefaultHandler(AbstractHandler):
    def _handle(self, request):
        print("end of chain, no handler for {}".format(request))
        return True


class Client(object):
    def __init__(self):
        # Initialize handler and its successor
        # handler(successor)
        self.handler = ConcreteHandler1(
            ConcreteHandler3(ConcreteHandler2(DefaultHandler()))
        )

    # Process an array of request
    def delegate(self, requests):
        for request in requests:
            self.handler.handle(request)


## Coroutine decorator
## For nesting coroutine
def coroutine(func):
    def start(*args, **kwargs):
        # func gives back a generator
        cr = func(*args, **kwargs)
        # kick start the generator
        # until yield is detected
        next(cr)
        return cr

    return start


@coroutine
# target is another generator function
def coroutine1(target):
    print("Cr 1")
    while True:
        # request = yield
        # 1. pass back to the caller
        # 2. accepts a request through send()
        request = yield
        if 0 < request <= 10:
            print("request {} handled in coroutine 1".format(request))
        else:
            # kick start the request = yield
            # of the target which is a generator
            target.send(request)


@coroutine
def coroutine2(target):
    print("Cr 2")
    while True:
        request = yield
        if 10 < request <= 20:
            print("request {} handled in coroutine 2".format(request))
        else:
            target.send(request)


@coroutine
def coroutine3(target):
    print("Cr 3")
    while True:
        request = yield
        if 20 < request <= 30:
            print("request {} handled in coroutine 3".format(request))
        else:
            target.send(request)


@coroutine
def default_coroutine():
    print("Cr default")
    while True:
        request = yield
        print("end of chain, no coroutine for {}".format(request))


class ClientCoroutine:
    def __init__(self):
        # Setup all generators in place
        # ready for kick start once
        # send() is called
        self.target = coroutine1(coroutine3(coroutine2(default_coroutine())))
        # Chained generator functions

    def delegate(self, requests):
        for request in requests:
            self.target.send(request)


def timeit(func):
    def count(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        count._time = time.time() - start
        return res

    return count


@contextmanager
def suppress_stdout():
    try:
        stdout, sys.stdout = sys.stdout, open(os.devnull, "w")
        yield
    finally:
        sys.stdout = stdout


if __name__ == "__main__":
    requests = [2, 5, 14, 22, 18, 3, 35, 27, 20]

    print("***Chained method calls***")
    client1 = Client()
    client1.delegate(requests)

    print("***Chained  function generators***")
    client2 = ClientCoroutine()
    client2.delegate(requests)

    requests *= 10000
    client1_delegate = timeit(client1.delegate)
    client2_delegate = timeit(client2.delegate)
    with suppress_stdout():
        client1_delegate(requests)
        client2_delegate(requests)
    # lets check which is faster
    print(
        "Chained method calls: ",
        client1_delegate._time,
        "| Chained function generators: ",
        client2_delegate._time,
    )

### OUTPUT ###
# request 2 handled in handler 1
# request 5 handled in handler 1
# request 14 handled in handler 2
# request 22 handled in handler 3
# request 18 handled in handler 2
# request 3 handled in handler 1
# end of chain, no handler for 35
# request 27 handled in handler 3
# request 20 handled in handler 2
# ------------------------------
# request 2 handled in coroutine 1
# request 5 handled in coroutine 1
# request 14 handled in coroutine 2
# request 22 handled in coroutine 3
# request 18 handled in coroutine 2
# request 3 handled in coroutine 1
# end of chain, no coroutine for 35
# request 27 handled in coroutine 3
# request 20 handled in coroutine 2
# Chained method calls:  0.2605576515197754 | Chained function generators:  0.18678641319274902
