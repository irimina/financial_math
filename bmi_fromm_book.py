'''
calculate bmi- body mass index
book, page 16, problem 112
Answer: 1128/49 = 23.020

'''

print('Are you healthy? Welcome to the BMI calculator')
weight= int(input('Enter your weight: '))
height = int(input('Enter your height: '))

bmi = (705*weight)/height**2
bmi = int(bmi)
print('Your bmi is: ', bmi)

'''
to continue program
display you are healthy if your bmi is wihin the range
18.5 and 24.9
'''


