def find_max_min(alist):
	'''
	This function finds both minimum and maximum numbers in a given list 
	:Author:Meshack Mbuvi
	:Email:meshmbuvi@gmail.com
	:Phone:+254719800509
	'''
	result=[]# holds the output
	#sort the list first
	alist.sort()
	#Get the index of the last element in the list;the last element in this case
	max_index=len(alist)-1
	#get the minimum and largest value in that order
	min=alist[0]
	max=alist[max_index]
	
	#if the minimum value is the same as the maximum value,return it.Otherwise,return both 
	if min==max:
		result.append(alist[0])
	else:
		result.append(min)
		result.append(max)

	return result