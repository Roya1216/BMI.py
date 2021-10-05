print ('please enter your weight by Kg :')
print('weight : ')
w=float(input())
print('please enter your height by metre :')
print('height : ')
h=float(input())
b=round((w/h**2),1)
print('\n your bmi is ',b)


if b<18.5:
    print('you are under weight')
elif b>=18.5 and b<=24.9:
    print('you are normal')
elif b>24.9 and b <=29.9:
    print('you are over weight')
elif b>29.9 and b <=34.9:
    print('you are Obese')
elif b>34.9 :
    print('you are extremely Obese ')