from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class AbstractSubject(ABC):
    """
    The AbstractSubject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, Abstractobserver: AbstractObserver) -> None:
        """
        Attach an Abstractobserver to the subject.
        """
        pass

    @abstractmethod
    def detach(self, Abstractobserver: AbstractObserver) -> None:
        """
        Detach an Abstractobserver from the subject.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all Abstractobservers about an event.
        """
        pass


class Subject(AbstractSubject):
    """
    The AbstractSubject owns some important state and notifies Abstractobservers when the state
    changes.
    """

    _state: int = None
    """
    For the sake of simplicity, the AbstractSubject's state, essential to all
    subscribers, is stored in this variable.
    """

    observers: List[AbstractObserver] = []
    """
    List of subscribers. In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    """

    def attach(self, abstractobserver: AbstractObserver) -> None:
        print(f"AbstractSubject: Attached an Abstractobserver {abstractobserver}.")
        self.observers.append(abstractobserver)

    def detach(self, abstractobserver: AbstractObserver) -> None:
        self.observers.remove(abstractobserver)

    """
    The subscription management methods.
    """

    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """

        print("AbstractSubject: Notifying Abstractobservers...")
        for observer in self.observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        """
        Usually, the subscription logic is only a fraction of what a AbstractSubject can
        really do. Subjects commonly hold some important business logic, that
        triggers a notification method whenever something important is about to
        happen (or after it).
        """

        print("\nSubject: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"AbstractSubject: My state has just changed to: {self._state}")
        self.notify()


class AbstractObserver(ABC):
    def __init__(self, name):
        self.name = name
    def __repr__(self) -> str:
        return self.name
    """
    The AbstractObserver interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject: AbstractSubject) -> None:
        """
        Receive update from subject.
        """
        pass


"""
Concrete AbstractObservers react to the updates issued by the AbstractSubject they had been
attached to.
"""


class ObserverA(AbstractObserver):        
    def update(self, subject: AbstractSubject) -> None:
        print(f"{self}: Reacted to the event state: {subject._state}")


class ObserverB(AbstractObserver):
    def update(self, subject: AbstractSubject) -> None:
        if subject._state == 0 or subject._state >= 4:
            print(f"{self}: Reacted to the event state: {subject._state}")


if __name__ == "__main__":
    # The client code.

    subject = Subject()

    observer_a = ObserverA("Abstractobserver-A")
    subject.attach(observer_a)

    observer_b = ObserverB("Abstractobserver-B")
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)

    subject.some_business_logic()
