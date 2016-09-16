import math
from numbers import Number, negative

nbit = input("Enter an nbit representation for a binary number in signed 2's representation ")
binarystring1 = raw_input("Enter an n digit binary number in signed 2's representation ")

x = PosOrNeg(binarystring1,nbit)

binarystring2 = raw_input("Enter another n digit binary number in signed 2's representation ")
operation = raw_input("Would you like to add or subtract(+/-) ")

if operation == "-":
	y = pow(2,nbit)-int(binarystring2,2)s
else:
	y =PosOrNeg(binarystring2,nbit)

if (x + y < 0):
	z1 = negative(x+y,nbit)
	z1.complement()
	z1.reverseNum()
else:
	z1 = Number(x+y,nbit)
	z1.numBin()
	z1.reverseNum()

print ''.join(str(e) for e in z1.binary_List)
