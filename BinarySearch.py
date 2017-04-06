class BinarySearch(list):
	def __init__(self,a,b):
		'''
		a is the length of the list to be created while b is the step to be used
		'''
		self.length=a
		for item in range(b,(a*b)+1,b):
			self.append(item)
		print (self,len(self))
	def search(self,item):
		result={'count':0,'index':-1}
		first=0
		last = len(self)-1
		found = False
		count=0
		index=-1
		b=self[last]-self[last-1]
		if item not in range(self[0],self[last]+1,b):
			count=0
			index=-1
		elif item==self[last]:
			count=0
			index=last
		else:
			while first<=last and not found:
				midpoint = (first + last)//2
				if self[midpoint] == item:
					index=midpoint
					found = True
				
				else:
					if item < self[midpoint]:
						last = midpoint-1
					else:
						first = midpoint+1
				count+=1
		
		result['count']=count
		result['index']=index
		return result

b=BinarySearch(20,2)
print b.search(40)