'''
calculate bmi- body mass index
book, page 16, problem 112
Answer: 1128/49 = 23.020

'''

print('Are you healthy? Welcome to the BMI calculator')
weight= input('Enter your weight: ')
height = input('Enter your height: ')

weight = int(weight)
height = int(height)
bmi = (705*weight)/height**2
bmi = int(bmi)
print('Your bmi is: ', bmi)

'''
to continue program
display you are healthy if your bmi is wihin the range
18.5 and 24.9
'''


