import a
def main():
	while True:
		try:
			module = input("What module to install? ")
		except KeyboardInterrupt: continue
		except EOFError: quit()
		if module == "".split(): continue
		else: break
	a.install(module)
	a.run("<stdin>", f"run(\"{a.filename}\")")
	while True:
		try:
			text = input("aragonite:argnm > ")
		except KeyboardInterrupt: print("\nTo exit shell type 'exit()'"); continue
		except EOFError: break
		if text.strip() == "": continue
		result, error = a.run('<stdin>', text)
		if error:
			print(error.as_string())
		elif result:
			if len(result.elements) == 1:
				print(repr(result.elements[0]))
			else:
				print(repr(result))
if __name__ == "__main__":
	main()
