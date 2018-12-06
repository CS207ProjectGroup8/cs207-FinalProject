
import numbers

class AutoDiff():

    ''' Create objects that return the value and partial derivatives of desired functions
    INSTANCE VARIABLES
    =======
    - val: numeric type, value of the variable to be evaluated at
    - varName: string,
             either created when the user is creating the AutoDiff
             object at the beginning, eg, x = AutoDiff(3, "x");
             or as "dummy" in function operations
    - *args: only read in args[0], which is a dictionary of derivative(s);
            eg. {"x":1, "y":2} means partial derivative of x is 1 and
            partial derivative of y is 2;
            Only situation that *args present is 0in the output of methods'
            implementation return
    EXAMPLE:
        EITHER: (created at the beginning by user)
            x = AutoDiff(3, "x")
        OR: (in method implementation)
            def...:
                .....
                return AutoDiff(x0*y0, "dummy", {"x":aa, "y":bb})
    '''

    def __init__(self, val, varName, *args):

        if isinstance(val, numbers.Real):
            self.val = val
        else:
            raise TypeError ("Please enter an integer or a float for the value of the AutoDiff object.")

        if isinstance(varName, str):
            self.varName = varName
        else:
            raise TypeError("Please enter a string for the name of the AutoDiff object.")

        if varName != "dummy":
            self.der = {varName:1}
            self.der2 = {varName:0}
        else:
            self.der = args[0]
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
        >>> t = -z
        >>> print(t.val, t.der)
        -1 {'x': -1}
        
        '''
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
        AutoDiff object with negative value and negative derivative of the current instance
        NOTES
        =====
        PRE:
             - Current isnstance of AutoDiff class
        POST:
             - Return a new Autodiff class instance
        EXAMPLES
        =========
        >>> z = AutoDiff(1,'x')
        >>> t = -z
        >>> print(t.val, t.der)
        -1 {'x': -1}
        '''

        derDict = {}      #Create a new dictionary to store updated derivative(s) information
        der2Dict = {}
        setSelfDer = set(self.der)      #give a set of keys, eg. set({x:1, y:2}) = set('x', 'y')
        # Store negatives of each partial derivative
        for key in setSelfDer:
            derDict[key] = -self.der[key]
            der2Dict[key] = -self.der2[key]


        return AutoDiff(-1* self.val, "dummy", derDict, der2Dict)

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

            return AutoDiff(self.val * other.val, "dummy", derDict, der2Dict)

        else:
            try:
                derDict = {}
                der2Dict = {}
                for key in self.der:
                    derDict[key] = other.real * self.der[key]
                for key in self.der2:
                    der2Dict[key] = other.real * self.der2[key]
                return AutoDiff(self.val * other.real, "dummy", derDict, der2Dict)
            except:
                print("illegal argument. Needs to be either autodiff object or numeric value.")
                raise AttributeError


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

        '''

        try:
        #if isinstance(other, AutoDiff)
            if other.val == 0:
                raise ZeroDivisionError

            derDict = {}
            der2Dict = {}

            setSelfDer = set(self.der)      #give a set of keys, eg. set({x:1, y:2}) = set('x', 'y')
            setOtherDer = set(other.der)     #give a set of keys, eg. set({y:1, z:2}) = set('y', 'z')

            #look through element in the Union set:eg from above would be {'x', 'y', 'z'}
            for key in setSelfDer.union(setOtherDer):
                for key2 in setSelfDer.union(setOtherDer):

                    if key in setSelfDer and key in setOtherDer:
                        derDict[key] = (self.der[key] * other.val - self.val * other.der[key])/(other.val * other.val)

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
                                    der2Dict[key+key2] = 2*other.der[key] *other.der[key2] * self.val / other.val ** 3 -\
                                            self.der[key] * other.der[key2]/other.val**2 -\
                                            self.val * other.der2[key+key2]/other.val**2
                                            

                    elif key in setSelfDer:
                        derDict[key] = (self.der[key] )/(other.val)

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

                        der2Dict[key] = (self.der2[key]*other.val)/other.val**2


                    elif key in setOtherDer:
                        derDict[key] = (-1*self.val * other.der[key])/(other.val*other.val)

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

            return AutoDiff(self.val/other.val, "dummy", derDict, der2Dict)

        except:
            try:
                derDict = {}
                der2Dict = {}
                if other.real == 0:
                    raise ZeroDivisionError
                for key in self.der:
                    derDict[key] = (1/other.real) * self.der[key]
                for key in self.der2:
                    der2Dict[key] = (1/other.real) * self.der2[key]

                return AutoDiff(self.val/other.real, "dummy", derDict, der2Dict)
            except:
                print("illegal argument. Needs to be either autodiff object or numeric value.")
                raise AttributeError





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

        >>> a = AutoDiff(1, 'a')
        >>> b = 5
        >>> t = b / a
        >>> print(t.val, t.der)
        5.0 {'a': -5.0}

        '''

        try:
        #if isinstance(other, AutoDiff)
            if self.val == 0:
                raise ZeroDivisionError
            derDict = {}
            der2Dict = {}
            
            setSelfDer = set(self.der)           #give a set of keys, eg. set({x:1, y:2}) = set('x', 'y')
            setOtherDer = set(other.der)         #give a set of keys, eg. set({y:1, z:2}) = set('y', 'z')

            for key in setSelfDer.union(setOtherDer):
                for key2 in setSelfDer.union(setOtherDer):

                    if key in setSelfDer and key in setOtherDer:
                        derDict[key] = (self.val * other.der[key] - self.der[key] * other.val)/(self.val * self.val)
                    
                    
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
                                
