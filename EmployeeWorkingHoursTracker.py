"""Calculate total working hours for multiple employees."""


class Employee:
    """Represent an employee and their daily working hours."""

    def __init__(self, name, hours_worked_list):
        """Initialize employee name and daily working hours."""
        self.name = name
        self.hours_worked_list = hours_worked_list

    def get_total_hours(self):
        """Calculate and print the employee's total working hours."""
        total_hours = sum(self.hours_worked_list)
        print(f"{self.name} worked a total of {total_hours} hours.")


# Create four employee objects
employee1 = Employee("Asjad", [8, 7, 9, 8, 6])
employee2 = Employee("Rahim", [7, 8, 8, 9, 7])
employee3 = Employee("Karim", [8, 8, 8, 8, 8])
employee4 = Employee("Hasan", [6, 7, 8, 7, 9])


# Call the method for each employee
employee1.get_total_hours()
employee2.get_total_hours()
employee3.get_total_hours()
employee4.get_total_hours()