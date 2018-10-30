##This class is used to define the behavior of elementary functions
import math
import AutoDiffObject as autodiff

class ElementaryFunctions():
    def __init__(self):

    def sin(self,other):
        try:
            ##try to find if the passed in other object is autodiff object and do
            ##proper operation to the passed in object
            other_val, other_der = other.val, other.der
            sin_value,cos_for_der = math.sin(other_val), math.cos(other_val)
            for key,derivative in other_der.items():
                other.der[key] = cos_for_der * derivative
            return autodiff(sin_value, other_der)

        except:
            try:
                ##try to check if the passed in other object is numeric value
                other_value = float(other)
                return math.sin(other_value)
            except:
                ##catch error if passed object is not numeric or autodiff
                print("illegal argument. Needs to be either autodiff object or numeric value")
                raise AttributeError
               
            
       #(Version 2 below by Kay,10302018)---------------------------------------------------------
          
    def sin(other):
        try:
            ##try to find if the passed in other object is autodiff object and do
            ##proper operation to the passed in object
            other_val = other.val
            other_der = {}       #! Here, we need a new dict, as if let other_der = other.der, 
                                 #it is actually a pointer that would change other.der during calculation as well
            sin_value,cos_for_der = math.sin(other_val), math.cos(other_val)
            for key,derivative in other.der.items():          #Here, loop through other.der
                other_der[key] = cos_for_der * derivative     #and build up other_der 
            return autodiff.AutoDiff(sin_value, "dummy", other_der)    #pass in other_der as updated der information

        except:
            try:
                ##try to check if the passed in other object is numeric value
                other_value = float(other)
                return math.sin(other_value)
            except:
                ##catch error if passed object is not numeric or autodiff
                print("illegal argument. Needs to be either autodiff object or numeric value")
                raise AttributeError
                
         #-------------------------------------------------------------------------------------------       
                

    def cos(self,other):
        try:
            ##try to find if the passed in other object is autodiff object and do
            ##proper operation to the passed in object
            other_val, other_der = other.val, other.der
            cos_value,sin_for_der = math.cos(other_val), -math.sin(other_val)
            for key,derivative in other_der.items():
                other.der[key] = sin_for_der * derivative
            return autodiff(cos_value, other_der)

        except:
            try:
                ##try to check if the passed in other object is numeric value
                other_value = float(other)
                return math.cos(other_value)
            except:
                ##catch error if passed object is not numeric or autodiff
                print("illegal argument. Needs to be either autodiff object or numeric value")
                raise AttributeError

    def tan(self,other):
        try:
            ##try to find if the passed in other object is autodiff object and do
            ##proper operation to the passed in object
            other_val, other_der = other.val, other.der
            tan_value, tan_for_der = math.tan(other_val), 1/(math.cos(x)**2)
            for key,derivative in other_der.items():
                other.der[key] = tan_for_der * derivative
            return autodiff(tan_value, other_der)

        except:
            try:
                ##try to check if the passed in other object is numeric value
                other_value = float(other)
                return math.tan(other_value)
            except:
                ##catch error if passed object is not numeric or autodiff
                print("illegal argument. Needs to be either autodiff object or numeric value")
                raise AttributeError

    def power(self,base,power):
    def log(self,other):
    def exp(self,other):
