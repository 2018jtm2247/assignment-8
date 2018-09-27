###### this is the first .py file ###########

####### write your code here ##########
n,m = list(map(int,input().split()))     #get n raw m coloum
for i in range(1,n+1):
	for j in range(1,m+1):
	#	si = sys.stdin.read(1)
		si=input()
		l=list(si)
		print(l)
		j+=1
	print("")	
	print(si)	
	i+=1	


