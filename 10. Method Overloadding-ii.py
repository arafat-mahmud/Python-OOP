class my_calculator:

    def product(self, *num):
        sum = 1
        for x in num:
            sum = sum * x
        print(sum)

c1 = my_calculator
c1.product(4)
c1.product(4, 5)
c1.product(4, 5, 6, 7)