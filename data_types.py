def data_type(arg):
	'''This function compares and returns results based of the following conditions
	:For :
		.strings, it returns its length
		.None,return string 'no value'
		.booleans,return the booleans
		.integers, return a string showing how it compares to hundred
		.lists, return the 3rd item or none if it doesn't exist
	
	:Author:Meshack Mbuvi
	:Email:meshmbuvi@gmail.com
	:Phone:+254719800509
	'''
	if isinstance(arg,str):
		return len(arg)
	elif arg==None:
	  return 'no value'
	elif isinstance(arg,bool):
	  return arg
	elif isinstance(arg,int):
	  if arg<100:
	    return 'less than 100'
	  elif arg==100:
	    return 'equal to 100'
	  else:
	    return 'more than 100'
	elif isinstance(arg,list):
	  if len(arg)>2:
	    return arg[2]
	  else:
	    return None
if __name__=='__main__':
	print data_type('kamila')
	print data_type(False)
	print data_type(3)
	print data_type([1,2])
	print data_type(None)