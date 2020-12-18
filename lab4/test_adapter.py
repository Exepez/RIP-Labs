import unittest
from adapter import *
import os

class TestStringMethods(unittest.TestCase):
       
    def test_adapter(self):
        str1="Текстовый Файл --- "
        for index in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя': 
            with self.subTest(index=index): 
                s=str(index)
                testpath="C:\\2\\rip\\lab4\\testfiles\\file"+s+".txt"
                str1 = str1 + s
                with open(testpath, 'wb') as f:
                    f.write(str1.encode('utf-8'))
                f.close()
                print("\n")

                adaptee = Adaptee()
                print("Попытка открытия файла без смены кодировки")
                print(f"Содержимое файла: {adaptee.specific_request(testpath)}", end="\n")
                f.close()

                print("Попытка открытия файла с кодировкой UTF-8")
                adapter = Adapter()
                str2='111'
                if s=='ж':
                    self.assertEqual(client_code(testpath, adapter), "Содержимое файла: " + str2)
                else:
                    self.assertEqual(client_code(testpath, adapter), "Содержимое файла: " + str1)
                # self.assertEqual(client_code(testpath, adapter), "Содержимое файла: " + str1)
                os.remove(testpath)
        
if __name__ == '__main__':
    unittest.main()