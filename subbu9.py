b=int(input())
temp=b
flag=0
if(b<0):
	print("negative numbers cannot be prime")
elif(b==0):
	print("not a prime")
else:
	for x in xrange(1,b+1):
		if(b%x==0):2
    
			flag=flag+1

          
	if(flag==2):
		print("prime")
	else:
		print("not a prime")
