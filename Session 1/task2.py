import math
def solution(a, b ,c):
	sol = []
	if a == 0 && b != 0:
		return (-c)/b
	if b == 0 && a == 0:
		return "sxal nermucum"
	D = b**2 - 4*a*c
	if D > 0:
		x1 = ((-b) + math.sqrt(D))/ (2*a) 
		x2 = ((-b) - math.sqrt(D))/ (2*a)
		sol = [x1, x2]
		return sol
		 
