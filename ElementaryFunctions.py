##This class is used to define the behavior of elementary functions
import math
import AutoDiffObject as autodiff

class ElementaryFunctions():
    def __init__(self):
        return

    def sin(self,other):
        try:
            ##try to find if the passed in other object is autodiff object and do
            ##proper operation to the passed in object
            other_val, other_varName = other.val, other.varName
            other_der = {}
            sin_value,cos_for_der = math.sin(other_val), math.cos(other_val)
            for key,derivative in other.der.items():
                other_der[key] = cos_for_der * derivative
            return autodiff.AutoDiff(sin_value, "dummy", other_der)
        except:
            try:
                ##try to check if the passed in other object is numeric value
                other_value = other.real
                return math.sin(other_value)
            except:
                ##catch error if passed object is not numeric or autodiff
                print("illegal argument. Needs to be either autodiff object or numeric value")
                raise AttributeError

    def cos(self,other):
        try:
            ##try to find if the passed in other object is autodiff object and do
            ##proper operation to the passed in object
            other_val, other_varName = other.val, other.varName
            other_der = {}
            cos_value,sin_for_der = math.cos(other_val), -math.sin(other_val)
            for key,derivative in other.der.items():
                other_der[key] = sin_for_der * derivative
            return autodiff.AutoDiff(cos_value, "dummy", other_der)
        except:
            try:
                ##try to check if the passed in other object is numeric value
                other_value = other.real
                return math.cos(other_value)
            except:
                ##catch error if passed object is not numeric or autodiff
                print("illegal argument. Needs to be either autodiff object or numeric value")
                raise AttributeError

    def tan(self,other):
        try:
            ##try to find if the passed in other object is autodiff object and do
            ##proper operation to the passed in object
            other_val= other.val
            other_der = {}
            tan_value, tan_for_der = math.tan(other_val), 1/(math.cos(other_val)**2)
            for key,derivative in other.der.items():
                other_der[key] = tan_for_der * derivative
            return autodiff.AutoDiff(tan_value, "dummy", other_der)

        except:
            try:
                ##try to check if the passed in other object is numeric value
                other_value = other.real
                return math.tan(other_value)
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
                power_val = power.val
                base_value = math.pow(base.val, power.val)
                base_der = set(base.der)
                power_der = set(power.der)
                for key in base_der.union(power_der):
                    if key in base_der and key in power_der:
                        other_der[key] = (power.der[key] * math.log(base.val) + power.val * (1/base.der[key])) * base_value
                    elif key in base_der:
                        other_der[key] = power.val * (1/base.der[key]) * base_value
                    else:
                        other_der[key] = power.der[key] * math.log(base.val) * base_value
                return autodiff.AutoDiff(base_value, "dummy", other_der)
            except:
                ##when base is autodiff object and power is not
                base_value = math.pow(base_val, power)
                base_der = power * math.pow(base_val, power-1)
                for key,derivative in base.der.items():
                    other_der[key] = base_der * derivative
                return autodiff.AutoDiff(base_value, "dummy", other_der)
        except:
            try:
                base_value = base.real
                try:
                    power_val = power.val
                    other_der = {}
                    ##try to check if the passed in other object is numeric value
                    for key,derivative in power.der.items():
                        other_der[key] = power.der[key] * math.log(base) * math.pow(base,power.val)
                    return autodiff.AutoDiff(math.pow(base.val,power.val), "dummy", other_der)
                except:
                    return math.pow(base,power)

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
            other_der = {}
            log_value, log_for_der = math.log(other_val), 1/float(other_val)
            for key,derivative in other.der.items():
                other_der[key] = log_for_der * derivative
            return autodiff.AutoDiff(log_value, "dummy", other_der)

        except:
            try:
                ##try to check if the passed in other object is numeric value
                other_value = other.real
                return math.log(other_value)
            except:
                ##catch error if passed object is not numeric or autodiff
                print("illegal argument. Needs to be either autodiff object or numeric value")
                raise AttributeError


    def exp(self,other):
        try:
            other_val = other.val
            other_der = {}
            exp_value, exp_for_der = math.exp(other_val), math.exp(other_val)
            for key,derivative in other.der.items():
                other_der[key] = exp_for_der * derivative
            return autodiff.AutoDiff(exp_value, "dummy", other_der)
        except:
            try:
                ##try to check if the passed in other object is numeric value
                other_value = other.real
                return math.exp(other_value)
            except:
                ##catch error if passed object is not numeric or autodiff
                print("illegal argument. Needs to be either autodiff object or numeric value")
                raise AttributeError



x = autodiff.AutoDiff(2, "x")
y = autodiff.AutoDiff(3, "y")
ef = ElementaryFunctions()

f = 5*x + ef.tan(7*x*y)
# f2 = ef.log((3*x))
f3 = 3*x
f4 = ef.power(x,y)

print(f4.val, f4.der)
