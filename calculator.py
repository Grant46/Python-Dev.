class Calculator:
    def __init__(self,a,b):
        self.val1=a
        self.val2=b
    
    def sum(self):
        adzz=self.val1+self.val2
        print(adzz)
    
    def subtraction(self):
        sott=self.val1-self.val2
        print(sott)
    
    def division(self):
        div=self.val1/self.val2
        print(div)


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
call = Calculator(num1, num2)
print("1° sum\n2° subtraction\n3°division")
print("\nSelect Operator")
sel = input()
print("\n\n")

if(sel == '1'):
    call.sum()

elif(sel == '2'):
    call.subtraction()

elif(sel == '3'):
    call.division()

elif(call == '0'): 
    call.sum()
    call.subtraction()
    call.division()

else:
    print("ERROR :-(")
