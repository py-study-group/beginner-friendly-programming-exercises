a = 10
b = 20
print('Initially')
print("a =",a,",","b =",b,'\n')
temp=a
a=b
b=temp
print("After interchanging")
print("a =",a,",","b =",b,'\n')



print('Another method')
a = 10
b = 20
a = a + b
b = a - b
a = a - b
print("a =",a,",",'b =',b,'\n')


print('Yet another method')
a = a ^ b
b = b ^ a
a = a ^ b
print('a =',a,',','b  =',b)