class Car(object):
	"""docstring for ClassName"""
	def __init__(self,*aset):
		if len(aset)==3:
			self.type=aset[0]
			self.name=aset[1]
			self.model=aset[2]
		elif len(aset)==2:
			self.type='saloon'
			self.name=aset[1]
			self.model=aset[0]
		else:
			self.type='saloon'
			self.name='General'
			self.model='GM'
		
		
		if self.model=='Porshe' or self.model== 'Koenigsegg':
			self.doors=2
		else:
			self.doors=4
		if self.type=='saloon':
			self.wheels=4
			self.speed=0
		else:
			self.wheels=8
		self.speed=0
	def drive(self,speed):
		if self.type=='saloon':
			self.speed=1000
		else:
			self.speed=77
		return self.speed

o=Car('MAN', 'Truck', 'trailer')
c =  Car('Toyota', 'Corolla')
print o.doors,o.model,o.wheels,o.type,o.drive(1)
print c.doors,c.model,c.wheels,c.type,c.drive(1)