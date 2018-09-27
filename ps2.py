###### this is the second .py file ###########

####### write your code here ##########
#rotate function
def rotate(lst,x):
    copy = list(lst)
    for i in range(len(lst)):
        if x<0:
            lst[i+x] = copy[i]
        else:
            lst[i] = copy[i-x]


#Create 3 groups
g1="abcdefghi"
g2="jklmnopqr"
g3="stuvwxyz_"

c1 =[]
c2 =[]
c3 =[]
index1=[]
index2=[]
index3=[]

#get key vakue from user
k1,k2,k3 = list(map(int,input().split()))

#get string
msg = input()
msg_list = list(msg)
print(msg_list)

#now compair g1 in string and copy similaar char into s1
for i in range(0,len(msg)):
	if msg_list[i] in g1:
		c1.append(msg_list[i])
		index1.append(i)
		
	elif msg_list[i] in g2:
	    c2.append(msg_list[i])
	    index2.append(i)
	elif msg_list[i] in g3:
	    c3.append(msg_list[i]) 
	    index3.append(i)



#rotate c1,c2,c3
rotate(c1,k1)
rotate(c2,k2)
rotate(c3,k3)



#get decrypted msg
p=q=r=0
for i in range(0,len(msg)+1):
	if i in index1:
		msg_list[i]=c1[p]
		p+=1
	elif i in index2:
		msg_list[i]=c2[q]
		q+=1
	elif i in index3:
		msg_list[i]=c3[r]
		r+=1	

print(msg_list)

for i in msg_list[:]:
	print (i, end ='')

print(\n)









