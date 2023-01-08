work_hours = eval(input("\nHours of work: "))
work_days = work_hours / 8
gross_salary = 500 * work_days
tax_deduct = gross_salary * 0.12

print(f"""
That is {work_days} days
Gross Salary: P{gross_salary:.2f}
Deduction Tax: P{tax_deduct:.2f}
SSS: P100.00
PAG-IBIG: P200.00
Net Salary: P{gross_salary - tax_deduct - 100 - 200:.2f}
""")