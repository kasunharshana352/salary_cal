import unittest
import json
from salary_calculator import parse_salary_input, calculate_salary

class TestSalaryCalculator(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Load test data from test_data.json
        with open('test_data.json') as f:
            cls.test_data = json.load(f)
    
    def test_valid_inputs(self):
        for test_case in self.test_data["valid_inputs"]:
            with self.subTest(test_case=test_case):
                user_input = test_case["input"]
                expected = test_case["expected"]
                gross_salary = parse_salary_input(user_input)
                self.assertEqual(gross_salary, expected)

    def test_invalid_inputs(self):
        for test_case in self.test_data["invalid_inputs"]:
            with self.subTest(test_case=test_case):
                user_input = test_case["input"]
                expected_error = test_case["expected_error"]
                with self.assertRaises(ValueError) as context:
                    parse_salary_input(user_input)
                self.assertEqual(str(context.exception), expected_error)
    
    def test_salary_calculation(self):
        for test_case in self.test_data["salary_calculations"]:
            with self.subTest(test_case=test_case):
                gross_salary = test_case["gross_salary"]
                expected_result = test_case["result"]
                result = calculate_salary(gross_salary)
                for key, value in expected_result.items():
                    self.assertAlmostEqual(result[key], value, places=2)
    
    def test_tax_calculation(self):
        for test_case in self.test_data["tax_calculation"]:
            with self.subTest(test_case=test_case):
                gross_salary = test_case["gross_salary"]
                expected_tax = test_case["expected_tax"]
                result = calculate_salary(gross_salary)
                self.assertEqual(result["Tax"], expected_tax)

if __name__ == '__main__':
    unittest.main() 
