from abc import ABC, abstractmethod

class Combiner(ABC):
    @abstractmethod
    def findOverlap(self):
        pass

    @abstractmethod
    def maskOverlap(self):
        pass

    @abstractmethod
    def averageOverlap(self):
        pass

    @abstractmethod
    def cutEnds():
        pass

    @abstractmethod
    def concat(self):
        pass
