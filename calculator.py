class Calculator(object):
    def add(self, a, b):
        number_types = (int, float, complex)

        if isinstance(a, number_types) and isinstance(b, number_types):
            import pdb; pdb.set_trace()
            result =  a + b
            print ('Result is: {}'.format(result))
            return result
        else:
            raise ValueError
