class Intern:
    def __init__(self, name='', surname='', address='', mobile_number='', email=''):
        self.name = name
        self.surname = surname
        self.address = address
        self.mobile_number = mobile_number
        self.email = email

    def getdata(self):
        self.name = input("Введіть ім'я стажера: ")
        self.surname = input("Введіть прізвище стажера: ")
        self.address = input("Введіть адресу стажера: ")
        self.mobile_number = input("Введіть номер мобільного стажера: ")
        self.email = input("Введіть електронну пошту стажера: ")

    def putdata(self):
        print("Ім'я стажера:", self.name)
        print("Прізвище стажера:", self.surname)
        print("Адреса стажера:", self.address)
        print("Номер мобільного стажера:", self.mobile_number)
        print("Електронна пошта стажера:", self.email)

    def __del__(self):
        print("Об'єкт стажера видалено.")


class NewIntern(Intern):
    def show_info(self):
        print("Інформація про стажера:")
        self.putdata()


intern1 = Intern()
intern1.getdata()
intern1.putdata()
del intern1

new_intern = NewIntern()
new_intern.getdata()
new_intern.show_info()
