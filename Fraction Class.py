class Fraction:
	def __init__(self, numerator, denominator):
		self.numerator = numerator
		self.denominator = denominator
	def print(self):
		print(self.numerator, "/" ,self.denominator)
	def simplify(self):
		greater, lesser = max(self.numerator, self.denominator), min(self.numerator, self.denominator)
		factNum = [i for i in range(1, self.numerator) if self.numerator % i == 0]
		factDen = [i for i in range(1, self.denominator) if self.denominator % i == 0]
		print(factNum)		
		print(factDen)		

if __name__ == '__main__':
	fract1 = Fraction(36,72)
	fract1.print()
	fract1.simplify()