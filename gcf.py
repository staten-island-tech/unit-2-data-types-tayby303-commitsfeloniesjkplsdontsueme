num1=int(input("Number 1: "))
num2=int(input("Number 2: "))
def gcf(a,b):
  smaller=min(a,b)
  for i in (smaller,0,-1):
    if a%i==0 and b%i==0:
     return i
    return 1
print(gcf(num1,num2))