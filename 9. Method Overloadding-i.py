class my_calculator:
    def product(self, num_1, num_2 = None, num_3 = None):
        if num_1 != None and num_2 != None and num_3 != None:
            print(num_1 * num_2 * num_3)
        elif num_1 != None and num_2 != None:
            print((num_1 * num_2))
        else:
            print(1 * num_1)



c1 = my_calculator()
c1.product(4)
c1.product(4, 5)
c1.product(4, 5, 6)
