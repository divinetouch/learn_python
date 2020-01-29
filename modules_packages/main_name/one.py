'''
one.py
'''

print('Indentation zero get run by default')

def func():
    print("func() in one.py")

# built in varaable
# when run directly like: python one.py
if __name__ == "__main__":
    print('Is being run directly')
else:
    print('one.py has been imported!')
