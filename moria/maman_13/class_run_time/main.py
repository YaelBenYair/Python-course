from moria.maman_13.class_run_time.class_parent import *
from moria.maman_13.class_run_time.menu import Menu

if __name__ == '__main__':

    menu = Menu()
    menu.run()

    # a = Politician('yael', 'bla bla')
    # a.display()
    # # ab = input("enter:")
    # # print(ab)
    # # t = "str"
    # # print(isinstance(ab, t))
    # Student = type('Student', (Politician,), {'major': 'bla'})
    # s = Student('moria', 'comp')
    #
    #
    # # # Student.__bases__ = (Politician,)
    # s.display()
    # print(Student.__dict__)
    # print(s.major)
    # print(s.__dict__)
    # print(Politician.__dict__)
    # print(s.__class__.__name__)
    # # print(s.display)
    #
    # Student = type('Student', (Barber,), {'major': 'bla'})
    # s = Student('moria', 'comp')
    # # Student.__bases__ = (Politician,)
    # s.display()

    # base_class_name = "Politician"
    # d = {'major': 'bla'}
    # class_name = "Bob"
    # UserClass = type(f'{class_name}', (base_class_name,), d)
    # b = UserClass()
    # print(b.__class__.__name__)
    # b.display()

    #     exec(f"""
    #     Bob = type('Bob', ({class_name},), {d})
    # """)


