import codecs

class Target:
    def request(self,path) -> str:
        f = open(path)
        text=f.read()
        f.close()
        return f"Содержимое файла: "+text


class Adaptee:
    def specific_request(self, path) -> str:
        f = open(path, 'r')
        text=f.read()
        f.close()
        return text


class Adapter(Target, Adaptee):
    def request(self, path) -> str:
        f=codecs.open(path, encoding='utf8')
        text=f.read()
        f.close()
        return f"Содержимое файла: "+text


def client_code(path, target: "Target") -> None:
    print(target.request(path), end="")
    return target.request(path)


if __name__ == "__main__":
    path = 'C:\\2\\rip\\lab4\\testfiles\\file.txt'
    # path = 'C:\\2\\file.txt'
    print("\n")
    print("Попытка открытия файла без необходимости смены кодировки")
    target = Target()
    client_code(path, target)
    print("\n\n")

    adaptee = Adaptee()
    print("Попытка открытия файла без смены кодировки")
    print(f"Содержимое файла: {adaptee.specific_request(path)}", end="\n\n")

    print("Попытка открытия файла с кодировкой UTF-8")
    adapter = Adapter()
    client_code(path, adapter)

    