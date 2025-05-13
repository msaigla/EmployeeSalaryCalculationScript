from abc import ABC, abstractmethod
from typing import Dict, Union, List

Employee = Dict[str, Union[str, int]]

class BaseReport(ABC):
    def __init__(self, employees: List[Employee]) -> None:
        self.employees = employees

    @abstractmethod
    def generate(self) -> str:
        pass