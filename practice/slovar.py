

dict = {"алмаз" : "Система Clarion - один из тех редких алмазов, которые почти неизвестны за пределами сравнительно небольших групп программистов, рассеянных по всему свету. [Мир ПК №1 1998, Николас Петрели, Окно и паутина]",
        "вязкая среда": "Среда существования людей становится связной, подчас почти вязкой. [КомпьюТерра №47 (321) 1999, Сладость снов вне офиса, Найдена Данилович С.В.]",
        "кристалл": "Компания Intel объявила о создании флэш-памяти нового типа, способной хранить в два раза больше данных при том же размере кристалла, что и раньше, а IBM обнародовала метод использования меди для уменьшения размеров микросхем и увеличения их производительности.",
        "'разведение' кристаллов": "... создавался с 'разведением' кристаллов... [Компьютер Пресс №8 1998, Новый процессор Xeon. Найдена Антоновой Н.В.]",
        "глубина": "Минимизируйте глубину цвета. [Компьютер Пресс №5 1999, Руководство по электронному издательству. Найдена Гинсбург М. Ю.]",
        "море": "Завершая отзыв о книге, следует сказать, что в море компьютерной литературы книга Билла Гейтса явление необычное. [Мир ПК №2 1997, Г.Рузайкин, Мифологизация дороги в будущее]",
        "океан": "На 11 дисках поместился целый океан информации. [Мир ПК №12 1997, Дмитрий Рамодин, Linux для разработчиков]",
        "атака": "Атаки на компьютерные узлы осуществлялись преимущественно через Internet. [Мир ПК №4 1998, Руслан Богатырев, Совершенно секретно, или Всемирная электронная нервная система]",
        "битва": "А победа в битве серверов - это очень важная задача для вашей компании. [Мир ПК №2 1998, Марк Гиббс, Как победить в войне Web-серверов]",
        "знамя в атаке": "... летальная среда угробит очередного пользователя, компьютер будет подхвачен, как знамя в атаке. [Компьютер Пресс № 7 1998, Золотые ворота силиконовой долины. Найдена Антоновой Н.В.]"
}

print("="*10, "СЛоварь v-1.0", "="*10)

help = """
s - поиск метафоры по словарю
a - добавить новую словарную статью
r - удалить словарную статью
k - вывод всех метафор
d - вывод всего словаря
q - выход из программы 
"""
choice = ""
while choice != "q":
    choice = input("(h - справка>>)")
    if choice == "s":
        word = input("Введите метафору: ")
        res = dict.get(word, "Нет такой метафоры")
        print(res)
    elif choice == "a":
        word = input("введите новую метафору")
        value = input("Введите контекст")
        dict[word] = value
        print("Словарная статья добавлена")
    elif choice == "r":
        word = input("Введите словарную статью для удаления:")
        del dict[word]
        print("Словарная статья", word, "удалена")
    elif choice == "k":
        print(dict.keys())
    elif choice == "d":
        for i in dict:
            print(i, dict[i], sep = "\n")
    elif choice == "h":
        print(help)
    elif choice == "q":
        continue
    else: 
        print("Нет такой команды, введите h для показа справки")