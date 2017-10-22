class Calculator(object):
    def add(self, a, b):
        number_types = (int, float, complex)

        if isinstance(a, number_types) and isinstance(b, number_types):
            print ('A is: {}'.format(a))
            print ('B is: {}'.format(b))
            result =  a - b
            print ('Result is: {}'.format(result))
            return result
        else:
            raise ValueError
