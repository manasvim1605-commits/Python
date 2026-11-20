def Calculate_salary(basic_salary, bonus=2000):
    total_salary = basic_salary + bonus
    print(f"Basic Salary: {basic_salary} | Bonus: {bonus} | Total Salary: {total_salary}")


# 1. Default argument (bonus defaults to 2000)
Calculate_salary(25000)

# 2. Positional arguments (both arguments passed by position)
Calculate_salary(30000, 3500)

# 3. Keyword arguments (arguments passed by parameter name, in any order)
Calculate_salary(bonus=5000, basic_salary=40000)