#                        der2Dict[key] = -other.val*self.der2[key]/self.val**2 + \
#                                        2*other.val*self.der[key]**2/self.val**3
                    

                    elif key in setOtherDer:
                        derDict[key] = other.der[key]/self.val
                        
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
                                

            return AutoDiff(other.val/self.val, "dummy", derDict, der2Dict)

        except:
            try:
                if self.val == 0:
                    raise ZeroDivisionError
                derDict = {}
                der2Dict = {}
                for key in self.der:
                    for key2 in self.der:

                        derDict[key] = (1/(self.val * self.val)) * (-1 * other.real * self.der[key])
                        
                        if key == key2:
                            der2Dict[key] = -other.real*((self.der2[key]*self.val - 2*self.der[key]**2)/self.val**3)
                        else:
                            der2Dict[key+key2] = - other.real * self.der2[key+key2] / self.val**2 + \
                                            2* other.real * self.der[key] * self.der[key2]/self.val**3

                return AutoDiff(other.real/self.val, "dummy", derDict, der2Dict)
            except:
                print("illegal argument. Needs to be either autodiff object or numeric value.")
                raise AttributeError



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

            return AutoDiff(self.val + other.val, "dummy", derDict, der2Dict)
        
        except:
            try:
                return AutoDiff(self.val + other.real, "dummy", self.der, self.der2)
            except:
                print("illegal argument. Needs to be either autodiff object or numeric value.")
                raise AttributeError


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
        >>> a = AutoDiff(1, 'a')
        >>> b = AutoDiff(2, 'b')
        >>> t = a - b
        >>> print(t.val)
        -1
        >>> print(t.der['a'])
        1
        >>> print(t.der['b'])
        -1
        >>> a = AutoDiff(1, 'a')
        >>> b = 33
        >>> t = a - b
        >>> print(t.val, t.der)
        -32 {'a': 1}
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

            return AutoDiff(self.val - other.val, "dummy", derDict, der2Dict)

        except:
            try:
                return AutoDiff(self.val - other.real, "dummy", self.der, self.der2)
            except:
                print("illegal argument. Needs to be either autodiff object or numeric value.")
                raise AttributeError


    __rsub__ = __sub__


if __name__ == "__main__":

    x = AutoDiff(10, "x")
    y = AutoDiff(2, "y")
    z = AutoDiff(4, "z")

    h = 6/z  + x*3 - 9
    print(h.val, h.der, h.der2)
    
    print(x*99 == x*99)
    print(x*90 == x)

#    f = g + h
#    print(f.val, f.der, f.der2)    
#
    # g = -x*y*z
    # print(g.val, g.der, g.der2)

    # h = z/2
    # print(h.val, h.der)

    # p = 2/z
    # print(p.val, p.der)


    # m = -x
    # print(m.val, m.der)




'''
Notes
test = {"x":1, "y":2}
test2 = {"y":3, "z":4}
for key in test:
    print(test[key])
set1 = set(test)
set2 = set(test2)
new = {}
for key in set1.union(set2):
    if key in set1 and key in set2:
        new[key] = test[key] + test2[key]
    elif key in set1:
        new[key] = test[key]
    else:
        new[key] = test2[key]
new
'''
