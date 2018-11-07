##This class is used to define the behavior of elementary functions
import sys
sys.path.append("./")
import math
import numpy as np
from AutoDiffObject import AutoDiff

class ElementaryFunctions():

    ''' Create objects that support elementary functions on AutoDiff objects and return AutoDiff objects

    EXAMPLE:
            x = AutoDiff(3, "x")
            ef = ElementaryFunctions()
            new_x = ef.sin(x)
    '''

    def __init__(self):
        return

    def sin(self,other):
        ''' Returns the another AutoDiff object or numeric value after
        performing sine operation on the input

        RETURNS
        ========
        A new instance of AutoDiff object or numeric value

        NOTES
        =====
        PRE:
             - EITHER: another instance of AutoDiff class
                 OR: float

        POST:
             - Return a new Autodiff class instance or a numeric value

        EXAMPLES
        =========
        >>> a = AutoDiff(2, 'a')
        >>> ef = ElementaryFunctions()
        >>> t = ef.sin(a)
        >>> print(t.val)
        0.9092974268256817
        >>> print(t.der['a'])
        -0.4161468365471424

        >>> a = AutoDiff(1, 'a')
        >>> b = 33
        >>> ef = ElementaryFunctions()
        >>> t = ef.sin(a * b)
        >>> print(t.val, t.der)
        0.9999118601 {'a': -0.01327674722}
        '''

        try:
            ##try to find if the passed in other object is autodiff object and do
            ##proper operation to the passed in object
            other_val, other_varName = other.val, other.varName
            other_der = {}
            sin_value,cos_for_der = np.sin(other_val), np.cos(other_val)
            for key,derivative in other.der.items():
                other_der[key] = cos_for_der * derivative
            return AutoDiff(sin_value, "dummy", other_der)
        except:
            try:
                ##try to check if the passed in other object is numeric value
                other_value = other.real
                return np.sin(other_value)
            except:
                ##catch error if passed object is not numeric or autodiff
                print("illegal argument. Needs to be either autodiff object or numeric value")
                raise AttributeError

    def cos(self,other):
        ''' Returns the another AutoDiff object or numeric value after
        performing cosine operation on the input

        RETURNS
        ========
        A new instance of AutoDiff object or numeric value

        NOTES
        =====
        PRE:
             - EITHER: another instance of AutoDiff class
                 OR: float

        POST:
             - Return a new Autodiff class instance or a numeric value

        EXAMPLES
        =========
        >>> a = AutoDiff(2, 'a')
        >>> ef = ElementaryFunctions()
        >>> t = ef.sin(a)
        >>> print(t.val)
        0.9092974268256817
        >>> print(t.der['a'])
        -0.4161468365471424

        >>> a = AutoDiff(1, 'a')
        >>> b = 33
        >>> ef = ElementaryFunctions()
        >>> t = ef.sin(a * b)
        >>> print(t.val, t.der)
        0.9999118601 {'a': -0.01327674722}
        '''
        try:
            ##try to find if the passed in other object is autodiff object and do
            ##proper operation to the passed in object
            other_val, other_varName = other.val, other.varName
            other_der = {}
            cos_value,sin_for_der = np.cos(other_val), -np.sin(other_val)
            for key,derivative in other.der.items():
                other_der[key] = sin_for_der * derivative
            return AutoDiff(cos_value, "dummy", other_der)
        except:
            try:
                ##try to check if the passed in other object is numeric value
                other_value = other.real
                return np.cos(other_value)
            except:
                ##catch error if passed object is not numeric or autodiff
                print("illegal argument. Needs to be either autodiff object or numeric value")
                raise AttributeError

    def tan(self,other):
        try:
            if abs(np.tan(other.val)) > 10**16:
                print ("input value should not be pi/2 + 2*pi*k, k integer ")
                raise ValueError
            ##try to find if the passed in other object is autodiff object and do
            ##proper operation to the passed in object
            other_val= other.val
            other_der = {}
            tan_value, tan_for_der = np.tan(other_val), 1/(np.cos(other_val)**2)
            if abs(tan_value) > 10**16:
                print("Input value should not be pi/2 + 2*pi*k, k interger ")
                raise ValueError
            for key,derivative in other.der.items():
                other_der[key] = tan_for_der * derivative
            return AutoDiff(tan_value, "dummy", other_der)

        except:
            try:
                if abs(np.tan(other.real)) > 10**16:
                    print ("input value should not be a pi/2 + 2*pi*k, k integer ")
                    raise ValueError
                ##try to check if the passed in other object is numeric value
                other_value = other.real
                if abs(np.tan(other_value)) > 10**16:
                    print("Input value should not be pi/2 + 2*pi*k, k interger ")
                    raise ValueError
                return np.tan(other_value)
            except:
                ##catch error if passed object is not numeric or autodiff
                print("illegal argument. Needs to be either autodiff object or numeric value")
                raise AttributeError

    def power(self,base,power):
        try:
            ##try to find if the passed in base and power object is autodiff object and do
            ##proper operation to the passed in object
            base_val = base.val
            other_der = {}
            try:
                ##When both the base and the power are autodiff objects

                if type(np.power(base.val, power.val)) == complex:
                    print ("base value should be positive, because we don't consider imaginary number here.")
                    raise ValueError


                power_val = power.val
                base_value = np.power(base.val, power.val)
                base_der = set(base.der)
                power_der = set(power.der)
                for key in base_der.union(power_der):
                    if key in base_der and key in power_der:

                        if base.val <= 0:
                            print ("base value should be positive, because we don't consider imaginary number here.")
                            raise ValueError


                        other_der[key] = np.power(base.val,power.val-1) * (power.val * base.der[key] + base.val * np.log(base.val) * power.der[key])
                    elif key in base_der:
                        other_der[key] = power.val * np.power(base.val,power.val-1) * base.der[key]
                    else:

                        if base.val <= 0:
                            print ("base value should be positive, because we don't consider imaginary number here.")
                            raise ValueError

                        other_der[key] = power.der[key] * np.log(base.val) * base_value

                return AutoDiff(base_value, "dummy", other_der)
            except:
                ##when base is autodiff object and power is not

                if type(np.power(base.val, power.real)) == complex:
                    print ("base value should be positive, because we don't consider imaginary number here.")
                    raise ValueError



                base_value = np.power(base_val, power)
                base_der = power * np.power(base_val, power-1)
                for key,derivative in base.der.items():
                    other_der[key] = base_der * derivative
                return AutoDiff(base_value, "dummy", other_der)
        except:
            try:
                base_value = base.real


                try:
                    #base numeric, power autodiff
                    if type(np.power(base.real, power.val)) == complex:
                        print ("base value should be positive, because we don't consider imaginary number here.")
                        raise ValueError

                    if base.real <= 0:
                        print ("base value should be positive, because we don't consider imaginary number here.")
                        raise ValueError

                    power_val = power.val
                    other_der = {}
                    ##try to check if the passed in other object is numeric value
                    for key,derivative in power.der.items():
                        other_der[key] = power.der[key] * np.log(base) * np.power(base,power.val)
                    return AutoDiff(np.power(base.val,power.val), "dummy", other_der)
                except:

                    if type(np.power(base, power)) == complex:
                        print ("base value should be positive, because we don't consider imaginary number here.")
                        raise ValueError

                    return np.power(base,power)

            except:
                ##catch error if passed object is not numeric or autodiff
                print("illegal argument. Needs to be either autodiff object or numeric value")
                raise AttributeError

    ##Need to look more into it
    def log(self,other):
        try:
            ##try to find if the passed in other object is autodiff object and do
            ##proper operation to the passed in object
            other_val = other.val

            if other_val <= 0:
                    print ("base value should be positive, because we don't consider imaginary number here.")
                    raise ValueError

            other_der = {}
            log_value, log_for_der = np.log(other_val), 1/float(other_val)
            for key,derivative in other.der.items():
                other_der[key] = log_for_der * derivative
            return AutoDiff(log_value, "dummy", other_der)

        except:
            try:
                ##try to check if the passed in other object is numeric value
                other_value = other.real

                if other_value <= 0:
                    print ("base value should be positive, because we don't consider imaginary number here.")
                    raise ValueError

                return np.log(other_value)
            except:
                ##catch error if passed object is not numeric or autodiff
                print("illegal argument. Needs to be either autodiff object or numeric value")
                raise AttributeError


    def exp(self,other):
        try:
            other_val = other.val
            other_der = {}
            exp_value, exp_for_der = np.exp(other_val), np.exp(other_val)
            for key,derivative in other.der.items():
                other_der[key] = exp_for_der * derivative
            return AutoDiff(exp_value, "dummy", other_der)
        except:
            try:
                ##try to check if the passed in other object is numeric value
                other_value = other.real
                return np.exp(other_value)
            except:
                ##catch error if passed object is not numeric or autodiff
                print("illegal argument. Needs to be either autodiff object or numeric value")
                raise AttributeError


if __name__ == "__main__":
    x = AutoDiff(-2, "x")
    y = AutoDiff(3, "y")
    z = AutoDiff(4, "z")
    ef = ElementaryFunctions()

    f = 5*x + ef.tan(7*x*y)
    print(f.val, f.der)

    f2 = ef.log((3*x))
    print(f2.val, f2.der)

    f3 = ef.power(x,z)
    print(f3.val, f3.der)

    f4 = ef.exp(x*y)
    print(f4.val, f4.der)

    # f6 = ef.sin("thirty")
    # print(f6.val, f6.der)