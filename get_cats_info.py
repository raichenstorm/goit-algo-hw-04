def get_cats_info(path):
    cats_info = list()
    try:
        with open(path, 'r') as fh:
            for line in fh:
                dict_keys = line.strip().split(',')
                if len(dict_keys) == 3:
                    cat = {
                        'id' : dict_keys[0],
                        'name' : dict_keys [1],
                        'age': dict_keys [2]
                    }
                    cats_info.append(cat)
                else:
                    print('У вашому файлі є проблема, неможливо зчитати потрібні дані')
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
    except Exception as error:
        print('Виникла помилка:', error)   
    return cats_info

cats_info = get_cats_info(r'cats.txt')
print(cats_info)

