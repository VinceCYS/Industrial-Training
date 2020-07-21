#Chapter 5
#question 24
hbaromega = 2.48

for count in range(10):
	n = count + 1
	DeltaE = n*hbaromega
	print(n,DeltaE)
	

#question 16
from collections import Counter
mylist = []

for count in range(8):
	nx = count + 1    
	for count in range(8):
		ny = count + 1
		sumofn = nx**2 + ny**2
		if sumofn >= 50:
			#print("nx =",nx)
			#print("ny =",ny)
			#print("Sum of n =",sumofn)
			mylist.append(int(sumofn))

print(Counter(mylist))


#question 17
from collections import Counter
mylist = []

for count in range(6):
	nx = count + 1    
	for count in range(6):
		ny = count + 1
		sumofn = nx**2 + (ny**2)/4
		#print("nx =",nx)
		#print("ny =",ny)
		#print("Sum of n =",sumofn)
		mylist.append(float(sumofn))

print(Counter(mylist))