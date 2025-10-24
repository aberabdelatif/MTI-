class Module:
    """
    Represents a teaching module with pedagogical and evaluation attributes.
    """

    def __init__(
        self,
        name: str = "",  # module code
        title: str = "",
        coef: int = 1,
        credit: int = 1,
        hours_lecture: float = 1.5,
        hours_td: float = 0,
        hours_tp: float = 0,
        teaching_mode: str = "In-person",  # "Distance" or "In-person"
        continous_percent: int = 40,
        exam_percent: int = 60
    ):
        # Weeks in a semester
        self._WEEKS = 15

        # Basic attributes
        self.name = name
        self.title = title
        self.coef = coef
        self.credit = credit

        # Workload distribution (volume horaire)
        self.hours_lecture = hours_lecture
        self.hours_td = hours_td
        self.hours_tp = hours_tp

        # Teaching and evaluation mode
        self.teaching_mode = teaching_mode  # "Distance" or "In-person"
        self.evaluation_continous_percent = continous_percent
        self.evaluation_exam_percent = exam_percent

        # Total hours = hours per week × number of weeks
        self.total_hours = self._WEEKS * (self.hours_lecture + self.hours_td + self.hours_tp)

        # Encapsulated grades
        self._grades = {"tp": None, "td": None, "exam": None}

    # Encapsulation: controlled access to grades
    def set_grade(self, tp=None, td=None, exam=None):
        if tp is not None:
            self._grades["tp"] = tp
        if td is not None:
            self._grades["td"] = td
        if exam is not None:
            self._grades["exam"] = exam

    def summary(self):
        """Return a short textual description of the module."""
        return (
            f"Module: {self.title} ({self.name})\n"
            f"Coefficient: {self.coef}, Credits: {self.credit}\n"
            f"Hours: total {self.total_hours}, "
            f"{self.hours_lecture} Lecture, {self.hours_td} TD, {self.hours_tp} TP\n"
            f"Teaching mode: {self.teaching_mode}\n"
            f"Evaluation mode: Continuous: {self.evaluation_continous_percent}% | "
            f"Exam: {self.evaluation_exam_percent}%"
        )

    def calculate_average(self):
        """Should be implemented by subclasses."""
        pass


# Example usage
if __name__ == "__main__":
    mti = Module(
        name="MTI",
        title="Methods and Technologies of Implementation",
        coef=3,
        credit=5,
        hours_lecture=1.5,
        hours_tp=1.5,
        teaching_mode="In-person"
    )

    print(mti.summary())
