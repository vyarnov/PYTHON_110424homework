

    
def ask_data():
    s_name = input("Введите фамилию: ")
    f_name = input("Введите имя: ")
    m_name = input("Введите отчество: ")
    phone = input("Введите номер телефона: ")
    contact = {'second_name': s_name, 'first_name': f_name, 'middle_name': m_name, 'phone_number': phone}
    return contact


def add_new_contact():
    contact = ask_data()
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        for value in contact.values():
            file.write(value +';')
        file.write('\n')

def open_phonebook():
    title=["Фамилия", "Имя", "Отчество", "Телефон"]
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        print("\t\t".join(title))
        for line in file:
            print("\t".join(line.split(";")))

def find_contact():
    # title=["Фамилия", "Имя", "Отчество", "Телефон"]
    s_name=input("Введите фамилию:")
    n_line=str()
    # counter=0
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        # print(*[item + '\t\t' for item in title])
        for line in file:
            line=line.split(";")
            # counter+=1
            if s_name in line[0]:
                # n_line.append(counter)
                n_line=line
                find=True
                break
                # print(*[item + ' ' for item in line])
            else:
                find=False
    if find == True: 
            print("Найдено:")
            print(*n_line)
            
            # n_line=n_line.split(')
        
    else:  print("Не найдено")
    return n_line, find

def copy_contact():
    n_line,find=find_contact()

    if find == True:
        print("Контакт скопирован в файл copyphonebook.txt")
        with open('copyphonebook.txt', 'w+', encoding='utf-8') as file:
            for line in n_line:
                file.write(f"{line}" + " ")



# def delete_contact():
    # find_contact()
            


def main():
    isStop=10
    while isStop !=0:
        print(f"Выберите что хотите сделать: \n1 найти \n2 добавить \n3 удалить \n4 открыть всю книгу \n5 копирование \n0 выход")
        isStop =int(input(">"))
        if isStop ==1:
            find_contact()
        elif isStop ==2:
            add_new_contact()
        elif isStop ==4:
            open_phonebook()
        elif isStop ==5:
            copy_contact()
        input("Нажмите Enter чтобы продолжить ")


main()
        
