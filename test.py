#Дебильный калькулятор
a = float(input('Enter first number:'))
b = float(input('Enter second number:'))
c = input('Choose you`r action:')

#Actions: +, -, *, /, **, %.

	if c == '+':
		d = a + b;
		print(d)
	elif c == '-':
		d = a - b;
		print(d)
	elif c == '*':
		d = a * b;
		print(d)
	elif c == '/':
		d = a / b;
		print(d)
	elif c == '**':
		d = a ** b;
		print(d)	
	else:
		print('ERROR!')


input()