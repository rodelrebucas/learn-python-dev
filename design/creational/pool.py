# Use a resource/object if it is already available in the pool - avoid unnecessary creation
# Get object/resource from a pool - Queue implemented
# Return back an object to the pool if it is not used


class ObjectPool(object):
    def __init__(self, queue, auto_get=False):
        print("__init__")

        self._queue = queue  # Queue
        # Get/Extract first item (FIFO)
        self.item = self._queue.get() if auto_get else None

    def __enter__(self):
        # processing here
        print("__enter__")
        if self.item is None:
            self.item = self._queue.get()
        return self.item

    def __exit__(self, Type, value, traceback):
        # Upon exit , put the item back to the queue
        # __exit__ is called when context manager WIth statement is *done
        print("__exit__")
        if self.item is not None:
            print("exiting...")
            self._queue.put(self.item)
            self.item = None

    # Garbage collection, called everytime
    def __del__(self):
        print("__del__")
        if self.item is not None:
            print("deleting...")
            # return back the item to the queue
            self._queue.put(self.item)
            self.item = None


def main():
    try:
        import queue
    except ImportError:  # python 2.x compatibility
        import Queue as queue

    sample_queue = queue.Queue()
    sample_queue.put("yam")  # push to queue

    # context manager - ObjectPool - use a resource
    # then relase after exit
    with ObjectPool(sample_queue) as obj:
        print("Inside with: {}".format(obj))
    print("Outside with: {}".format(sample_queue.get()))

    def test_object(queue):
        pool = ObjectPool(queue, True)
        print("Inside func: {}".format(pool.item))

    sample_queue.put("sam")
    test_object(sample_queue)
    print("Outside func: {}".format(sample_queue.get()))

    if not sample_queue.empty():
        print(sample_queue.get())


if __name__ == "__main__":
    main()

### OUTPUT ###
# Inside with: yam
# Outside with: yam
# Inside func: sam
# Outside func: sam
