def get_employee_data():
    employee_data = []
    num_employees = int(input("Enter the number of employees: "))

    for _ in range(num_employees):
        last_name = input("Enter the employee's last name: ")
        salary = float(input("Enter the employee's salary: "))
        employee_data.append((last_name, salary))

    return employee_data

def save_to_file(employee_data, filename):
    with open(filename, 'w') as file:
        for last_name, salary in employee_data:
            file.write(f"{last_name}\n{salary:.2f}\n")

def read_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    employee_data = []
    for i in range(0, len(lines), 2):
        last_name = lines[i].strip()
        salary = float(lines[i + 1].strip())
        employee_data.append((last_name, salary))

    return employee_data

def get_bonus_rate(salary):
    if salary >= 100000.00:
        return 0.20
    elif salary >= 50000.00:
        return 0.15
    else:
        return 0.10

def calculate_and_display_bonuses(employee_data):
    total_bonus = 0.0

    for last_name, salary in employee_data:
        bonus_rate = get_bonus_rate(salary)
        bonus = salary * bonus_rate
        total_bonus += bonus
        print(f"{last_name}: Salary = ${salary:.2f}, Bonus = ${bonus:.2f}")

    print(f"\nTotal Bonuses Paid Out: ${total_bonus:.2f}")

def main():
    filename = 'employee_data.txt'
    employee_data = get_employee_data()
    save_to_file(employee_data, filename)
    read_employee_data = read_from_file(filename)
    calculate_and_display_bonuses(read_employee_data)

if __name__ == "__main__":
    main()