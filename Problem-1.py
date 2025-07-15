# Problem-1:   Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
#   Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
#   Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string


class calculator :

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def calculate (self,type):
        self.type = type

        if type=="Addition":
            return self.a + self.b

        elif type =="Subtraction":
            return self.a - self.b

        elif type =="Multiplication" :
            return self.a * self.b

        elif type =="Division" :
            if self.b !=0:
                return self.a / self.b
            else:
                return "Error: Division by Zero Error"
            
        else:
            return "Enter proper operation"

a= float(input("Enter first number: "))

b= float(input("Enter Second number: "))

op = str(input("Enter type of Operation (Addition,Subtraction,Multiplication,Division): "))

calc= calculator(a,b)

result = calc.calculate(op)

print("Result: ", result)

