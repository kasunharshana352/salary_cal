def calculate_salary(gross_salary):
    # Ensure the gross salary is a positive number
    if not isinstance(gross_salary, (int, float)) or gross_salary < 0:
        raise ValueError("Gross salary must be a positive number.")
    
    # EPF and ETF Calculations
    employer_epf = gross_salary * 0.12
    employee_epf = gross_salary * 0.08
    employer_etf = gross_salary * 0.03
    
    # Tax Calculation
    taxable_income = gross_salary
    tax = 0

    # Tax slabs (progressive tax rates)
    tax_slabs = [
        (100000, 0),      # 0% tax on first 100,000
        (150000, 6),      # 6% tax on the next 50,000
        (200000, 12),     # 12% tax on the next 50,000
        (250000, 18),     # 18% tax on the next 50,000
        (300000, 24),     # 24% tax on the next 50,000
        (350000, 30),     # 30% tax on the next 50,000
        (float("inf"), 36)  # 36% tax on everything above 350,000
    ]
    
    lower_bound = 0
    for upper_bound, rate in tax_slabs:
        if taxable_income > lower_bound:
            taxable_amount = min(taxable_income, upper_bound) - lower_bound
            tax += (taxable_amount * rate) / 100
        lower_bound = upper_bound

    # Take-home Salary and Total Benefit calculation
    take_home_salary = gross_salary - employee_epf - tax
    total_benefit = gross_salary + employer_epf + employer_etf

    # Return the results as a dictionary for easy access
    return {
        "Gross Salary": gross_salary,
        "Employer EPF": employer_epf,
        "Employee EPF": employee_epf,
        "Employer ETF": employer_etf,
        "Tax": round(tax, 2),  # Ensuring tax is rounded to 2 decimal places
        "Take-home Salary": round(take_home_salary, 2),
        "Total Benefit": round(total_benefit, 2)
    }


def parse_salary_input(user_input):
    """
    Parse the salary input string, handling suffixes like K, L, M, and B,
    and convert it to a float for calculation.
    """
    if not user_input:
        raise ValueError("Input cannot be empty.")
    
    # Remove spaces and commas from the input
    cleaned_input = user_input.replace(" ", "").replace(",", "")

    # Handle suffixes for large numbers
    multiplier = 1
    if cleaned_input[-1] in "KkLlMmBb":
        suffix = cleaned_input[-1].upper()
        if suffix == "K":
            multiplier = 1_000
        elif suffix == "L":
            multiplier = 100_000
        elif suffix == "M":
            multiplier = 1_000_000
        elif suffix == "B":
            multiplier = 1_000_000_000
        else:
            raise ValueError(f"Invalid suffix '{suffix}' in input.")
        cleaned_input = cleaned_input[:-1]  # Remove the suffix

    # Try to convert the cleaned input to a float
    try:
        cleaned_input = float(cleaned_input)
    except ValueError:
        raise ValueError("Input contains invalid characters.")

    # Return the final amount after applying the multiplier
    return cleaned_input * multiplier


if __name__ == "__main__":
    print("Welcome to the Salary Calculator")
    print("You can use the following suffixes for large numbers:")
    print("K: Thousand (e.g., 50K = 50,000)")
    print("L: Lakh (e.g., 5L = 500,000)")
    print("M: Million (e.g., 1.5M = 1,500,000)")
    print("B: Billion (e.g., 2B = 2,000,000,000)\n")

    while True:
        try:
            user_input = input("Enter the gross salary (or type 'exit' to quit): ").strip()
            if user_input.lower() == "exit":
                print("Goodbye! Have a great day!")
                break

            gross_salary = parse_salary_input(user_input)
            result = calculate_salary(gross_salary)

            print("\nSalary Breakdown:")
            for key, value in result.items():
                print(f"{key}: {value:,.2f}")  # Added comma formatting for better readability

        except ValueError as e:
            print(f"Error: {e} Please try again.")
        except Exception as e:
            print(f"Unexpected error: {e} Please try again.")
