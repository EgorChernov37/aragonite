import os
try:
	import basic
except Expection as e:
	print(e)
print('x0: Everything alright.')
basic.run('<stdin>', 'run("classes.sh6c")')
while True:
	text = input('shell > ')
	if text.strip() == "": continue
	result, error = basic.run('<stdin>', text)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))
			print(repr(result))