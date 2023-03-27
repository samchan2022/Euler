import math

# iterative approach
def get_sum_of_multiple_iterative(list_of_int,limit):
    sum=0
    for i in range(1, limit):
        cond=0
        for j in list_of_int:
            cond = cond or (i%j==0)
        if cond ==1:
            sum+=i
    return sum

# infinite sum
def get_sum_of_multiple_infinite_sum(limit):
    v=limit - 1
    n3=math.floor(v/3)
    sum3=3*n3*(n3+1)/2
    n5=math.floor(v/5)
    sum5=5*n5*(n5+1)/2
    # mcf: maximum common factor for the 3 and 5 is 15
    n15=math.floor(v/15)
    sum15=15*n15*(n15+1)/2
    return int(sum3+sum5-sum15)

sum1=get_sum_of_multiple_iterative([3,5],1000)
print(f"sum1: {sum1}")
sum2=get_sum_of_multiple_infinite_sum(1000)
print(f"sum2: {sum2}")
