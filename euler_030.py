from utils import numDigits, nthDigit
def ds(n):
	s = 0
	for i in range(numDigits(n)):
		s += nthDigit(n,i)**5
	# print(s)
	return s
def main():
	# find the upper bound
	i = 3
	while ds(i) <= i:
		i += 1
	print(ds(i))
if __name__ == '__main__':
	main()