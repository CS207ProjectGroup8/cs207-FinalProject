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
        else:
            self.der = args[0]

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
        setSelfDer = set(self.der)      #give a set of keys, eg. set({x:1, y:2}) = set('x', 'y')
        # Store negatives of each partial derivative
        for key in setSelfDer:
            derDict[key] = -self.der[key]

        return AutoDiff(-1* self.val, "dummy", derDict)

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

        try:
        #if isinstance(other, AutoDiff):
            derDict = {}      #Create a new dictionary to store updated derivative(s) information
            setSelfDer = set(self.der)      #give a set of keys, eg. set({x:1, y:2}) = set('x', 'y')
            setOtherDer = set(other.der)     #give a set of keys, eg. set({y:1, z:2}) = set('y', 'z')

            #look through element in the Union set:eg from above would be {'x', 'y', 'z'}
            for key in setSelfDer.union(setOtherDer):

                #if both derivative dictionaries have the partial derivative info for this variable
                if key in setSelfDer and key in setOtherDer:
                    derDict[key] = self.der[key]*other.val + other.der[key]*self.val

                #if only one of them have the partial derivative info for the variable
                elif key in setSelfDer:
                    derDict[key] = self.der[key]*other.val
                else:
                    derDict[key] = other.der[key]*self.val

            return AutoDiff(self.val * other.val, "dummy", derDict)

        except:
            try:
                derDict = {}
                for key in self.der:
                    derDict[key] = other.real * self.der[key]
                return AutoDiff(self.val * other.real, "dummy", derDict)
            except:
                print("illegal argument. Needs to be either autodiff object or numeric value.")
                raise AttributeError


    __rmul__ = __mul__


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
            setSelfDer = set(self.der)
            setOtherDer = set(other.der)

            for key in setSelfDer.union(setOtherDer):
                if key in setSelfDer and key in setOtherDer:
                    derDict[key] = self.der[key] + other.der[key]
                elif key in setSelfDer:
                    derDict[key] = self.der[key]
                else:
                    derDict[key] = other.der[key]

            return AutoDiff(self.val + other.val, "dummy", derDict)
        except:
            try:
                return AutoDiff(self.val + other.real, "dummy", self.der)
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
            setSelfDer = set(self.der)
            setOtherDer = set(other.der)

            for key in setSelfDer.union(setOtherDer):
                if key in setSelfDer and key in setOtherDer:
                    derDict[key] = self.der[key] - other.der[key]
                elif key in setSelfDer:
                    derDict[key] = self.der[key]
                else:
                    derDict[key] = -1 * other.der[key]

            return AutoDiff(self.val - other.val, "dummy", derDict)

        except:
            try:
                return AutoDiff(self.val - other.real, "dummy", self.der)
            except:
                print("illegal argument. Needs to be either autodiff object or numeric value.")
                raise AttributeError


    __rsub__ = __sub__

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
            setSelfDer = set(self.der)
            setOtherDer = set(other.der)

            for key in setSelfDer.union(setOtherDer):
                if key in setSelfDer and key in setOtherDer:
                    derDict[key] = (self.der[key] * other.val - self.val * other.der[key])/(other.val * other.val)
                elif key in setSelfDer:
                    derDict[key] = (self.der[key] * other.val)/(other.val*other.val)
                elif key in setOtherDer:
                    derDict[key] = (-1*self.val * other.der[key])/(other.val*other.val)
            return AutoDiff(self.val/other.val, "dummy", derDict)

        except:
            try:
                derDict = {}
                if other.real == 0:
                    raise ZeroDivisionError
                for key in self.der:
                    derDict[key] = (1/other.real) * self.der[key]

                return AutoDiff(self.val/other.real, "dummy", derDict)
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
            setSelfDer = set(self.der)
            setOtherDer = set(other.der)

            for key in setSelfDer.union(setOtherDer):
                if key in setSelfDer and key in setOtherDer:
                    derDict[key] = (self.val * other.der[key] - self.der[key] * other.val)/(self.val * self.val)
                elif key in setOtherDer:
                    derDict[key] = (self.val * other.der[key])/(self.val * self.val)
                elif key in setSelfDer:
                    derDict[key] = (- self.der[key] * other.val)/(self.val * self.val)

            return AutoDiff(other.val/self.val, "dummy", derDict)

        except:
            try:
                if self.val == 0:
                    raise ZeroDivisionError
                derDict = {}
                for key in self.der:
                    derDict[key] = (1/(self.val * self.val)) * (-1 * other.real * self.der[key])
                return AutoDiff(other.real/self.val, "dummy", derDict)
            except:
                print("illegal argument. Needs to be either autodiff object or numeric value.")
                raise AttributeError






if __name__ == "__main__":

    x = AutoDiff(2, "x")
    y = AutoDiff(3, "y")
    z = AutoDiff(4, "z")


    f = 5*x - 7*y + x*y*z*4 + 3.0*z + 4
    print(f.val, f.der)

    g = -x*y*z
    print(g.val, g.der)

    h = z/2
    print(h.val, h.der)

    p = 2/z
    print(p.val, p.der)


    m = -x
    print(m.val, m.der)


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
