###### this is the first .py file ###########

####### write your code here ##########
n,m = list(map(int,input().split()))     #get n raw m coloum

l=[]

for i in range(0,n):
	t = list(input())
	if len(t) == m:
		l = l+ [t]
	else:
	    print("Error")	


print(l)
raw_count=coloum_count=0
k=1
i=J=0
count=0
#chaeck pattern
for i in range(0,n):
	print(i)
	for j in range(0,m):
		if l[j] == "S":
			while l[j-k] == "S" and l[j+k]=="S":
				raw_count+=1
				print(raw_count)
				k+=1
			k=1	
			while l[i-k] == "S" and l[i+k]=="S":
				coloum_count+=1
				print(coloum_count)
				k+=1
			k=1	
			if raw_count == coloum_count:
			    count = raw_count + coloum_count + 1          
                print(count)
                raw_count = coloum_count = count = 0

            else:
               raw_count = coloum_count = count = 0    
               

print("end of prog")                

