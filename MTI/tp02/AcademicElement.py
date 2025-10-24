from abc import ABC, abstractmethod

class AcademicElement(ABC):
    """Abstract base class for academic entities (Module, Unit, Semester, etc.)."""

    def __init__(self, name, title):
        self.name = name
        self.title = title
        self._WEEKS = 15  # Encapsulation: private attribute

        # Basic academic attributes
        self.coef = 0
        self.credit = 0

        # Workload distribution (volume horaire)
        self.hours_lecture = 0
        self.hours_td = 0
        self.hours_tp = 0

    @abstractmethod
    def calculate_average(self):
        """Abstract method to be implemented by subclasses."""
        pass

    @abstractmethod
    def calculate_credits(self):
        """Abstract method to be implemented by subclasses."""
        pass
