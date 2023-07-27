star="*"
for i in range(1): 
    print(star)
    for i in range(4):
        star=star+"*"
        print(star)
# For every i across a range of 1, print 1*, and then for every i across a range of 4, print 1* + 1* for each iteration (4), for as many iterations as the outer loop (1).