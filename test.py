a = 2000
b = 21
print(f"a = {a}")
print(f"b = {b}")
print(f"a + b = {a + b}")

# ad19
a = 10

if a>1:
	
	for i in range(2, (a//2)+1):
		
		if a % i == 0:
			print(a, "is not prime ")
			break
			
		else:
			print(a, "is prime ")
else:
	print(a, "is not prime ")
