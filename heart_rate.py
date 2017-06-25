'''
Calculate your heart rate,
college alg and trig, page 16, problem 111
'''


welcome = input('this program calculates your heart rate. Hit Enter/return to continue ')

cool_t = input('Enter the number of minutes after the start of the cool-down period ')
cool_t = int(cool_t)

heart_rate = 65 + 53/(4*cool_t+1)
heart_rate = int(heart_rate)
#round(heart_rate)
print('Your heart rate is',heart_rate)





     
