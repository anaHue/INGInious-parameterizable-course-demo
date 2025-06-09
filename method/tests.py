import importlib.util
import sys
import io
import unittest

class TestStudentCode(unittest.TestCase):
    def setUp(self):
        self.student_code_path = "/task/student/code.py"
        self.method_name = "print_text"

        spec = importlib.util.spec_from_file_location("student_code", self.student_code_path)
        self.student_code = importlib.util.module_from_spec(spec)
        sys.modules["student_code"] = self.student_code
        spec.loader.exec_module(self.student_code)

    def test_method_output(self):
        self.assertTrue(hasattr(self.student_code, self.method_name), 
                        f"Method '{self.method_name}' not found.")
        
        method = getattr(self.student_code, self.method_name)
        self.assertTrue(callable(method), f"Error: {self.method_name} is not callable.")

        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            method()
        finally:
            sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip()

        self.assertNotEqual(output, "Correct", "The output must not be 'Correct'.")

if __name__ == "__main__":
    if not @@$isInExamMode@@:
        unittest.main()