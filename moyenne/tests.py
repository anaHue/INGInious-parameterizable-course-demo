import importlib.util
import sys
import io
import unittest

class TestStudentCode(unittest.TestCase):
    def setUp(self):
        self.student_code_path = "/task/student/code.py"
        self.method_name = "calculate_average"

        spec = importlib.util.spec_from_file_location("student_code", self.student_code_path)
        self.student_code = importlib.util.module_from_spec(spec)
        sys.modules["student_code"] = self.student_code
        spec.loader.exec_module(self.student_code)

    def test_method_simple(self):
        self.assertTrue(hasattr(self.student_code, self.method_name), 
                        f"Method '{self.method_name}' not found.")
        
        method = getattr(self.student_code, self.method_name)
        self.assertTrue(callable(method), f"Error: {self.method_name} is not callable.")

        result = method(1, 2, 3)

        self.assertEqual(result, 2.0, "The mean is not correct for the first test.")

    def test_method_complex(self):
        self.assertTrue(hasattr(self.student_code, self.method_name), 
                        f"Method '{self.method_name}' not found.")
        
        method = getattr(self.student_code, self.method_name)
        self.assertTrue(callable(method), f"Error: {self.method_name} is not callable.")

        result = method(5, 23, 42)

        self.assertEqual(result, 70/3, "The mean is not correct for the second test.")

if __name__ == "__main__":
    if not @@$isInExamMode@@:
        unittest.main()