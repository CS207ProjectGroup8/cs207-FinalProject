##This class is used to define the behavior of elementary functions
import numpy as np
from src.source_code.AutoDiffObject import AutoDiff

class ElementaryFunctions():

    ''' Create objects that support elementary functions on AutoDiff objects and return AutoDiff objects

    EXAMPLE:
            x = AutoDiffObject.AutoDiff(3, "x")
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
        >>> np.isclose(t.val, 0.9092974268256817)
        True
        >>> np.isclose(t.der['a'], -0.4161468365471424)
        True
        >>> a = AutoDiff(1, 'a')
        >>> b = 33
        >>> t = ElementaryFunctions.sin(a * b)
        >>> np.isclose(t.val, 0.9999118601072672)
        True
        >>> np.isclose(t.der['a'], -0.4381326583609628)
        True
        >>> x = AutoDiff(4, 'x')
        >>> y = AutoDiff(3, 'y')
        >>> t = ElementaryFunctions.sin(x*x*y*y)
        >>> np.isclose(t.val, -0.4910216)
        True
        >>> np.isclose(t.der['x'], 62.72261)
        True
        >>> np.isclose(t.der['y'], 83.63015)
        True
        >>> np.isclose(t.der2['x'], 2561.137)
        True
        >>> np.isclose(t.der2['y'], 4553.132)
        True
        >>> np.isclose(t.der2['xy'], 3435.756)
        True
        >>>
        '''

        try:
            ##try to find if the passed in other object is autodiff object and do
            ##proper operation to the passed in object
            other_val = other.val
            other_der = {}
            other_der2 = {}
            sin_value,cos_value = np.sin(other_val), np.cos(other_val)

            # first derivative
            for key,derivative in other.der.items():
                other_der[key] = cos_value * derivative

            # second derivative
            # loop through all keys in second derivative dictionary
            for key, derivative2 in other.der2.items():
                # check if that key is in first derivative dictionary so we are taking second derivative w.r.t. one variable
                # i.e., f_xx --> key == x and x in first derivative dictionary
                if key in other.der.keys():
                    other_der2[key] = -1*other.der[key]*sin_value*other.der[key] + cos_value*other.der2[key]
                else:
                    # split the second derivative dictionary key into the two variables
                    first_var = key[0]
                    second_var = key[1]
                    other_der2[key] = -1*other.der[first_var]*other.der[second_var]*sin_value + cos_value*other.der2[key]

            return AutoDiff(sin_value, "dummy", other_der, other_der2)

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
        >>> np.isclose(t.val, -0.4161468365471424)
        True
        >>> np.isclose(t.der['a'], -0.9092974268256817)
        True
        >>> a = AutoDiff(1, 'a')
        >>> b = 33
        >>> t = ElementaryFunctions.cos(a * b)
        >>> np.isclose(t.val, -0.013276747223059479)
        True
        >>> np.isclose(t.der['a'], -32.99709138353982)
        True
        '''

        try:
            ##try to find if the passed in other object is autodiff object and do
            ##proper operation to the passed in object
            other_val = other.val
            other_der = {}
            other_der2 = {}
            cos_value,sin_value = np.cos(other_val), np.sin(other_val)
            for key,derivative in other.der.items():
                other_der[key] = -1 * sin_value * derivative

            # second derivative
            # loop through all keys in second derivative dictionary
            for key, derivative2 in other.der2.items():
                # check if that key is in first derivative dictionary so we are taking second derivative w.r.t. one variable
                # i.e., f_xx --> key == x and x in first derivative dictionary
                if key in other.der.keys():
                    other_der2[key] = -1*other.der[key]*cos_value*other.der[key] + -1*sin_value*other.der2[key]
                else:
                    # split the second derivative dictionary key into the two variables
                    first_var = key[0]
                    second_var = key[1]
                    other_der2[key] = -other.der[first_var]*other.der[second_var]*cos_value + -1*sin_value*other.der2[key]

            return AutoDiff(cos_value, "dummy", other_der, other_der2)


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
        >>> np.isclose(t.val, -2.185039863261519)
        True
        >>> np.isclose(t.der['a'], 5.774399204041917)
        True
        >>> a = AutoDiff(1, 'a')
        >>> b = 33
        >>> t = ElementaryFunctions.tan(a * b)
        >>> np.isclose(t.val, -75.31301480008509)
        True
        >>> np.isclose(t.der['a'], 187210.6565431686)
        True
        '''

        try:
            if abs(np.tan(other.val)) > 10**16:
                print ("input value should not be pi/2 + 2*pi*k, k integer ")
                raise ValueError
            ##try to find if the passed in other object is autodiff object and do
            ##proper operation to the passed in object
            other_val= other.val
            other_der = {}
            other_der2 = {}
            tan_value, sec2_value = np.tan(other_val), 1/(np.cos(other_val)**2)
            if abs(tan_value) > 10**16:
                print("Input value should not be pi/2 + 2*pi*k, k interger")
                raise ValueError

            # first derivative
            for key,derivative in other.der.items():
                other_der[key] = sec2_value * derivative

            # second derivative
            # loop through all keys in second derivative dictionary
            for key, derivative2 in other.der2.items():
                # check if that key is in first derivative dictionary so we are taking second derivative w.r.t. one variable
                # i.e., f_xx --> key == x and x in first derivative dictionary
                if key in other.der.keys():
                    other_der2[key] = 2*other.der[key]*other.der[key]*sec2_value*tan_value + sec2_value*other.der2[key]
                else:
                    # split the second derivative dictionary key into the two variables
                    first_var = key[0]
                    second_var = key[1]
                    other_der2[key] = 2*other.der[first_var]*other.der[second_var]*sec2_value*tan_value + sec2_value*other.der2[key]

            return AutoDiff(tan_value, "dummy", other_der, other_der2)

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
        >>> a = AutoDiffObject.AutoDiff(2, 'a')
        >>> b = AutoDiffObject.AutoDiff(3, 'b')
        >>> t = ElementaryFunctions.power(a,b)
        >>> print(t.val)
        8
        >>> print(t.der['a'])
        12
        >>> np.isclose(t.der['b'], 5.545177444479562)
        True
        >>> np.isclose(t.der2['a'], 0)
        True
        >>> np.isclose(t.der2['b'], 3.843624111345611)
        True
        >>> np.isclose(t.der2['ab'], 8.317766166719343)
        True


        >>> a = AutoDiffObject.AutoDiff(4, 'a')
        >>> b = 2
        >>> t = ElementaryFunctions.power(a, b)
        >>> print(t.val)
        4.0
        >>> print(t.der['a'])
        4
        >>> print(t.der2['a'])
        2
        '''

        try:
            ##try to find if the passed in base and power object is autodiff object and do
            ##proper operation to the passed in object
            base_val = base.val
            other_der = {}
            other_der2 = {}
            try:
                ##When both the base and the power are autodiff objects
                if type(np.power(base.val, power.val)) == complex:
                    print ("base value should be positive, because we don't consider imaginary number here.")
                    raise ValueError

                base_value = np.power(base.val, power.val)
                base_der = set(base.der)
                power_der = set(power.der)

                if base.val <= 0:
                    print ("base value should be positive, because we don't consider imaginary number here.")
                    raise ValueError

                for key in base_der.union(power_der):
                    for key2 in base_der.union(power_der):
                        ## If the element exists in both base derivative and power derivatives
                        if key in base_der and key in power_der:
                            other_der[key] = np.power(base.val,power.val) * (power.val * 1/base.val * base.der[key] + np.log(base.val) * power.der[key])
                            if key2+key in other_der2.keys():
                                other_der2[key+key2] = other_der2[key2+key]
                            else:
                                if key == key2:
                                    other_der2[key] = np.power(base.val,power.val) * (power.der[key] * np.log(base.val) + power.val/base.val * base.der[key])**2 + np.power(base.val,power.val) * (power.der2[key] * np.log(base.val) + 2 * power.der[key] * 1/base.val * base.der[key] - power.val * 1/(base.val**2) * base.der[key]**2 + power.val/base.val * base.der2[key])
                                else:
                                    if key2 in base_der and key2 in power_der:
                                        other_der2[key+key2] = np.power(base.val,power.val) * (power.der[key2]*np.log(base.val) + power.val/base.val*base.der[key2]) * (power.der[key]*np.log(base.val) + power.val/base.val * base.der[key]) + np.power(base.val,power.val) * (power.der2[key+key2]*np.log(base.val) + 1/base.val * power.der[key] * base.der[key2] + power.der[key2] * 1/base.val * base.der[key] - power.val/(base.val**2)*base.der[key2]*base.der[key] + power.val/base.val * base.der2[key+key2])
                                    elif key2 in base_der:
                                        other_der2[key+key2] = np.power(base.val,power.val) * power.val/base.val * base.der[key2] * (power.der[key]*np.log(base.val) + power.val/base.val * base.der[key]) + np.power(base.val,power.val) * (1/base.val * power.der[key] * base.der[key2] + power.val/(base.val**2) * base.der[key2] * base.der[key] + power.val/base.val * base.der[key+key2])
                                    else:
                                        other_der[key+key2] = np.power(base.val,power.val) * power.der[key2] * np.log(base.val) * (power.der[key]*np.log(base.val) + power.val/base.val * base.der[key]) + np.power(base.val,power.val) * (power.der2[key+key2]*np.log(base.val) + power.der[key2]*1/base.val*base.der[key])
                        elif key in base_der:
                            other_der[key] = power.val * np.power(base.val,power.val) * base.der[key] * 1/base.val
                            if key2+key in other_der2.keys():
                                other_der2[key+key2] = other_der2[key2+key]
                            else:
                                if key == key2:
                                    other_der2[key] = np.power(base.val, power.val) * (power.val/base.val * base.der[key])**2 + np.power(base.val, power.val) * (-power.val * 1/(base.val**2) * base.der[key]**2 + power.val/base.val*base.der2[key])
                                else:
                                    if key2 in base_der and key2 in power_der:
                                        other_der2[key+key2] = np.power(base.val, power.val) * power.val/base.val * base.der[key] * (power.der[key2]*np.log(base.val) + power.val/base.val * base.der[key2]) + np.power(base.val, power.val) * (power.der[key2] * 1/base.val * base.der[key] + power.val/(base.val**2) * base.der[key] + power.val/base.val * base.der[key+key2])
                                    elif key2 in base_der:
                                        other_der2[key+key2] = np.power(base.val, power.val) * power.val**2 / base.val**2 * base.der[key] * base.der[key2] + np.power(base.val, power.val) * ((power.val/base.val**2) * base.der[key] * base.der[key2] + power.val/base.val * base.der2[key+key2])
                                    else:
                                        other_der2[key+key2] = np.power(base.val, power.val) * power.der[key2] * np.log(base.val) * (power.val/base.val * base.der[key]) + np.power(base.val, power.val) * power.der[key2] * 1/base.val * base.der[key]
                        else:
                            #other_der[key] = power.der[key] * np.log(base.val) * base_value
                            other_der[key] = np.power(base.val,power.val) * power.der[key] * np.log(base.val)
                            if key2+key in other_der2.keys():
                                other_der2[key+key2] = other_der2[key2+key]
                            else:
                                if key == key2:
                                    other_der2[key] = np.power(base.val, power.val) * (power.der[key]*np.log(base.val))**2 + np.power(base.val, power.val) * (power.der2[key]*np.log(base.val))
                                else:
                                    if key2 in base_der and key2 in power_der:
                                        other_der2[key+key2] = np.power(base.val,power.val) * (power.der[key2]*np.log(base.val) + power.val/base.val * base.der[key2]) * power.der[key] * np.log(base.val) + np.power(base.val,power.val) * (power.der2[key+key2]*np.log(base.val) + 1/base.val * power.der[key] * base.der[key2])
                                    elif key2 in base_der:
                                        other_der2[key+key2] = np.power(base.val,power.val) * power.val/base.val * base.der[key2] * power.der[key] * np.log(base.val) + np.power(base.val,power.val) * (1/base.val * power.der[key] * base.der[key2])
                                    else:
                                        other_der2[key+key2] = np.power(base.val,power.val) * (power.der[key2] * np.log(base.val) + power.val/base.val * base.der[key2])

                return AutoDiff(base_value, "dummy", other_der, other_der2)
            except:
                ##when base is autodiff object and power is not
                if type(np.power(base.val, power.real)) == complex:
                    print ("base value should be positive, because we don't consider imaginary number here.")
                    raise ValueError

                base_value = np.power(base_val, power)
                base_der = power * np.power(base_val, power-1)
                for key,derivative in base.der.items():
                    other_der[key] = base_der * derivative

                for key,derivative2 in base.der2.items():
                    if key in base.der.keys():
                        other_der2[key] = power * (power-1) * np.power(base.val,power-2) * base.der[key]**2 + power * np.power(base.val,power-1) * base.der2[key]
                    else:
                        key1 = key[0]
                        key2 = key[1]
                        other_der2[key] = power * (power-1) * np.power(base.val,power-2) * base.der[key1] * base.der[key2] + power * np.power(base.val,power-1) * base.der2[key]

                return AutoDiff(base_value, "dummy", other_der, other_der2)
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
                    other_der2 = {}
                    ##try to check if the passed in other object is numeric value
                    for key,derivative in power.der.items():
                        other_der[key] = power.der[key] * np.log(base) * np.power(base,power.val)
                    for key, derivative2 in power.der2.items():
                        if key in base.der.keys():
                            other_der2[key] = power.der[key] * np.log(base) * np.power(base,power.val) + power.der2[key] * np.log(base) * np.power(base,power.val)
                        else:
                            key1 = key[0]
                            key2 = key[1]
                            other_der2[key] = power.der[key2] * np.log(base) * np.power(base,power.val) + power.der[key] * power.der[key2] * np.log(base) * np.power(base,power.val)
                    return AutoDiff(np.power(base.val,power.val), "dummy", other_der, other_der2)
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
        >>> a = AutoDiffObject.AutoDiff(2, 'a')
        >>> b = AutoDiffObject.AutoDiff(3, 'b')
        >>> t = ElementaryFunctions.log(a*b)
        >>> np.isclose(t.val, 1.79175946923)
        True
        >>> np.isclose(t.der['a'],0.5)
        True
        >>> np.isclose(t.der['b'], 1/3)
        True
        >>> np.isclose(t.der2['a'], -0.25)
        True
        >>> np.isclose(t.der2['b'], -0.1111111111111111)
        True
        >>> np.isclose(t.der2['ab'], 0)
        True
        '''

        try:
            ##try to find if the passed in other object is autodiff object and do
            ##proper operation to the passed in object
            other_val = other.val

            if other_val <= 0:
                    print ("base value should be positive, because we don't consider imaginary number here.")
                    raise ValueError

            other_der = {}
            other_der2 = {}
            log_value, log_for_der = np.log(other_val), 1/float(other_val)

            ##First derivatives for log function
            for key,derivative in other.der.items():
                other_der[key] = log_for_der * derivative

            ##Second Derivatives for log functions
            for key, derivative2 in other.der2.items():
                # check if that key is in first derivative dictionary so we are taking second derivative w.r.t. one variable
                # i.e., f_xx --> key == x and x in first derivative dictionary
                if key in other.der.keys():
                    other_der2[key] = -1.0/other.val**2 * other.der[key] * other.der[key] + 1.0/other_val * other.der2[key]
                else:
                    # split the second derivative dictionary key into the two variables
                    first_var = key[0]
                    second_var = key[1]
                    other_der2[key] = -1.0/other.val**2 * other.der[first_var] * other.der[second_var] + 1.0/other_val * other.der2[key]

            return AutoDiff(log_value, "dummy", other_der,other_der2)

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
        >>> x = AutoDiff(2, 'x')
        >>> y = AutoDiff(3, 'y')
        >>> t = ElementaryFunctions.exp(x*y)
        >>> np.isclose(t.val, 403.428793493)
        True
        >>> np.isclose(t.der['x'], 1210.28638048)
        True
        >>> np.isclose(t.der['y'], 806.857586985)
        True
        >>> np.isclose(t.der2['x'], 3630.85914143)
        True
        >>> np.isclose(t.der2['y'], 1613.71517397)
        True
        >>> np.isclose(t.der2['xy'], 2824.00155445)
        True
        '''

        try:
            other_val = other.val
            other_der = {}
            other_der2 = {}
            exp_value, exp_for_der = np.exp(other_val), np.exp(other_val)
            ##First derivatives for log function
            for key,derivative in other.der.items():
                other_der[key] = exp_for_der * derivative

            ##Second Derivatives for log functions
            for key,derivative2 in other.der2.items():
                if key in other.der.keys():
                    other_der2[key] = exp_for_der * other.der[key] * other.der[key] + exp_for_der * other.der2[key]
                else:
                    # split the second derivative dictionary key into the two variables
                    first_var = key[0]
                    second_var = key[1]
                    other_der2[key] = exp_for_der * other.der[first_var] * other.der[second_var] + exp_for_der * other.der2[key]

            return AutoDiff(exp_value, "dummy", other_der, other_der2)
        except:
            try:
                ##try to check if the passed in other object is numeric value
                other_value = other.real
                return np.exp(other_value)
            except:
                ##catch error if passed object is not numeric or autodiff
                print("illegal argument. Needs to be either autodiff object or numeric value")
                raise AttributeError

    @staticmethod
    def sqrt(other):
        ''' Returns the another AutoDiff object or numeric value after
        performing square root operation on the input

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
        >>> x = AutoDiff(2, 'x')
        >>> y = AutoDiff(3, 'y')
        >>> t = ElementaryFunctions.sqrt(x*y)
        >>> np.isclose(t.val, 2.44948974278)
        True
        >>> np.isclose(t.der['x'], 0.61237243569579458)
        True
        >>> np.isclose(t.der['y'], 0.40824829046386307)
        True
        >>> np.isclose(t.der2['x'], -0.15309310892394862)
        True
        >>> np.isclose(t.der2['y'], -0.06804138174397717)
        True
        >>> np.isclose(t.der2['xy'], 0.10206207261596578)
        True
        '''
        try:
            ##try to find if the passed in other object is autodiff object and do
            ##proper operation to the passed in object
            other_val = other.val
            other_der = {}
            other_der2 = {}
            sqrt_value = np.sqrt(other.val)

            if other_val < 0 :
                print("unsupported input. Obect needs to have non-negative values")
                raise ValueError

            # first derivative
            for key,derivative in other.der.items():
                other_der[key] = 1.0/2 * 1.0/np.sqrt(other.val) * other.der[key]

            # second derivative
            # loop through all keys in second derivative dictionary
            for key, derivative2 in other.der2.items():
                # check if that key is in first derivative dictionary so we are taking second derivative w.r.t. one variable
                # i.e., f_xx --> key == x and x in first derivative dictionary
                if key in other.der.keys():
                    other_der2[key] = -1.0/4 * 1.0/other.val**(3.0/2) * other.der[key]**2 + 1.0/2 * 1.0/np.sqrt(other.val) * other.der2[key]
                else:
                    # split the second derivative dictionary key into the two variables
                    key1 = key[0]
                    key2 = key[1]
                    other_der2[key] = -1.0/4 * 1.0/other.val**(3.0/2) * other.der[key1] * other.der[key2] + 1.0/2 * 1.0/np.sqrt(other.val) * other.der2[key]

            return AutoDiff(sqrt_value, "dummy", other_der, other_der2)

        except:
            try:
                ##try to check if the passed in other object is numeric value
                other_value = other.real
                return np.sqrt(other_value)
            except:
                ##catch error if passed object is not numeric or autodiff
                print("illegal argument. Needs to be either autodiff object or numeric value")
                raise AttributeError

    @staticmethod
    def logit(other):
        ''' Returns the another AutoDiff object or numeric value after
        performing square root operation on the input

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
        >>> x = AutoDiff(2, 'x')
        >>> y = AutoDiff(3, 'y')
        >>> t = ElementaryFunctions.sqrt(x*y)
        >>> np.isclose(t.val, 0.880797077978)
        True
        >>> np.isclose(t.der['x'], 0.104993585404)
        True
        >>> np.isclose(t.der2['x'], -0.0799625010562)
        True
        '''
        try:
            ##try to find if the passed in other object is autodiff object and do
            ##proper operation to the passed in object
            other_val = other.val
            other_der = {}
            other_der2 = {}
            sqrt_value = np.exp(other.val) / (1 + np.exp(other.val))

            if other_val < 0 :
                print("unsupported input. Obect needs to have non-negative values")
                raise ValueError

            # first derivative
            for key,derivative in other.der.items():
                other_der[key] = np.exp(other.val) * other.der[key] / (1 + np.exp(other.val))**2

            # second derivative
            # loop through all keys in second derivative dictionary
            for key, derivative2 in other.der2.items():
                # check if that key is in first derivative dictionary so we are taking second derivative w.r.t. one variable
                # i.e., f_xx --> key == x and x in first derivative dictionary
                if key in other.der.keys():
                    other_der2[key] = (np.exp(other.val)*other.der[key]**2 + np.exp(other.val)*other.der2[key])/(1+np.exp(other.val))**2 - 2 * np.exp(other.val)**2 * other.der[key]**2 / (1 + np.exp(other.val))**3
                    # other_der2[key] = (np.exp(other.val) * other.der[key] + np.exp(other.val)*other.der2[key] + np.exp(other.val)**2 * other.der[key] + np.exp(other.val)**2 *other.der2[key] - np.exp(other.val)**2 * other.der[key]**2) / (1 + np.exp(other.val))**3
                else:
                    # split the second derivative dictionary key into the two variables
                    key1 = key[0]
                    key2 = key[1]
                    other_der2[key] = (np.exp(other.val)*other.der[key1]*other.der[key2] + np.exp(other.val)*other.der2[key1+key2])/(1+np.exp(other.val))**2 - 2 * np.exp(other.val)**2 * other.der[key1]* other.der[key2] / (1 + np.exp(other.val))**3

            return AutoDiff(sqrt_value, "dummy", other_der, other_der2)

        except:
            try:
                ##try to check if the passed in other object is numeric value
                other_value = other.real
                return np.exp(other_value)
            except:
                ##catch error if passed object is not numeric or autodiff
                print("illegal argument. Needs to be either autodiff object or numeric value")
                raise AttributeError


    @staticmethod
    def arcsin(other):

        '''
        Returns the another AutoDiff object or numeric value after
        performing the arcsine operation on the input
        RETURNS
        ========
        A new instance of AutoDiff object or numeric value
        NOTES
        =====
        PRE:
             - EITHER: another instance of AutoDiff class
                 OR: float
             - Value must be in [-1, 1]
        POST:
             - Return a new Autodiff class instance or a numeric value
        EXAMPLES
        =========
        >>> g = ElementaryFunctions.arcsin(1)
        >>> np.isclose(g.val, np.pi/2)
        True
        >>> a = AutoDiff(0.4, 'a')
        >>> b = AutoDiff(0.5, 'b')
        >>> f = ElementaryFunctions.arcsin(a*a*b*b)
        >>> np.isclose(f.val, 0.04001067)
        True
        >>> np.isclose(f.der['a'], 0.2001602)
        True
        >>> np.isclose(f.der['b'], 0.1601282)
        True
        >>> np.isclose(f.der2['a'], 0.5020005)
        True
        >>> np.isclose(f.der2['b'], 0.3212803)
        True
        >>> np.isclose(f.der2['ab'], 0.8019208)
        True
        '''

        if abs(other.val) > 1:
            raise ValueError("Value must be in [-1, 1]")

        try:
            ##try to find if the passed in other object is autodiff object and do
            ##proper operation to the passed in object
            other_val = other.val
            other_der = {}
            other_der2 = {}
            arcsin_value = np.arcsin(other_val)

            # first derivative
            for key,derivative in other.der.items():
                other_der[key] = derivative / np.sqrt(1 - other_val**2)

            # second derivative
            # loop through all keys in second derivative dictionary
            for key, derivative2 in other.der2.items():
                # check if that key is in first derivative dictionary so we are taking second derivative w.r.t. one variable
                # i.e., f_xx --> key == x and x in first derivative dictionary
                if key in other.der.keys():
                    other_der2[key] = (other.der2[key]/np.sqrt(1-other_val**2)) + (other.der[key]*other.der[key]*other_val/((1-other_val**2)**(3/2)))
                else:
                    # split the second derivative dictionary key into the two variables
                    first_var = key[0]
                    second_var = key[1]
                    other_der2[key] = (other.der2[key]*np.sqrt(1-other_val**2) + (other.der[first_var]*other.der[second_var]*other_val/np.sqrt(1-other_val**2)))/(1-other_val**2)

            return AutoDiff(arcsin_value, "dummy", other_der, other_der2)

        except:
            try:
                ##try to check if the passed in other object is numeric value
                other_value = other.real
                return np.arcsin(other_value)
            except:
                ##catch error if passed object is not numeric or autodiff
                print("illegal argument. Needs to be either autodiff object or numeric value")
                raise AttributeError

    @staticmethod
    def arccos(other):

        '''
        Returns the another AutoDiff object or numeric value after
        performing the arccosine operation on the input
        RETURNS
        ========
        A new instance of AutoDiff object or numeric value
        NOTES
        =====
        PRE:
             - EITHER: another instance of AutoDiff class
                 OR: float
             - Value must be in [-1, 1]
        POST:
             - Return a new Autodiff class instance or a numeric value
        EXAMPLES
        =========
        >>> g = ElementaryFunctions.arccos(0)
        >>> np.isclose(g.val, np.pi/2)
        True
        >>> a = AutoDiff(0.1, 'a')
        >>> b = AutoDiff(0.8, 'b')
        >>> f = ElementaryFunctions.arccos(a*a*b*b)
        >>> np.isclose(f.val, 1.564396)
        True
        >>> np.isclose(f.der['a'], -0.1280026)
        True
        >>> np.isclose(f.der['b'], -0.01600033)
        True
        >>> np.isclose(f.der2['a'], -1.280131)
        True
        >>> np.isclose(f.der2['b'], -0.02000205)
        True
        >>> np.isclose(f.der2['ab'], -0.3200197)
        True
        '''

        if abs(other.val) > 1:
            raise ValueError("Value must be in [-1, 1]")

        try:
            ##try to find if the passed in other object is autodiff object and do
            ##proper operation to the passed in object
            other_val = other.val
            other_der = {}
            other_der2 = {}
            arccos_value = np.arccos(other_val)

            # first derivative
            for key,derivative in other.der.items():
                other_der[key] = (-1*derivative) / np.sqrt(1 - other_val**2)

            # second derivative
            # loop through all keys in second derivative dictionary
            for key, derivative2 in other.der2.items():
                # check if that key is in first derivative dictionary so we are taking second derivative w.r.t. one variable
                # i.e., f_xx --> key == x and x in first derivative dictionary
                if key in other.der.keys():
                    other_der2[key] = (-1*other.der2[key]/np.sqrt(1-other_val**2)) - (other.der[key]*other.der[key]*other_val/((1-other_val**2)**(3/2)))
                else:
                    # split the second derivative dictionary key into the two variables
                    first_var = key[0]
                    second_var = key[1]
                    other_der2[key] = (-1*other.der2[key]*np.sqrt(1-other_val**2) - (other.der[first_var]*other.der[second_var]*other_val/np.sqrt(1-other_val**2)))/(1-other_val**2)

            return AutoDiff(arccos_value, "dummy", other_der, other_der2)

        except:
            try:
                ##try to check if the passed in other object is numeric value
                other_value = other.real
                return np.arccos(other_value)
            except:
                ##catch error if passed object is not numeric or autodiff
                print("illegal argument. Needs to be either autodiff object or numeric value")
                raise AttributeError

    @staticmethod
    def arctan(other):

        '''
        Returns the another AutoDiff object or numeric value after
        performing the arctangent operation on the input
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
        >>> g = ElementaryFunctions.arctan(1)
        >>> np.isclose(g.val, np.pi/4)
        True
        >>> a = AutoDiff(0.3, 'a')
        >>> b = AutoDiff(0.6, 'b')
        >>> f = ElementaryFunctions.arctan(a*a*b*b)
        >>> np.isclose(f.val, 0.03238867)
        True
        >>> np.isclose(f.der['a'], 0.2032113)
        True
        >>> np.isclose(f.der['b'], 0.1016057)
        True
        >>> np.isclose(f.der2['a'], 0.7162248)
        True
        >>> np.isclose(f.der2['b'], 0.1790562)
        True
        >>> np.isclose(f.der2['ab'], 0.7177349)
        True
        '''

        try:
            ##try to find if the passed in other object is autodiff object and do
            ##proper operation to the passed in object
            other_val = other.val
            other_der = {}
            other_der2 = {}
            arctan_value = np.arctan(other_val)

            # first derivative
            for key,derivative in other.der.items():
                other_der[key] = other.der[key] / (1 + other_val**2)

            # second derivative
            # loop through all keys in second derivative dictionary
            for key, derivative2 in other.der2.items():
                # check if that key is in first derivative dictionary so we are taking second derivative w.r.t. one variable
                # i.e., f_xx --> key == x and x in first derivative dictionary
                if key in other.der.keys():
                    other_der2[key] = (other.der2[key]/(1+other_val**2)) - (2*other.der[key]*other.der[key]*other_val)/((1+other_val**2)**2)
                else:
                    # split the second derivative dictionary key into the two variables
                    first_var = key[0]
                    second_var = key[1]
                    other_der2[key] = (other.der2[key]/(1+other_val**2)) - (2*other.der[first_var]*other.der[second_var]*other_val)/((1+other_val**2)**2)

            return AutoDiff(arctan_value, "dummy", other_der, other_der2)

        except:
            try:
                ##try to check if the passed in other object is numeric value
                other_value = other.real
                return np.arctan(other_value)
            except:
                ##catch error if passed object is not numeric or autodiff
                print("illegal argument. Needs to be either autodiff object or numeric value")
                raise AttributeError

if __name__ == "__main__":
    x = AutoDiff(2, "x")
    y = AutoDiff(3, "y")
    z = AutoDiff(4, "z")

    # f = 5*x + ElementaryFunctions.tan(7*x*y)
    # print(f.val, f.der)
    #
    # f2 = ElementaryFunctions.log((x*y))
    # print(f2.val, f2.der, f2.der2)
    #
    # f3 = ElementaryFunctions.power(x,2)
    # print(f3.val, f3.der, f3.der2)
    #
    # f4 = ElementaryFunctions.exp(x*y)
    # print(f4.val, f4.der, f4.der2)

    # f5 = ElementaryFunctions.power(x*y,x*y)
    # print(f5.val, f5.der, f5.der2)
    #
    # f6 = ElementaryFunctions.sqrt(x*y)
    # print(f6.val, f6.der, f6.der2)

    # f7 = ElementaryFunctions.logit(x)
    # print(f7.val, f7.der, f7.der2)


#    f6 = ElementaryFunctions.sin("thirty")
#    print(f6.val, f6.der)

    f = ElementaryFunctions.tan(x*x*y*y)
    print(f.val, f.der, f.der2)