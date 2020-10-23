
import math
import sys
import argparse
 
def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-a')
    parser.add_argument ('-b')
    parser.add_argument ('-c')
    return parser
 
 
if __name__ == '__main__':
    print("Гришин Илья Алексеевич ИУ5-52Б")
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
 
    #print (namespace)
    
    try:
        a=float(namespace.a)
        b=float(namespace.b)
        c=float(namespace.c)
        print("Введены параметры a = {}; b = {}; c = {} уравнения вида a*x^4 + b*x^2 + c = 0:".format(a, b, c))     
    except (ValueError, TypeError):
        f = True
        while f:
            try:
                print("Введите параметры уравнения вида a*x^4 + b*x^2 + c = 0:")
                a=float(input("a = "))
                b=float(input("b = "))
                c=float(input("c = "))
                f = False
            except ValueError:
                print ("Параметры введены неправильно. Повторите ввод")
           
    discr = (b * b) - (4 * a * c)
    #print(discr)
    if a==0 and b==0:
        print("Уравнение не составлено")
    else:
        if discr > 0:
            if a == 0:
                if -c/b > 0:
                    x1=math.sqrt(-c/b)
                    x2=-x1
                    print("x1 = {}; x2 = {}".format(x1, x2)) 
                else:
                    if c==0:
                        print("x1 =",0)
                    else: 
                        print("Действительных корней нет") 
            else:
                t1=(-b+math.sqrt(discr))/(2*a)
                t2=(-b-math.sqrt(discr))/(2*a)
                #print(t1, t2)
                if t1>0:
                    x1=math.sqrt(t1)
                    x2=-x1
                    print("x1 = {}; x2 = {}".format(x1, x2))  
                    f1=False
                else: 
                    f1=True

                if t2>0:
                    x3=math.sqrt(t2)
                    x4=-x3
                    f2=False
                    print("x3 = {}; x4 = {}".format(x3, x4))  
                else: 
                    f2=True
                if f1 and f2:
                    print("Действительных корней нет")       
        else:
            if a!=0 and b==0 and c==0:
                print("x1 =",0)
            else: 
                print("Действительных корней нет")


