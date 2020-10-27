#Дебильный калькулятор
a = float(input('Enter first number:'))
b = float(input('Enter second number:'))
c = input('Choose you`r action:')

#Actions: +, -, *, /, **, %.
try:
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
		print('Error!')
except ZeroDivisionError:
	print('Division by 0')
except SyntaxError:
	print('Yor code is wrong')
else:
	print('All alright!')