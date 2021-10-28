class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, ID, scores):
        super().__init__(firstName,lastName, ID)
        self.scores = scores

    def calculate(self):
        sum = 0
        for i in self.scores:
            sum+=i
        average= sum / len(self.scores)
        
        if average >= 90 and average <= 100:
            return "O"
        elif average >= 80 and average < 90:
            return "E"
        elif average >= 70 and average < 80:
            return "A"
        elif average >= 55 and average < 70:
            return "P"
        elif average >= 40 and average < 50:
            return "D"
        elif average < 40:
            return "T"
            
line = input().split()
