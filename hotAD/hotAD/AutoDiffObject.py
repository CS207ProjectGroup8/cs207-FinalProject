import numbers

class AutoDiff():

    ''' Create objects that return the value and partial derivatives of desired functions. Additionally,
    the second partial derivatives can also be returned.

    INSTANCE VARIABLES
    =======
    - val: numeric type, value of the variable to be evaluated a

    - varName: string,
             either created when the user is creating the AutoDiff
             object at the beginning, eg, x = AutoDiff(3, "x");
             or as "dummy" in function operations

    - *args: read in args[0], which is a dictionary of derivative(s);
            eg. {"x":1, "y":2} means partial derivative with respect to x is 1 and
            partial derivative with respect to y is 2;
            Only situation that *args present is in the output of methods'
            implementation return.

            If Hessian switch is on (H=True specified when instantiating the AD object),
            then read in args[1], which is a dictionary of second partial derivatives;
            e.g. {"x": 1, "y": 2, "xy":3} means the second partial derivative of the
            function with respect to x is 1, with respect to y is 2, and with respect
            to x and y is 3.

    EXAMPLE:
        EITHER: (created at the beginning by user)
            To calculate first partial derivatives:
            x = AutoDiff(3, "x")
            To also calculate second partial derivatives:
            x = AutoDiff(3, "x", H = True)

        OR: (in method implementation)
            def...:
                .....
                return AutoDiff(x0*y0, "dummy", {"x":aa, "y":bb})
    '''

    def __init__(self, val, varName, *args, H = False):

        if isinstance(val, numbers.Real):
            self.val = val
        else:
            raise TypeError ("Please enter an integer or a float for the value of the AutoDiff object.")

        if isinstance(varName,str):
            if varName.isalnum():
                self.varName = varName
            else:
                raise TypeError("Please enter a alphanumeric char for the name of the AutoDiff object.")

        else:
            raise TypeError("Please enter a character for the name of the AutoDiff object.")

        if H in [True, False]:
            self.H = H
        else:
            raise TypeError ("Please enter a truth value for including the Hessian.")

        if varName != "dummy":
            if len(varName) == 1:
                self.der = {varName:1}
                if H == True:
                    self.der2 = {varName:0}
            else:
                raise TypeError("Please enter a single character as the variable name.")

        else:
            self.der = args[0]
            if H == True:
                self.der2 = args[1]

    def __eq__(self, other):

        '''Returns the truth value of two objects being equal
        RETURNS
        ========
        Truth value of two AD objects being equal in value and derivatives.

        PRE:
             - Current instance of AutoDiff class
             - EITHER: another instance of AutoDiff class
                 OR: float

        POST:
             - Truth value of equal value and derivative

        EXAMPLES
        =========
        >>> z = AutoDiff(1,'x')
        >>> a = AutoDiff(1,'x')
        >>> z == a
        True

        >>> l = AutoDiff(2,'z')
        >>> m = AutoDiff(2,'x')
        >>> l == m
        False

        '''
        if self.H == True:
            if isinstance(other, AutoDiff):
                return self.val == other.val and self.der == other.der and self.der2 == other.der2
        else:
            if isinstance(other,AutoDiff):
                return self.val == other.val and self.der == other.der
        return False

    def __neq__(self, other):
        return not self.__eq__(other)


    def __neg__(self):

        ''' Returns another AutoDiff object which is the negative of the instance of the complex class.
            This is a special method.

        RETURNS
        ========
        AutoDiff object with negative value and negative derivative of the current instance.
        If Hessian of the current instance has been specified, then the negative second derivatives are also returned.

        NOTES
        =====
        PRE:
             - Current instance of AutoDiff class
        POST:
             - Returns a new Autodiff class instance
        EXAMPLES
        =========
        >>> x = AutoDiff(1,'x')
        >>> t = -x
        >>> print(t.val, t.der)
        -1 {'x': -1}

        >>> y = AutoDiff(2, 'y', H = True)
        >>> r = -y
        >>> print(r.val, r.der, r.der2)
        -2 {'y': -1} {'y': 0}
        '''

        derDict = {}      #Create a new dictionary to store updated derivative(s) information
        der2Dict = {}
        setSelfDer = set(self.der)      #give a set of keys, eg. set({x:1, y:2}) = set('x', 'y')
        # Store negatives of each partial derivative
        for key in setSelfDer:
            derDict[key] = -self.der[key]
            if self.H == True:
                der2Dict[key] = -self.der2[key]

        if self.H == True:
            return AutoDiff(-1* self.val, "dummy", derDict, der2Dict, H = True)
        else:
            return AutoDiff(-1* self.val, "dummy", derDict, der2Dict, H = False)

    def __mul__(self, other):

        ''' Returns the another AutoDiff object which is the product of current AutoDiff object
            and another object (either AutoDiff object or float) separated by '*'.
            This is a special method.

        RETURNS
        ========
        A new instance of AutoDiff object
        NOTES
        =====
        PRE:
             - Current instance of AutoDiff class
             - EITHER: another instance of AutoDiff class
               OR: float

        POST:
             - Return a new Autodiff class instance
        EXAMPLES
        =========
        >>> a = AutoDiff(1, 'a')
        >>> b = AutoDiff(2, 'b')
        >>> t = a * b
        >>> print(t.val)
        2
        >>> print(t.der['a'])
        2
        >>> print(t.der['b'])
        1

        >>> a = AutoDiff(1, 'a')
        >>> b = 33
        >>> t = a * b
        >>> print(t.val, t.der)
        33 {'a': 33}


        >>> a = AutoDiff(3, 'a', H=True)
        >>> b = AutoDiff(2, 'b',H=True)
        >>> t = a * a * b * b
        >>> print(t.val)
        36
        >>> print(t.der['a'])
        24
        >>> print(t.der2['a'])
        8
        '''

        if isinstance(other, AutoDiff):
            derDict = {}      #Create a new dictionary to store updated derivative(s) information
            der2Dict = {}

            setSelfDer = set(self.der)      #give a set of keys, eg. set({x:1, y:2}) = set('x', 'y')
            setOtherDer = set(other.der)     #give a set of keys, eg. set({y:1, z:2}) = set('y', 'z')

            #look through element in the Union set:eg from above would be {'x', 'y', 'z'}
            for key in setSelfDer.union(setOtherDer):
                for key2 in setSelfDer.union(setOtherDer):

                    # Both derivative dicts have partial derivative info for this variable
                    if key in setSelfDer and key in setOtherDer:
                        derDict[key] = self.der[key] * other.val + self.val * other.der[key]

                        if self.H == True:
                            if key2+key in der2Dict:
                                der2Dict[key + key2] = der2Dict[key2 + key]
                            else:
                                if key2 == key:
                                    der2Dict[key] = self.der2[key] *other.val + \
                                                    2*other.der[key]*self.der[key] +\
                                                    self.val*other.der2[key]
                                else:
                                    if key2 in setSelfDer and key2 in setOtherDer:
                                        der2Dict[key+key2] = self.der2[key+key2]*other.val + \
                                                             self.der[key]*other.der[key2]+ \
                                                             self.der[key2]*other.der[key]+ \
                                                             self.val*other.der2[key+key2]
                                    elif key2 in setSelfDer:
                                        der2Dict[key+key2] = self.der2[key+key2]*other.val + \
                                                             self.der[key2]*other.der[key]
                                    else:
                                        der2Dict[key+key2] = self.der[key]*other.der[key2]+ \
                                                             self.val*other.der2[key +key2]

                    #if only one of them have the partial derivative info for the variable
                    elif key in setSelfDer:
                        derDict[key] = self.der[key]*other.val

                        if self.H == True:

                            if key2+key in der2Dict:
                                der2Dict[key + key2] = der2Dict[key2 + key]
                            else:
                                if key2 == key:
                                    der2Dict[key] = self.der2[key]*other.val
                                else:
                                    if key2 in setSelfDer and key2 in setOtherDer:
                                        der2Dict[key+key2] = self.der2[key+key2]*other.val + \
                                                             self.der[key]*other.der[key2]
                                    elif key2 in setSelfDer:
                                        der2Dict[key+key2] = self.der2[key+key2]*other.val
                                    else:
                                        der2Dict[key+key2] = self.der[key]*other.der[key2]

                    else: #key in other
                        derDict[key] = other.der[key]*self.val

                        if self.H == True:
                            if key2+key in der2Dict:
                                der2Dict[key + key2] = der2Dict[key2 + key]
                            else:
                                if key2 == key:
                                    der2Dict[key] = other.der2[key]*self.val
                                else:
                                    if key2 in setSelfDer and key2 in setOtherDer:
                                        der2Dict[key+key2] = other.der2[key+key2]*self.val + \
                                                             other.der[key]*self.der[key2]
                                    elif key2 in setSelfDer:
                                        der2Dict[key+key2] = other.der[key]*self.der[key2]
                                    else:
                                        der2Dict[key+key2] = other.der2[key + key2]*self.val

            if self.H == True:
                return AutoDiff(self.val * other.val, "dummy", derDict, der2Dict, H = True)
            else:
                return AutoDiff(self.val * other.val, "dummy", derDict, der2Dict, H = False)

        else:
            try:
                derDict = {}
                der2Dict = {}
                for key in self.der:
                    derDict[key] = other.real * self.der[key]
                if self.H == True:
                    for key in self.der2:
                        der2Dict[key] = other.real * self.der2[key]
                    return AutoDiff(self.val * other.real, "dummy", derDict, der2Dict, H = True)
                else:
                    return AutoDiff(self.val * other.real, "dummy", derDict, der2Dict, H = False)

            except:
                raise AttributeError("Illegal argument. Needs to be either autodiff object or numeric value.")


    __rmul__ = __mul__


    def __truediv__(self,other):

        ''' Returns the another AutoDiff object which is the current AutoDiff object
            divided by another object (either AutoDiff object or float) separated by '/'.
            This is a special method.

        RETURNS
        ========
        A new instance of AutoDiff object

        NOTES
        =====
        PRE:
             - Current instance of AutoDiff class
             - EITHER: another instance of AutoDiff class
                 OR: float

        POST:
             - Return a new Autodiff class instance

        EXAMPLES
        =========
        >>> a = AutoDiff(1, 'a')
        >>> b = AutoDiff(2, 'b')
        >>> t = a / b
        >>> print(t.val)
        0.5
        >>> print(t.der['a'])
        0.5
        >>> print(t.der['b'])
        -0.25

        >>> a = AutoDiff(1, 'a')
        >>> b = 5
        >>> t = a / b
        >>> print(t.val, t.der)
        0.2 {'a': 0.2}

        >>> a = AutoDiff(1, 'a', H=True)
        >>> b = AutoDiff(2, 'b', H=True)
        >>> t = a / (b)
        >>> print(t.val)
        0.5
        >>> print(t.der['a'])
        0.5
        >>> print(t.der['b'])
        -0.25
        >>> print(t.der2['b'])
        0.25

        >>> a = AutoDiff(1, 'a', H=True)
        >>> b = 5
        >>> t = a / b
        >>> print(t.val, t.der, t.der2)
        0.2 {'a': 0.2} {'a': 0.0}

        '''

        try:

            derDict = {}
            der2Dict = {}

            setSelfDer = set(self.der)      #give a set of keys, eg. set({x:1, y:2}) = set('x', 'y')
            setOtherDer = set(other.der)     #give a set of keys, eg. set({y:1, z:2}) = set('y', 'z')

            #look through element in the Union set:eg from above would be {'x', 'y', 'z'}
            for key in setSelfDer.union(setOtherDer):
                for key2 in setSelfDer.union(setOtherDer):

                    if key in setSelfDer and key in setOtherDer:
                        derDict[key] = (self.der[key] * other.val - self.val * other.der[key])/(other.val * other.val)

                        if self.H == True:
                            if key2+key in der2Dict:
                                der2Dict[key+key2] = der2Dict[key2+key]
                            else:
                                if key2 == key:
                                    der2Dict[key] = self.der2[key]/other.val - \
                                            (self.val * other.der2[key]/other.val**2) - \
                                            (2 * self.der[key] * other.der[key]/other.val**2) + \
                                            (2 * (other.der[key]**2) * self.val/other.val**3)

                                else:
                                    if key2 in setSelfDer and key2 in setOtherDer:
                                        der2Dict[key+key2] = self.der2[key+key2]/other.val - \
                                                (self.der[key] * other.der[key2])/(other.val**2) - \
                                                (other.der2[key+key2] * self.val)/(other.val**2) - \
                                                (other.der[key] * self.der[key2]/(other.val **2)) + \
                                                (2 * other.der[key] * other.der[key2] * self.val)/(other.val**3)


                                    elif key2 in setSelfDer:
                                        der2Dict[key+key2] = self.der2[key+key2]/other.val - \
                                                (other.der[key] * self.der[key2]/(other.val **2))

                                    elif key2 in setOtherDer:
                                        der2Dict[key+key2] = 2*other.der[key]*other.der[key2] * self.val / other.val ** 3 -\
                                                self.der[key] * other.der[key2]/other.val**2 -\
                                                self.val * other.der2[key+key2]/other.val**2


                    elif key in setSelfDer:
                        derDict[key] = (self.der[key] )/(other.val)

                        if self.H == True:
                            if key2+key in der2Dict:
                                der2Dict[key + key2] = der2Dict[key2 + key]
                            else:
                                if key2 == key :
                                    der2Dict[key] = self.der2[key]/other.val
                                else:
                                    if key2 in setSelfDer and key2 in setOtherDer:
                                        der2Dict[key+key2] = (self.der2[key+key2]/other.val) - \
                                                (other.der[key2]*self.der[key])/(other.val**2)
                                    elif key2 in setSelfDer:
                                        der2Dict[key+key2] = self.der2[key+key2]/(other.val)
                                    else:
                                        der2Dict[key+key2] = -other.der[key2] * self.der[key] / (other.val**2)

                    elif key in setOtherDer:
                        derDict[key] = (-1*self.val * other.der[key])/(other.val*other.val)

                        if self.H == True:
                            if key2+key in der2Dict:
                                der2Dict[key + key2] = der2Dict[key2 + key]
                            else:
                                if key2 == key:
                                    der2Dict[key] = -self.val*other.der2[key]/other.val**2 + \
                                            2*self.val*(other.der[key]**2)/other.val**3
                                else:
                                    if key2 in setSelfDer and key2 in setOtherDer:
                                        der2Dict[key+key2] = - self.der[key2] * other.der[key] / other.val**2 - \
                                                other.der2[key+key2] * self.val / other.val**2 + \
                                                2 * other.der[key] * other.der[key2] * self.val/other.val**3
                                    elif key2 in setSelfDer:
                                        der2Dict[key+key2] = (-other.der[key] * self.der[key2]) / (other.val**2)
                                    else:
                                        der2Dict[key+key2] = (-self.val*other.der2[key+key2]) / (other.val**2) + \
                                                2*other.der[key]*other.der[key2]*self.val/(other.val**3)
            if self.H == True:
                return AutoDiff(self.val/other.val, "dummy", derDict, der2Dict, H = True)
            else:
                return AutoDiff(self.val/other.val, "dummy", derDict, der2Dict, H = False)

        except ZeroDivisionError as err:
            raise ZeroDivisionError("Denominator cannot have value 0.")

        except:
            try:
                derDict = {}
                der2Dict = {}
                for key in self.der:
                    derDict[key] = (1/other.real) * self.der[key]

                if self.H == True:
                    for key in self.der2:
                        der2Dict[key] = (1/other.real) * self.der2[key]
                    return AutoDiff(self.val/other.real, "dummy", derDict, der2Dict, H = True)
                else:
                    return AutoDiff(self.val/other.real, "dummy", derDict, der2Dict, H = False)

            except ZeroDivisionError as err:
                raise ZeroDivisionError("Denominator cann ot have value 0.")

            except:
                raise AttributeError("Illegal argument. Needs to be either autodiff object or numeric value.")

    def __rtruediv__(self,other):

        ''' Returns the another AutoDiff object which is the current AutoDiff object
            divided by another object (either AutoDiff object or float) separated by '/'.
            This is a special method.

        RETURNS
        ========
        A new instance of AutoDiff object

        NOTES
        =====
        PRE:
             - Current instance of AutoDiff class
             - EITHER: another instance of AutoDiff class
                 OR: float

        POST:
             - Return a new Autodiff class instance
        EXAMPLES
        =========

        >>> a = AutoDiff(1, 'a', H=True)
        >>> b = 5
        >>> t = b / a
        >>> print(t.val, t.der,t.der2)
        5.0 {'a': -5.0} {'a': 10.0}

        '''

        try:

            derDict = {}
            der2Dict = {}

            setSelfDer = set(self.der)           #give a set of keys, eg. set({x:1, y:2}) = set('x', 'y')
            setOtherDer = set(other.der)         #give a set of keys, eg. set({y:1, z:2}) = set('y', 'z')

            for key in setSelfDer.union(setOtherDer):
                for key2 in setSelfDer.union(setOtherDer):

                    if key in setSelfDer and key in setOtherDer:
                        derDict[key] = (self.val * other.der[key] - self.der[key] * other.val)/(self.val * self.val)

                        if self.H == True:
                            if key2+key in der2Dict:
                                der2Dict[key+key2] = der2Dict[key2+key]
                            else:
                                if key2 == key:
                                    der2Dict[key] = other.der2[key]/self.val - \
                                                    (self.der2[key]*other.val/self.val**2) - \
                                                    (2*other.der[key] * self.der[key]/self.val**2) + \
                                                    (2 * other.val * self.der[key] * self.der[key] / self.val ** 3)
                                else:
                                    if key2 in setSelfDer and key2 in setOtherDer:
                                        der2Dict[key+key2] = other.der2[key+key2] / self.val - \
                                                             (other.val * self.der2[key+key2]) / self.val**2 - \
                                                             (self.der[key] * other.der[key2] / self.val**2) - \
                                                             (other.der[key] * self.der[key2] / self.val**2) + \
                                                             (2*other.val *self.der[key] * self.der[key2]/self.val**3)

                                    elif key2 in setSelfDer:
                                        der2Dict[key+key2] = (- other.val * self.der2[key+key2]) / self.val ** 2 - \
                                                             (other.der[key] * self.der[key2] / self.val ** 2) + \
                                                             (2*self.der[key] * self.der[key2] * other.val / self.val ** 3)
                                    else:
                                        der2Dict[key+key2] = other.der2[key+key2]/self.val - \
                                                             (self.der[key] * other.der[key2] / self.val ** 2)


                    elif key in setSelfDer:
                        derDict[key] = (- self.der[key] * other.val) / self.val**2

                        if self.H == True:
                            if key2+key in list(der2Dict.keys()):
                                der2Dict[key+key2] = der2Dict[key2+key]

                            else:
                                if key2 == key:
                                    der2Dict[key] = - other.val * self.der2[key] / self.val ** 2 + \
                                                    2 * other.val * (self.der[key] ** 2)/self.val ** 3
                                else:
                                    if key2 in setSelfDer and key2 in setOtherDer:
                                        der2Dict[key+key2] = 2 * other.val * self.der[key] * self.der[key2]/self.val ** 3 -\
                                                            other.der[key2] * self.der[key]/self.val**2 - \
                                                            other.val * self.der2[key+key2]/self.val**2
                                    elif key2 in setSelfDer:
                                        der2Dict[key+key2] = 2 * other.val * self.der[key] * self.der[key2]/self.val ** 3 -\
                                                            other.val * self.der2[key+key2]/self.val**2
                                    else:
                                        der2Dict[key+key2] = -other.der[key2] * self.der[key]/self.val**2


                    elif key in setOtherDer:
                        derDict[key] = other.der[key]/self.val

                        if self.H == True:
                            if key2+key in list(der2Dict.keys()):
                                der2Dict[key+key2] = der2Dict[key2+key]
                            else:
                                if key2 == key:
                                    der2Dict[key] = other.der2[key]/self.val
                                else:
                                    if key2 in setSelfDer and key2 in setOtherDer:
                                        der2Dict[key+key2] = other.der2[key+key2]/self.val -\
                                                             other.der[key]*self.der[key2]/self.val**2

                                    elif key2 in setSelfDer:
                                        der2Dict[key+key2] =  - other.der[key]*self.der[key2]/self.val**2

                                    elif key2 in setOtherDer:
                                        der2Dict[key+key2] = other.der2[key+key2]/self.val

            if self.H == True:
                return AutoDiff(other.val/self.val, "dummy", derDict, der2Dict, H = True)
            else:
                return AutoDiff(other.val/self.val, "dummy", derDict, der2Dict, H = False)

        except ZeroDivisionError as err:
            raise ZeroDivisionError("Denominator cann ot have value 0.")

        except:
            try:
                derDict = {}
                der2Dict = {}
                for key in self.der:
                    for key2 in self.der:

                        derDict[key] = (1/(self.val * self.val)) * (-1 * other.real * self.der[key])

                        if self.H == True:
                            if key == key2:
                                der2Dict[key] = -other.real*((self.der2[key]*self.val - 2*self.der[key]**2)/self.val**3)
                            else:
                                der2Dict[key+key2] = - other.real * self.der2[key+key2] / self.val**2 + \
                                                2* other.real * self.der[key] * self.der[key2]/self.val**3
                if self.H == True:
                    return AutoDiff(other.real/self.val, "dummy", derDict, der2Dict, H = True)
                else:
                    return AutoDiff(other.real/self.val, "dummy", derDict, der2Dict, H = False)

            except ZeroDivisionError as err:
                raise ZeroDivisionError("Denominator cann ot have value 0.")

            except:
                raise AttributeError("Illegal argument. Needs to be either autodiff object or numeric value.")


    def __add__(self, other):

        ''' Returns the another AutoDiff object which is the sum of current AutoDiff object
            and another object (either AutoDiff object or float) separated by '+'.
            This is a special method.
        RETURNS
        ========
        A new instance of AutoDiff object
        NOTES
        =====
        PRE:
             - Current instance of AutoDiff class
             - EITHER: another instance of AutoDiff class
                 OR: float
        POST:
             - Return a new Autodiff class instance
        EXAMPLES
        =========
        >>> a = AutoDiff(1, 'a')
        >>> b = AutoDiff(2, 'b')
        >>> t = a + b
        >>> print(t.val)
        3
        >>> print(t.der['a'])
        1
        >>> print(t.der['b'])
        1
        >>> a = AutoDiff(1, 'a')
        >>> b = 33
        >>> t = a + b
        >>> print(t.val, t.der)
        34 {'a': 1}
        '''

        try:
        #if isinstance(other, AutoDiff):
            derDict = {}
            der2Dict = {}
            setSelfDer = set(self.der)
            setOtherDer = set(other.der)

            for key in setSelfDer.union(setOtherDer):
                for key2 in setSelfDer.union(setOtherDer):

                    if key in setSelfDer and key in setOtherDer:
                        derDict[key] = self.der[key] + other.der[key]

                        if self.H == True:
                            if key2+key in list(der2Dict.keys()):
                                der2Dict[key + key2] = der2Dict[key2 + key]
                            else:
                                if key2 == key:

                                    der2Dict[key] = self.der2[key] + other.der2[key]
                                else:

                                    if key2 in setSelfDer and key2 in setOtherDer:
                                        der2Dict[key+key2] = self.der2[key+key2] + other.der2[key+key2]

                                    elif key2 in setSelfDer:
                                        der2Dict[key+key2] = self.der2[key+key2]

                                    else:
                                        der2Dict[key+key2] = other.der2[key+key2]

                    elif key in setSelfDer:
                        derDict[key] = self.der[key]

                        if self.H == True:
                            if key2+key in list(der2Dict.keys()):
                                der2Dict[key + key2] = der2Dict[key2 + key]
                            else:
                                if key2 == key:
                                    der2Dict[key] = self.der2[key]
                                else:
                                    if key2 in setSelfDer and key2 in setOtherDer:
                                        der2Dict[key+key2] = self.der2[key+key2]

                                    elif key2 in setSelfDer:
                                        der2Dict[key+key2] = self.der2[key+key2]

                                    else:
                                        der2Dict[key+key2] = 0


                    else:
                        derDict[key] = other.der[key]

                        if self.H == True:
                            if key2+key in list(der2Dict.keys()):
                                der2Dict[key + key2] = der2Dict[key2 + key]
                            else:
                                if key2 == key:
                                    der2Dict[key] = other.der2[key]
                                else:
                                    if key2 in setSelfDer and key2 in setOtherDer:
                                        der2Dict[key+key2] = other.der2[key+key2]

                                    elif key2 in setSelfDer:
                                        der2Dict[key+key2] = 0

                                    else:
                                        der2Dict[key+key2] = other.der2[key+key2]
            if self.H == True:
                return AutoDiff(self.val + other.val, "dummy", derDict, der2Dict, H = True)
            else:
                return AutoDiff(self.val + other.val, "dummy", derDict, der2Dict, H = False)
        except:
            try:
                if self.H == True:
                    return AutoDiff(self.val + other.real, "dummy", self.der, self.der2, H = True)
                else:
                    return AutoDiff(self.val + other.real, "dummy", self.der, H = False)
            except:
                raise AttributeError("Illegal argument. Needs to be either autodiff object or numeric value.")


    __radd__ = __add__

    def __sub__(self,other):

        ''' Returns the another AutoDiff object which is the difference of current AutoDiff object
            and another object (either AutoDiff object or float) separated by '-'.
            This is a special method.
        RETURNS
        ========
        A new instance of AutoDiff object
        NOTES
        =====
        PRE:
             - Current instance of AutoDiff class
             - EITHER: another instance of AutoDiff class
                 OR: float
        POST:
             - Return a new Autodiff class instance
        EXAMPLES
        =========
        >>> x = AutoDiff(1, 'x')
        >>> y = AutoDiff(2, 'y')
        >>> t = x - y
        >>> print(t.val)
        -1
        >>> print(t.der['x'])
        1
        >>> print(t.der['y'])
        -1
        >>> a = AutoDiff(1, 'a')
        >>> b = 33
        >>> t = a - b
        >>> print(t.val, t.der)
        -32 {'a': 1}

        >>> a = AutoDiff(4, 'a', H=True)
        >>> b = AutoDiff(2, 'b', H = True)
        >>> t = a - b
        >>> print(t.val)
        2
        >>> print(t.der['a'])
        1
        >>> print(t.der['b'])
        -1
        >>> print(t.der2['a'])
        0
        >>> print(t.der2['b'])
        0
        >>> print(t.der2['b'])
        0

        >>> a = AutoDiff(1, 'a', H=True)
        >>> b = 33
        >>> t = a - b
        >>> print(t.val, t.der, t.der2)
        -32 {'a': 1} {'a': 0}
        '''

        try:
        #if isinstance(other, AutoDiff):
            derDict = {}
            der2Dict = {}
            setSelfDer = set(self.der)
            setOtherDer = set(other.der)

            for key in setSelfDer.union(setOtherDer):
                for key2 in setSelfDer.union(setOtherDer):

                    if key in setSelfDer and key in setOtherDer:
                        derDict[key] = self.der[key] - other.der[key]

                        if self.H == True:
                            if key2+key in list(der2Dict.keys()):
                                der2Dict[key + key2] = der2Dict[key2 + key]
                            else:
                                if key2 == key:
                                    der2Dict[key] = self.der2[key] - other.der2[key]
                                else:
                                    if key2 in setSelfDer and key2 in setOtherDer:
                                        der2Dict[key+key2] = self.der2[key+key2] - other.der2[key+key2]

                                    elif key2 in setSelfDer:
                                        der2Dict[key+key2] = self.der2[key+key2]

                                    else:
                                        der2Dict[key+key2] = -other.der2[key+key2]


                    elif key in setSelfDer:
                        derDict[key] = self.der[key]

                        if self.H == True:
                            if key2+key in list(der2Dict.keys()):
                                der2Dict[key + key2] = der2Dict[key2 + key]
                            else:
                                if key2 == key:
                                    der2Dict[key] = self.der2[key]
                                else:
                                    if key2 in setSelfDer and key2 in setOtherDer:
                                        der2Dict[key+key2] = self.der2[key+key2]

                                    elif key2 in setSelfDer:
                                        der2Dict[key+key2] = self.der2[key+key2]

                                    else:
                                        der2Dict[key+key2] = 0

                    else:
                        derDict[key] = -1 * other.der[key]

                        if self.H == True:
                            if key2+key in list(der2Dict.keys()):
                                der2Dict[key + key2] = der2Dict[key2 + key]
                            else:
                                if key2 == key:
                                    der2Dict[key] = -1 * other.der2[key]
                                else:
                                    if key2 in setSelfDer and key2 in setOtherDer:
                                        der2Dict[key+key2] = -other.der2[key+key2]

                                    elif key2 in setSelfDer:
                                        der2Dict[key+key2] = 0

                                    else:
                                        der2Dict[key+key2] = -other.der2[key+key2]

            if self.H == True:
                return AutoDiff(self.val - other.val, "dummy", derDict, der2Dict, H = True)
            else:
                return AutoDiff(self.val - other.val, "dummy", derDict, der2Dict, H = False)

        except:
            try:
                if self.H == True:
                    return AutoDiff(self.val - other.real, "dummy", self.der, self.der2, H = True)
                else:
                    return AutoDiff(self.val - other.real, "dummy", self.der, H = False)
            except:
                raise AttributeError("Illegal argument. Needs to be either autodiff object or numeric value.")


    __rsub__ = __sub__