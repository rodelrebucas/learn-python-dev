# Push Model = subject notifies the subscribers
# Pull Model =  observer gets update from subject
# Subject
class NewsPublisher:
    def __init__(self):
        self.__subscribers = []
        self.__latestNews = None

    # add an observer/subscriber
    def attach(self, subscriber):
        self.__subscribers.append(subscriber)

    def detach(self):
        return self.__subscribers.pop()

    def getAllsubscribers(self):
        pass

    def notifySubscribers(self):
        for sub in self.__subscribers:
            sub.update()

    def addNews(self, news):
        self.__latestNews = news

    def getNews(self):
        return "Got News: ", self.__latestNews


# abstract observer
class Subscriber(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        pass


# concrete observer
class SmsSubscriber:
    def __init__(self, publisher):
        # subscribe to an observer
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(self.publisher.getNews())


if __name__ == "__main__":
    news_publisher = NewsPublisher()
    subscriber = SmsSubscribe(news_publisher)

    news_publisher.addNews("News 1")
    news_publisher.notifySubscribers()
