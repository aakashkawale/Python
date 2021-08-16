# A = P(1 + \frac{r}{n})^{nt}
# A	=	final amount
# P	=	initial principal balance
# r	=	interest rate
# n	=	number of times interest applied per time period
# t	=	number of time periods elapsed
p = float(input("Enter Principal amount : "))
r = float(input("Enter Rate of interest : "))
n = float(input("Enter The number that compound the interest : "))
t = float(input("Enter The Time of period : "))
r = r / 100
a = p * (1 + (r / n)) ** (n * t)
ci = a - p
print(ci)