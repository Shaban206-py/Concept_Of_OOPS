class Student:
    def __init__(self, name):
        self._name = name  # Using a protected attribute with a leading underscore
        print("Adding new Student")

    # Getter for name
    def get_name(self):
        return self._name

    # Setter for name with validation
    def _set_name(self, name):
        if isinstance(name, str) and name.strip():
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string.")


try:
    student = Student("Ali")
    print(f"Student Name: {student.get_name()}")  # Using the getter to access the name

    student.set_name("Sara")  # Using the setter to update the name
    print(f"Updated Student Name: {student.get_name()}")

    student.set_name("")  # This will raise a ValueError due to invalid name
except ValueError as e:
    print(e)
