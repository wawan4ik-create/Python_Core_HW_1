def total_salary(path):
    if not path:
        return (0, 0)
    
    total = 0
    length = 0
    
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            salary = float(line.split(',')[1].strip())            
            total += salary
            length += 1

    return (total, total/length)


if __name__ == '__main__':
    total, average = total_salary("salaries.txt")
    print(f"Загальна сума заробітної плати: {total},\nСередня заробітна плата: {average}")
