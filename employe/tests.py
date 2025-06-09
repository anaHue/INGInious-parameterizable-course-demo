import importlib.util
import sys
import unittest

class TestStudentCode(unittest.TestCase):
    def setUp(self):
        self.student_code_path = "/task/student/code.py"
        self.class_name = "Employe"

        # Dynamically load the student's code
        spec = importlib.util.spec_from_file_location("student_code", self.student_code_path)
        self.student_code = importlib.util.module_from_spec(spec)
        sys.modules["student_code"] = self.student_code
        spec.loader.exec_module(self.student_code)

    def test_class_exists(self):
        # Check if the class exists
        self.assertTrue(hasattr(self.student_code, self.class_name), 
                        f"Class '{self.class_name}' not found.")

    def test_constructor(self):
        # Check if the constructor accepts name and salary
        Employe = getattr(self.student_code, self.class_name)
        try:
            emp = Employe("John Doe", 50000)
        except TypeError:
            self.fail("Constructor for 'Employe' must accept 'name' and 'salary' as parameters.")

    def test_getters(self):
        # Check if getters for name and salary work
        Employe = getattr(self.student_code, self.class_name)
        emp = Employe("John Doe", 50000)
        self.assertTrue(hasattr(emp, "get_name"), "Getter method 'get_name' not found.")
        self.assertTrue(hasattr(emp, "get_salary"), "Getter method 'get_salary' not found.")
        self.assertEqual(emp.get_name(), "John Doe", "Getter for 'name' is not working correctly.")
        self.assertEqual(emp.get_salary(), 50000, "Getter for 'salary' is not working correctly.")

    def test_increase_salary(self):
        # Check if the increase_salary method works correctly
        Employe = getattr(self.student_code, self.class_name)
        emp = Employe("John Doe", 50000)
        self.assertTrue(hasattr(emp, "increase_salary"), 
                        "Method 'increase_salary' not found in class 'Employe'.")
        emp.increase_salary(10)  # Increase salary by 10%
        self.assertEqual(emp.get_salary(), 55000, 
                         "Method 'increase_salary' did not correctly update the salary.")

if __name__ == "__main__":
    unittest.main()