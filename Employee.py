class Employee(object):
	def __init__(self,name,gender,age):
		self.name=name
		self.gender=gender
		self.age=age
	def do_work(self):
		pass
	def details():
		pass
class software_developer(Employee):
	def __init__(self,name,gender,age,salary):
		super(software_developer,self).__init__(name,gender,age)
		self.salary=salary
	def do_work(self):
		self.work='Build software'
	def details(self):
		self.do_work()
		details={'Name':self.name,'Age ':self.age,'Work':self.work,'Salary':self.salary}
		return details
class sales_manager(Employee):
	def __init__(self,name,gender,age,salary):
		super(sales_manager,self).__init__(name,gender,age)
		self.salary=salary
	def do_work(self):
		self.work='Manage sales'
	def details(self):
		self.do_work()
		details={'Name':self.name,'Age ':self.age,'Work':self.work,'Salary':self.salary}
		return details

class manager(Employee):
	def __init__(self,age,gender,name,salary):
		super(manager,self).__init__(name,gender,age)
		self.salary=salary
	def do_work(self):
		self.work='manage employees'
	def details(self):
		self.do_work()
		details={'Name':self.name,'Age ':self.age,'Work':self.work,'Salary':self.salary}
		return details
dev=manager('meshack','male',21,200)
dev.do_work()
print isinstance(dev,Employee)