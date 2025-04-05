class Value:
    def __init__(self, assigned: bool, name: str):
        self.value: bool = assigned
        self.name: str = name
    
    def print(self):
        return (self.name + ":" + str(self.value))
    

    def evaluate(self):
        return self.value
    

class And(Value):
    def __init__ (self, *args):
        self.values = list()
        for val in args:
            self.values.append(val)
        Value.__init__(self ,False, "AND")

    def print(self):
        outstring = "("
        i: int = 0
        for val in self.values:
            outstring += val.print()
            if(i != len(self.values) - 1):
                outstring += " * "
            i += 1
        outstring += ")"
        return outstring

    def evaluate(self):
        ret_val: bool = True
        for val in self.values:
            ret_val &= val.evaluate()
            #optimization
            if (ret_val == False):
                break
        self.value = ret_val
        return self.value
    
class Or(Value):
    def __init__ (self, *args):
        self.values = list()
        for val in args:
            self.values.append(val)
        Value.__init__(self, False, "OR")

    def print(self):
        outstring = "("
        i: int = 0
        for val in self.values:
            outstring += val.print()
            if(i != len(self.values) - 1):
                outstring += " + "
            i += 1
        outstring += ")"
        return outstring

    def evaluate(self):
        ret_val: bool = False
        for val in self.values:
            ret_val |= val.evaluate()
            #optimization
            if (ret_val == True):
                break
        self.value = ret_val
        return self.value
    
class Not(Value):
    def __init__(self, val):
        self.wrappedVal = val
        self.value = not val.evaluate()
        self.name = "not"

    def print(self):
        outputstring = "NOT ("
        outputstring += self.wrappedVal.print()
        outputstring += ")"
        return outputstring

    def evaluate(self):
        return not self.wrappedVal.evaluate()
    
class Impl(Value):
    def __init__(self, vall, valr):
        self.lvalue = vall
        self.rvalue = valr
        self.value = False
        self.name = "Impl"
    
    def evaluate(self):
        ret_vall = self.lvalue.evaluate()
        ret_valr = self.rvalue.evaluate()

        if (ret_vall == True):
            if (ret_valr == True):
                return True
            else:
                return False
        else:
            return True
    
    def print(self):
        outputstr = "("
        outputstr += self.lvalue.print()
        outputstr += " => "
        outputstr += self.rvalue.print()
        outputstr += ")"
        return outputstr


#Test

a = Not(Value(False,"a"))
b = Not(Value(False, "b"))
c = Not(Value(False, "c"))
testone =Impl(And(a, b, c), Not(Value(False, "d")))
print(testone.print())
print(str(testone.evaluate()))
