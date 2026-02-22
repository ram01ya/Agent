x=[1,2,3,4,5]
y=[2,3,5,4,6]

n=len(x)
sum_x=sum(x)
sum_y=sum(y)

sum_xy=sum(i*j for i , j in zip(x,y))
sumx2=sum(i**2 for i in x)



m=(n*sum_xy-(sum_x*sum_y))/((n*sumx2)-(sum_x**2))

mean_x=sum_x/n
mean_y=sum_y/n

c=mean_y-(mean_x*m)
print(f"m:{m}")
print(f"c:{c}")
print(f"Linear regression line: y={m}x+{c}")