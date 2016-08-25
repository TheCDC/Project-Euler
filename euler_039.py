def test(a,b,c):
	return a**2 + b**2 == c**2

def num_solutions(n):
	ns = 0
	for a in range(1,n+1):
		for b in range(1,a):
			c = n-a-b
			if test(a, b, c):
				ns += 1
	return ns

testn = num_solutions(120)
print(testn)
assert num_solutions(120) == 3

biggest = num_solutions(1000)
for i in range(1000,0,-2):
	a = num_solutions(i)
	if a > biggest:
		print("New biggest:",a,"at i =",i)
		biggest = a
print(a,i)
# ss = [num_solutions(i) for i in range(1000,0,-1)]
