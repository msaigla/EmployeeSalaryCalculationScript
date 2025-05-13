from abc import ABC, abstractmethod

class BaseReport(ABC):
    def __init__(self, employees):
        self.employees = employees

    @abstractmethod
    def generate(self):
        pass