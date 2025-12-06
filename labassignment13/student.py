class Student:
    """A class to store student details and marks."""

    def __init__(self, name, age, marks):
        """
        Initialize a student with name, age, and a list of marks.
        marks: list like [m1, m2, m3]
        """
        self.name = name
        self.age = age
        self.marks = marks

    def details(self):
        """Print student details in a readable format."""
        print(f"Name: {self.name}, Age: {self.age}")

    def total(self):
        """Return total of all marks."""
        return sum(self.marks)
s = Student("Azra", 21, [90, 88, 95])
s.details()
print("Total marks:", s.total())
