import numpy as np
# November
# Week1
# Min Temp and max temp
a=np.array([9,30,6,25,8,23,10,31,8,23,13,30,13,32])
b=a.reshape(7,2)
print("Week 1")
print(b)

#Week2
# Min Temp and max temp
c=np.array([13,24,9,20,12,30,-13,25,9,29,10,25,6,22])
d=c.reshape(7,2)
print("Week 2")
print(d)

#Week3
# Min Temp and max temp
e=np.array([8,26,14,32,13,24,11,20,9,31,10,26,8,23])
f=e.reshape(7,2)
print("Week 3")
print(f)

#Week4
# Min Temp and max temp
g=np.array([13,24,9,32,8,31,11,23,15,26,14,24,7,25])
h=g.reshape(7,2)
print("Week 4")
print(h)

i=np.array([a,c,e,g])
print("November")
print(i)

# December
# Week1
# Min Temp and max temp
j=np.array([14,28,13,29,9,31,14,32,8,26,10,24,11,24])
k=j.reshape(7,2)
print("Week 1")
print(k)

#Week2
# Min Temp and max temp
l=np.array([12,26,13,29,13,28,13,29,6,29,9,21,15,25])
m=l.reshape(7,2)
print("Week 2")
print(m)

#Week3
# Min Temp and max temp
n=np.array([14,28,10,23,15,24,14,29,13,21,11,28,8,28])
o=n.reshape(7,2)
print("Week 3")
print(o)

#Week4
# Min Temp and max temp
p=np.array([15,28,14,20,11,27,13,25,11,32,12,22,6,23])
q=p.reshape(7,2)
print("Week 4")
print(q)

r=np.array([j,l,n,p])
print("December")
print(r)

# January
# Week1
# Min Temp and max temp
s=np.array([6,22,8,21,8,20,3,22,2,22,3,6,18,4])
t=s.reshape(7,2)
print("Week 1")
print(t)

#Week2
## Min Temp and max temp
u=np.array([8,19,4,21,4,20,8,20,6,22,2,7,18,4])
v=u.reshape(7,2)
print("Week 2")
print(v)

#Week3
# Min Temp and max temp
w=np.array([7,22,8,18,4,18,7,18,7,18,5,6,22,6])
x=w.reshape(7,2)
print("Week 3")
print(x)

#Week4
# Min Temp and max temp
y=np.array([7,21,3,21,7,21,5,20,8,18,6,2,22,3])
z=y.reshape(7,2)
print("Week 4")
print(z)

aa=np.array([s,u,w,y])
print("January")
print(aa)

#Februrary
#Week 1
# Min Temp and max temp
bb=np.array([12,22,12,21,-10,20,9,20,11,22,12,71,18,12])
cc=bb.reshape(7,2)
print("Week 1")
print(cc)

#Week2
## Min Temp and max temp
dd=np.array([11,20,8,22,10,21,7,22,9,20,12,11,22,7])
ee=dd.reshape(7,2)
print("Week 2")
print(ee)

#Week3
# Min Temp and max temp
ff=np.array([11,18,9,18,11,22,10,18,7,22,12,7,20,10])
gg=ff.reshape(7,2)
print("Week 3")
print(gg)

#Week4
# Min Temp and max temp
hh=np.array([7,20,9,20,11,18,12,22,8,21,11,10,21,7])
ii=hh.reshape(7,2)
print("Week 4")
print(ii)

jj=np.array([bb,dd,ff,hh])
print("Februrary")
print(jj)

# Overall Data
ll=np.array([b,d,f,h])
mm=np.array([k,m,o,q])
nn=np.array([t,v,x,z])
oo=np.array([cc,ee,gg,ii])
kk=np.array([ll,mm,nn,oo])
jjjj=np.array([i,r,aa,jj])
print("Temperature in Winters")
print(kk)

# Shape and Dimension of Numpy Array
print("Shape of Array:",kk.shape)
print("Dimension of array",kk.ndim)
print("Size of Array:",kk.size)
print("Type of elements in array:",kk.dtype)

#Daily temperatures for the first week of each month.
pp=np.array([ll[0],mm[0],nn[0],oo[0]])
print("Temperatures for 1st week of each month")
print(pp)

# Temperatures for Tuesday of each month
qq=np.array([a[2:4],c[2:4],e[2:4],g[2:4]]) #November
rr=np.array([j[2:4],l[2:4],n[2:4],p[2:4]]) #December
ss=np.array([s[2:4],u[2:4],w[2:4],y[2:4]]) #January
tt=np.array([bb[2:4],dd[2:4],ff[2:4],hh[2:4]]) #Feburary
uu=np.concatenate([qq,rr])
print("Temperatures for Tuesday of each month")
print(uu)
#Only the maximum temperature for all the weekdays of Dec and Feb.
vv= np.max(j)               # December
ww=np.max(l)
xx=np.max(n)
yy=np.max(p)
zz= np.array([vv,ww,xx,yy])
print("The maximum temperature for all the weekdays of Dec:")
print(zz)
aaa=np.max(bb)              # Feburary
bbb=np.max(dd)
ccc=np.max(ff)
ddd=np.max(hh)
eee=np.array([aaa,bbb,ccc,ddd])
print("The maximum temperature for all the weekdays of Feb:")
print(eee)
#All the days along with the week number in November when the minimum temperature was less than 8 degrees.
fff= i[i<8]
ggg=np.where(i<8)
print("For November temperature<8 is",fff,"at",ggg)
# All the weeks in Dec and Jan where the maximum temperature has crossed a threshold of 20 degrees.
nnn=r[r>20]
ooo=np.where(r>20)
print("All the weeks in Dec where the maximum temperature has crossed a threshold of 20 degrees are:")
print("Weeks:",ooo)
print("Temperatures are:",nnn)

