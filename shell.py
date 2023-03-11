import os
try:
	import a
except Exception as e:
	print(e)
while True:
	try:
		text = input('shell > ')
	except KeyboardInterrupt:
		print("\nTo exit shell type 'exit()'")
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