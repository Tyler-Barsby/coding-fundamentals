def calculateIncomeTax(salary):
    
    personal_allowance = 11850
    band1_limit = 34500
    band2_limit = 150000
    
    taxable_income = salary - personal_allowance
    
    total_tax = 0.0
    
    if taxable_income <= 0:
        return total_tax
    if taxable_income > band2_limit:
        total_tax += (taxable_income - band2_limit) * 0.3
        taxable_income = band2_limit
    if taxable_income > band1_limit:
        total_tax += (taxable_income - band1_limit) * 0.2
        taxable_income = band1_limit
    
    total_tax += taxable_income * 0.2
    
    return total_tax

def main():
    salary = float(input("Please enter your salary: "))
    return f"Your income tax is: £{calculateIncomeTax(salary):.2f}"

if __name__ == "__main__":
    print(main())