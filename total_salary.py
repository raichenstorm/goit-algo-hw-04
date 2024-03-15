def total_salary(path):
    salary = 0
    employees_number = 0
    total = 0

    try:
        with open(path, 'r') as fh:
            for line in fh:
                line_prepared = line.strip()
                name, salary = line_prepared.split(',')
                total += int(salary)
                employees_number += 1
        if employees_number == 0:
            return 0, 0
        average_salary = int(total / employees_number)
        return total, average_salary
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return 0, 0
    except Exception:
        print('Виникла помилка.')
        return 0, 0

total, average_salary = total_salary(r"salaries.txt")
print(f'Загальна заробітня плата - {total}, середня заробітня плата - {average_salary}.')