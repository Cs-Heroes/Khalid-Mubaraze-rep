class main:
    def __init__():
        print("it is constructer")
    def show():
        print("show in parent")
class sub(main):
    pass
    # def show():
    #     print("it is show in sub class")

obj=main()
obj.show()
obj1.sub()
obj1.show()