#the average max temperature for the winter months
ppp=np.max(i)   #November
qqq=np.max(r)    #December
rrr=np.max(aa)    #January
sss=np.max(jj)    #Feburary
ttt=np.array([ppp,qqq,rrr,sss])
print("Average of maximum temperature are:",np.average(ttt))

#The weekly min avg temp for the month of Dec
uuu= np.min(j)               
vvv=np.min(l)
www=np.min(n)
xxx=np.min(p)
yyy=np.array([uuu,vvv,www,xxx])
print("The weekly minimum avg temp for December month",np.average(yyy))

#  The overall avg temp for the months Dec and Jan
print("Average Temperature for December month:",np.average(r))
print("Average Temperature for January month:",np.average(aa))

#The least temp experienced by the city in the month of Dec and Jan
print("Least temperature for December month:",np.min(r))
print("Least temperature for January month:",np.min(aa))

# The max temp in the month of Feb
print("Maximum temperature for Feburary month:",np.max(jj))

#  The days in the month of Nov where the max temp of the day dropped below the avg temp of the month.
zzz=np.average(i)
print("Average temperature in November:",zzz)
print("Temperature in November less than average temperature:",i[i<zzz])

#The above dataset into an array where the weeks of the same month must be present in the same row, but belonging to different months should come in a row either below or above the selected month.
aaaa=i.flatten()
bbbb=r.flatten()
cccc=aa.flatten()
dddd=jj.flatten()
print("Temperature in Winters:")
print(np.array([aaaa,bbbb,cccc,dddd]))

#  Array that holds the same data but presented in Fahrenheit
eeee=np.multiply(np.array([aaaa,bbbb,cccc,dddd]),1.8)
print("Temperature in Fahrenheit:")
print(np.add(eeee,32))

#Sort the above data in descending order
# Weekly average for the month of Dec
print("Weekly average of December are:",np.average(j) ,np.average(l),np.average(n),np.average(p),"respectively")
print("Sorting in decending order:",np.sort(jjjj)[::-1])

#The difference between the max temp of two consecutive days for each month of winter season
print("The difference between the max temp of two consecutive days for November:")
print("Week 1:",b[1][1]-b[0][1],"Week 2:",d[1][1]-d[0][1],"Week 3:",f[1][1]-f[0][1],"Week 4:",h[1][1]-h[0][1]) # November
print("The difference between the max temp of two consecutive days for December:")
print("Week 1:",k[1][1]-k[0][1],"Week 2:",m[1][1]-m[0][1],"Week 3:",o[1][1]-o[0][1],"Week 4",q[1][1]-q[0][1])  #December
print("The difference between the max temp of two consecutive days for January:")
print("Week 1:",t[1][1]-t[0][1],"Week 2:",v[1][1]-v[0][1],"Week 3:",x[1][1]-x[0][1],"Week 4",z[1][1]-z[0][1])  #January
print("The difference between the max temp of two consecutive days for Feburary:")
print("Week 1:",cc[1][1]-cc[0][1],"Week 2:",ee[1][1]-ee[0][1],"Week 3:",gg[1][1]-gg[0][1],"Week 4",ii[1][1]-ii[0][1])  #Feburary

#The difference between the minimum temp of two consecutive days for each month of the winter season.
print("The difference between the min temp of two consecutive days for November:")
print("Week 1:",b[1][0]-b[0][0],"Week 2:",d[1][0]-d[0][0],"Week 3:",f[1][0]-f[0][0],"Week 4:",h[1][0]-h[0][0]) # November
print("The difference between the min temp of two consecutive days for December:")
print("Week 1:",k[1][0]-k[0][0],"Week 2:",m[1][0]-m[0][0],"Week 3:",o[1][0]-o[0][0],"Week 4",q[1][0]-q[0][0])  #December
print("The difference between the min temp of two consecutive days for January:")
print("Week 1:",t[1][0]-t[0][0],"Week 2:",v[1][0]-v[0][0],"Week 3:",x[1][0]-x[0][0],"Week 4",z[1][0]-z[0][0])  #January
print("The difference between the min temp of two consecutive days for Feburary:")
print("Week 1:",cc[1][0]-cc[0][0],"Week 2:",ee[1][0]-ee[0][0],"Week 3:",gg[1][0]-gg[0][0],"Week 4",ii[1][0]-ii[0][0])  #Feburary

#An array by combining the data present in arrays created in q.23 and q.24
eeee=np.array([b[1][1]-b[0][1],d[1][1]-d[0][1],f[1][1]-f[0][1],h[1][1]-h[0][1],k[1][1]-k[0][1],m[1][1]-m[0][1],o[1][1]-o[0][1],q[1][1]-q[0][1],t[1][1]-t[0][1],v[1][1]-v[0][1],x[1][1]-x[0][1],z[1][1]-z[0][1],cc[1][0]-cc[0][0],ee[1][0]-ee[0][0],gg[1][0]-gg[0][0],ii[1][0]-ii[0][0]])
ffff=np.array([b[1][0]-b[0][0],d[1][0]-d[0][0],f[1][0]-f[0][0],h[1][0]-h[0][0],k[1][0]-k[0][0],m[1][0]-m[0][0],o[1][0]-o[0][0],q[1][0]-q[0][0],t[1][0]-t[0][0],v[1][0]-v[0][0],x[1][0]-x[0][0],z[1][0]-z[0][0],cc[1][0]-cc[0][0],ee[1][0]-ee[0][0],gg[1][0]-gg[0][0],ii[1][0]-ii[0][0]])
print(np.array([eeee,ffff]))

