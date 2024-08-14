#one.py


def func():
	print("FUNC() IN ONE.PY")


## All the files with indentation level zero will be executed
print('TOP LEVEL IN ONE.PY')

## Python has built in variable
## assigns main to name variable directly in background
## It Allows You to Execute Code When the File Runs as a Script, but Not When It’s Imported as a Module
if __name__ == '__main__':
	print('ONE.PY is being run directly')
else:
	print('ONE.PY has been imported')