class Parent():
	def __init__(self,last_name,eye_color):
		print("parent cons called")
		self.last_name=last_name
		self.eye_color=eye_color
	def info(self):
		print("lastname is "+self.last_name)
		print("eyecolor is "+self.eye_color)
		
class Child(Parent):
	def __init__(self,last_name,eye_color,no_of_toys):
		print("child cons called")
		Parent.__init__(self,last_name,eye_color)
		self.no_of_toys=no_of_toys
	def info(self):
		print("lastname is "+self.last_name)
		print("eyecolor is "+self.eye_color)		
		print("total toys are "+str(self.no_of_toys))		
		
bk=Parent("kalsi","brown")
bk.info()
print(bk.last_name)
cmk=Child("kalsi","blue",10)
print(cmk.no_of_toys)
cmk.info()
