print('Welcome to the inflation calculator')
print("Let's calculate the future value of a product.")

'''
There are 3 models of calculating interest of a product

#1
simple interest: I = p*r*t ( principal * rate* time)
To find the total: p+I or p*(1+r*t)

#2
compound interest
A=p(1+r/n)**(n*t)

#3
continuous compound
A= P*e**(r*t)

'''

p = input('Enter the initial amount: ')
p = int(p)

n = input('Enter the number of the times the interest is compounded yearly: ')
n= int(n)

t= input('Enter the number of years: ')
t= int(t)

r= input('Enter the rate of the compound in the form of a decimal number: ')
r= float(r)


a = p*(1+r/n)**(n*t)
a=int(a)

print('Your future amount is: ',a)



