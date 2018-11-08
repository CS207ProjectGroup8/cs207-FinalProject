##This class is used to define the behavior of elementary functions
import numpy as np
from . import AutoDiffObject

class ElementaryFunctions():

    ''' Create objects that support elementary functions on AutoDiff objects and return AutoDiff objects

    EXAMPLE:
            x = AutoDiff(3, "x")
            new_x = ElementaryFunctions.sin(x)
    '''
    
    @staticmethod
    def sin(other):
        
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
        >>> t = ElementaryFunctions.sin(a)
        >>> print(t.val)
        0.9092974268256817
        >>> print(t.der['a'])
        -0.4161468365471424

        >>> a = AutoDiff(1, 'a')
        >>> b = 33
        >>> t = ElementaryFunctions.sin(a * b)
        >>> print(t.val, t.der)
        0.9999118601 {'a': -0.01327674722}
        '''

        try:
            ##try to find if the passed in other object is autodiff object and do
            ##proper operation to the passed in object
            other_val = other.val
            other_der = {}
            sin_value,cos_for_der = np.sin(other_val), np.cos(other_val)
            for key,derivative in other.der.items():
                other_der[key] = cos_for_der * derivative
            return autodiff.AutoDiff(sin_value, "dummy", other_der)
        except:
            try:
                ##try to check if the passed in other object is numeric value
                other_value = other.real
                return np.sin(other_value)
            except:
                ##catch error if passed object is not numeric or autodiff
                print("illegal argument. Needs to be either autodiff object or numeric value")
                raise AttributeError
    
    @staticmethod
    def cos(other):
        
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
        >>> t = ElementaryFunctions.cos(a)
        >>> print(t.val)
        -0.41614683654
        >>> print(t.der['a'])
        -0.90929742682

        >>> a = AutoDiff(1, 'a')
        >>> b = 33
        >>> t = ElementaryFunctions.cos(a * b)
        >>> print(t.val, t.der)
        -0.01327674722 {'a': -0.9999118601}
        '''
        
        try:
            ##try to find if the passed in other object is autodiff object and do
            ##proper operation to the passed in object
            other_val = other.val
            other_der = {}
            cos_value,sin_for_der = np.cos(other_val), -np.sin(other_val)
            for key,derivative in other.der.items():
                other_der[key] = sin_for_der * derivative
            return autodiff.AutoDiff(cos_value, "dummy", other_der)
        except:
            try:
                ##try to check if the passed in other object is numeric value
                other_value = other.real
                return np.cos(other_value)
            except:
                ##catch error if passed object is not numeric or autodiff
                print("illegal argument. Needs to be either autodiff object or numeric value")
                raise AttributeError
    
    @staticmethod
    def tan(other):
        
        ''' Returns the another AutoDiff object or numeric value after
        performing tangent operation on the input

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
        >>> t = ElementaryFunctions.tan(a)
        >>> print(t.val)
        -2.18503986326
        >>> print(t.der['a'])
        5.77439920404

        >>> a = AutoDiff(1, 'a')
        >>> b = 33
        >>> t = ElementaryFunctions.tan(a * b)
        >>> print(t.val, t.der)
        -75.3130148001 {'a': 42.0282677387}
        '''

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
            return autodiff.AutoDiff(tan_value, "dummy", other_der)

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

    @staticmethod
    def power(base,power):
        
        ''' Returns the another AutoDiff object or numeric value after
        raising base to the power operation

        ARGUMENTS
        ========
        base -- the base of the operation, can either be AutoDiff object or numeric
        power -- the power of the operation, can either be AutoDiff object or numeric

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
        >>> b = AutoDiff(3, 'b')
        >>> t = ElementaryFunctions.power(a,b)
        >>> print(t.val)
        8
        >>> print(t.der['a'])
        5.545177444479562
        >>> print(t.der['b'])
        12

        >>> a = AutoDiff(1, 'a')
        >>> b = 2
        >>> t = ElementaryFunctions.power(a * b)
        >>> print(t.val, t.der)
        4 {'a': 4}
        '''
        
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

                return autodiff.AutoDiff(base_value, "dummy", other_der)
            except:
                ##when base is autodiff object and power is not

                if type(np.power(base.val, power.real)) == complex:
                    print ("base value should be positive, because we don't consider imaginary number here.")
                    raise ValueError



                base_value = np.power(base_val, power)
                base_der = power * np.power(base_val, power-1)
                for key,derivative in base.der.items():
                    other_der[key] = base_der * derivative
                return autodiff.AutoDiff(base_value, "dummy", other_der)
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

                    other_der = {}
                    ##try to check if the passed in other object is numeric value
                    for key,derivative in power.der.items():
                        other_der[key] = power.der[key] * np.log(base) * np.power(base,power.val)
                    return autodiff.AutoDiff(np.power(base.val,power.val), "dummy", other_der)
                except:

                    if type(np.power(base, power)) == complex:
                        print ("base value should be positive, because we don't consider imaginary number here.")
                        raise ValueError

                    return np.power(base,power)

            except:
                ##catch error if passed object is not numeric or autodiff
                print("illegal argument. Needs to be either autodiff object or numeric value")
                raise AttributeError

    @staticmethod
    def log(other):
        
        ''' Returns the another AutoDiff object or numeric value after
        performing logrismic operation on the input

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
        >>> t = ElementaryFunctions.log(a)
        >>> print(t.val)
        0.30102999566
        >>> print(t.der['a'])
        0.5
        '''

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
            return autodiff.AutoDiff(log_value, "dummy", other_der)

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

    @staticmethod
    def exp(other):
        
        ''' Returns the another AutoDiff object or numeric value after
        performing exponential operation on the input

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
        >>> t = ElementaryFunctions.exp(a)
        >>> print(t.val)
        7.38905609893065
        >>> print(t.der['a'])
        7.38905609893065
        '''

        try:
            other_val = other.val
            other_der = {}
            exp_value, exp_for_der = np.exp(other_val), np.exp(other_val)
            for key,derivative in other.der.items():
                other_der[key] = exp_for_der * derivative
            return autodiff.AutoDiff(exp_value, "dummy", other_der)
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
    x = autodiff.AutoDiff(2, "x")
    y = autodiff.AutoDiff(3, "y")
    z = autodiff.AutoDiff(4, "z")

    f = 5*x + ElementaryFunctions.tan(7*x*y)
    print(f.val, f.der)

    f2 = ElementaryFunctions.log((3*x))
    print(f2.val, f2.der)

    f3 = ElementaryFunctions.power(x,2)
    print(f3.val, f3.der)

    f4 = ElementaryFunctions.exp(x)
    print(f4.val, f4.der)

#    f6 = ElementaryFunctions.sin("thirty")
#    print(f6.val, f6.der)
