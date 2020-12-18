# # coding: utf8

# # Загружаем файл с кодировкай utf8
# text = open('C:\\2\\file.txt','r').read()
# print(text)
# # Декодируем из utf8 в unicode - из внешней в рабочую
# text = text.encode("windows-1252").decode("utf-8")

# # Работаем с текстом
# text += text

# # Кодируем тест из unicode в utf8 - из рабочей во внешнюю
# text = text.encode('utf8')

# # Сохраняем в файл с кодировкий utf8
# open('file.txt','w').write(text)

# # import codecs
# # codecs.open('C:\\2\\file.txt', encoding='utf8')

# # f = open('C:\\2\\file.txt')
# # print(f.read())


# # f=codecs.open('C:\\2\\file.txt', encoding='utf8')
# # print(f.read())

# coding=utf-8           # -*- coding: utf-8 -*-
