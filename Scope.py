class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        differences = []

        for i in range(len(self.__elements) - 1):
            minuend = self.__elements[i]
            for j in self.__elements[i+1:]:
                differences.append(abs(minuend - j))
                
        self.maximumDifference = max(differences)
# End of Difference class

_ = 3
a = [1,2,5]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
