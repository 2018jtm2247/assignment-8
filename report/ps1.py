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
print(len(l))
raw_count=coloum_count=0
k=1
i=J=0
count=0

#chaeck pattern
for i in range(0,n):    #raw
	for j in range(0,m-1): #coloum value in the raw i
		if "S" in l[j]:	
		    #cheak horizontal pattern		
			while (j-k)>=0 and (j+k)<=m and "S" in l[j-k] and "S" in l[j+k] :
				raw_count+=2
				print("raw=",raw_count)
				print(j-k)
				k+=1
			k=m-1	
			print("k=",k)
	            
	        #check upper pattern
			#while l[i-k] in "S" and l[i+k] in "S" and (i-k)>=0 and (i+k)<=n:
			while (j-k)>=0 and (j+k)<=n and "S" in l[j-k] and "S" in l[j+k] :
				coloum_count+=2
				print("coloum=",coloum_count)
				k=k+k
			k=1	

			if raw_count == coloum_count and raw_count != 0:
				count = raw_count + coloum_count + 1
				print("count=",count)    
		        
	#	        raw_count = coloum_count = count = 0

	   		
			raw_count = coloum_count = count =0

print("end of prog")                

