
class AutoDiff():
    def __init__(self, val, varName, *args):
        '''
        INPUT:
            val: numeric type, value of the variable to be evaluated at
            varName: string,
                     either created when the user is creating the AutoDiff
                     object at the beginning, eg, x = AutoDiff(3, "x");
                     or as "dummy" in function operations
            *args: only read in args[0], which is a dictionary of derivative(s);
                    eg. {"x":1, "y":2} means partial derivative of x and
                    partial derivative of y;
                    Only situation that *args present is in the output of methods'
                    implementation return
        EXAMPLE:
            EITHER: (created at the beginning by user)
                x = AutoDiff(3, "x")
            OR: (in method implementation)
                def...:
                    .....
                    return AutoDiff(x0*y0, "dummy", {"x":aa, "y":bb})
        '''
        self.val = val
        self.varName = varName
        if varName != "dummy":
            self.der = {varName:1}
        else:
            self.der = args[0]
    
    def __neg__(self):
        derDict = {}      #Create a new dictionary to store updated derivative(s) information
        setSelfDer = set(self.der)      #give a set of keys, eg. set({x:1, y:2}) = set('x', 'y')
        # Store negatives of each partial derivative
        for key in setSelfDer:
            derDict[key] = -self.der[key]
            
        return AutoDiff(-1* self.val, "dummy", derDict)

    def __mul__(self, other):
        try:
        #if isinstance(other, AutoDiffToy):
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

        except AttributeError:
        #elif isinstance(other, (int,float, etc numeric types)):
            derDict = {}
            for key in self.der:
                derDict[key] = other.real * self.der[key]
            return AutoDiff(self.val * other.real, "dummy", derDict)


    __rmul__ = __mul__


    def __add__(self, other):
        try:
        #if isinstance(other, AutoDiffToy):
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

        except AttributeError:
        #elif isinstance(other, (int,float, etc numeric types)):
            return AutoDiff(self.val + other.real, "dummy", self.der)

    __radd__ = __add__
    
    def __sub__(self,other):
        try:
        #if isinstance(other, AutoDiffToy):
            derDict = {}
            setSelfDer = set(self.der)
            setOtherDer = set(other.der)

            for key in setSelfDer.union(setOtherDer):
                if key in setSelfDer and key in setOtherDer:
                    derDict[key] = self.der[key] - other.der[key]
                elif key in setSelfDer:
                    derDict[key] = self.der[key]
                else:
                    derDict[key] = other.der[key]

            return AutoDiff(self.val - other.val, "dummy", derDict)

        except AttributeError:
        #elif isinstance(other, (int,float, etc numeric types)):
            return AutoDiff(self.val - other.real, "dummy", self.der)

    __rsub__ = __sub__


if __name__ == "__main__":


    x = AutoDiff(2, "x")
    y = AutoDiff(3, "y")
    z = AutoDiff(4, "z")


    f = 5*x - 7*y + x*y*z*4 + 3.0*z + 4
    print(f.val, f.der)
    
    g = -x*y*z
    print(g.val, g.der)

        

#test = {'x': 53, 'z': 27.0, 'y': 39}
#test.keys
#set(test)
#test1 = {}
#for i in set(test):
#    print (i)
#    test1[i] = -test[i]
#test1


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
