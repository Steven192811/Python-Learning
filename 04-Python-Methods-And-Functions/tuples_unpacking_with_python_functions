stock_prices = [('APPL', 200), ('GOOG', 400), ('MSFT', 100)]

for item in stock_prices:
    print(item) # ('APPL', 200) ('GOOG', 400) ('MSFT', 100)

for ticker,price in stock_prices:
    print(ticker) # APPL GOOG MSFT
    print(price+(0.1*price)) # 220.0 440.0 110.0 # 10% increase in price

    work_hours = [('Abby',25),('Ella',30),('Emma',37.5)]

    def employee_check(work_hours):
        current_max = 0 # placeholder variable
        employee_of_month = '' # placeholder variable

        for employee,hours in work_hours: # iterate through the list
            if hours > current_max: # if hours is greater than current_max
                current_max = hours # update current_max
                employee_of_month = employee # update employee_of_month
            else:
                pass

        # Return
        return (employee_of_month,current_max) # return tuple of employee_of_month and current_max hours worked by employee_of_month

result = employee_check(work_hours) # ('Emma', 37.5)
print(result) # ('Emma', 37.5)
name,hours = employee_check(work_hours) # tuple unpacking
print(name) # Emma
print(hours) # 37.5

item = employee_check(work_hours) # tuple unpacking
print(item) # ('Emma', 37.5)
