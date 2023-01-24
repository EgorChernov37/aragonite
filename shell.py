import os
try:
	import a
except Expection as e:
	print(e)
while True:
	text = input('shell > ')
	if text.strip() == "": continue
	result, error = a.run('<stdin>', text)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))
			print(repr(result))