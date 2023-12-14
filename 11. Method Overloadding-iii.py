from multipledispatch import dispatch   # pip install multipledispatch

class my_calculator:
    @dispatch(int, int)
    def product(self, a, b):
        print(a * b)

    @dispatch(int, int, int)
    def product(self, a, b, c):
        print(a * b * c)

    @dispatch(str, str)
    def product(self, a, b):
        print(int(a) * int(b))

    @dispatch(float, float, float)
    def product(self, a, b, c):
        print(a * b * c)


    @dispatch(str, int)
    def product(self, a, b):
        print(int(a)*b)

c1 = my_calculator()
c1.product("4", 5)
c1.product(4, 5, 6)
c1.product (4.0, 5.0, 6.00)
c1.product("4", "5")
