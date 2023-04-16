import readline
try:
	import a
	from a import ver
except Exception as e:
	print(e)
while True:
	try:
		if 'ver' in locals():
			text = input(f'aragonite:{ver["version"]} > ')
		else:
			text = input(f'aragonite > ')
	except KeyboardInterrupt:
		print("\nTo exit shell type 'exit()'")
		continue
	except EOFError:
		break
	if text.strip() == "": continue
	result, error = a.run('<stdin>', text)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))
