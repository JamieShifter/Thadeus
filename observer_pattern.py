from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List

class Subject(ABC):

    @abstractmethod
    def attach(self, observer: Observer):
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        pass

class Observer(ABC):

    @abstractmethod
    def update(self, subject: Subject):
        pass


<<<<<<< HEAD
=======

# BELOW IS A CONCRETIZED EXAMPLE - DO NOT USE IN CODE!

>>>>>>> e4817f1ec2be1a4db4e7596c98d6fcf037e885d1
class ConcreteSubject(Subject):
    _state: int = None
    _observers: List[Observer] = []

    def attach(self, observer: Observer):
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self):
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self):
        print("\n Subject: I'm doing something important.")
        self._state = randrange(0, 10)
        print("Subject: My state has just changed to: {}".format(self._state))
        self.notify()


class ConcreteObserverA(Observer):
    def update(self, subject: Subject):
        if subject._state < 3:
            print("ConcreteObserverA: Reacted to event")


class ConcreteObserverB(Observer):
    def update(self, subject: Subject):
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserverB: Reacted to the event")


if __name__ == "__main__":
    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)

    subject.some_business_logic()