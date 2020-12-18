def print_result(func):
    def decorated_func(*args):
        print(func.__name__)
        result = func(*args)
        if (type(result)==list):
            for i in result:
                print(i)
        else:
            if (type(result)==dict):
                for i in result:
                    print(i, '-->', result.get(i))
            else:
                print(result)
        return result
    return decorated_func

@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


def main():
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()


if __name__ == '__main__':
    main()
