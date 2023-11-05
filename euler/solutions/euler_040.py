def how_many_n_digit(n):
    return (10**n)-(10**(n-1))
def digit_length_of_all_ndigits(n):
    return how_many_n_digit(n)*n
def get_upper_bound(n,bound_upper=None,digits=1):
    bound_upper = digit_length_of_all_ndigits(digits)
    while bound_upper <= n:
        digits += 1
        bound_upper += digit_length_of_all_ndigits(digits)
    return bound_upper
def main():
    for i in range(1,11):
        print(i,get_upper_bound(i),10**i,get_upper_bound(10**i))

if __name__ == '__main__':
    main()
