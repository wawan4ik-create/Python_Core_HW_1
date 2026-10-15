def get_cats_info(path=None):
    if path is None:
        print("Шлях до файлу не вказано.")
        return None
    
    with open(path, 'r', encoding='utf-8') as file: 
        cats_info = []
        for line in file:
            id, name, age = line.strip().split(',')
            cats_info.append({'id': id, 'name': name, 'age': age})
    return cats_info


if __name__ == '__main__':
    cats_info = get_cats_info("cats.txt")
    print(cats_info)