import math
class Number(object):
	binary_List = []
	def __init__(self, num, bit):
			self.num = num
			self.bit = bit
	def numBin (self):
		while (self.num > 0):
			self.binary_List.append(self.num%2)
			self.num = self.num/2
		while (len(self.binary_List) < self.bit):
			self.binary_List.append(0)
		while (len(self.binary_List)>self.bit):
			self.binary_List.pop(len(self.binary_List)-1)
		if (len(self.binary_List)==self.bit and self.binary_List[len(self.binary_List)-1]==1):
			for i in range(4):
				self.binary_List.append(0)
	def reverseNum(self):
		self.binary_List.reverse()

class negative(Number):
	def __init__(self,num,bit):
		self.num = num*-1
		self.bit = bit
	def complement(self):
		self.numBin()
		for i in range(0,len(self.binary_List)):
			if self.binary_List[i] == 1:
				for x in range(i+1,len(self.binary_List)):
					if self.binary_List[x] == 0:
						self.binary_List[x] = 1
					else:
						self.binary_List[x] = 0
				break
				
def PosOrNeg(binary,nbit): #works
	if(binary[0]=="1"):
		return -1*(pow(2,nbit)-int(binary,2))
	
	else: 
		return int(binary,2)


nbit = input("Enter an nbit representation for a binary number in signed 2's representation ")
binarystring1 = raw_input("Enter an n digit binary number in signed 2's representation ")
x = PosOrNeg(binarystring1,nbit)
binarystring2 = raw_input("Enter another n digit binary number in signed 2's representation ")
operation = raw_input("Would you like to add or subtract(+/-) ")
if operation == "-":
	y = pow(2,nbit)-int(binarystring2,2)

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










