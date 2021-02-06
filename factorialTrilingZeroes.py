def trailingZeroes( n):
    count=0
    if n <= 3:
        return 0
    f =1
    for i in range(1, n+1):
        f = f *i
    # Get the number of zeroes
    f = [int(d) for d in str(n)]
    print("f",f)
    for num in enumerate(f):
      print("num", num)
      
      if num == 0:
        count = count +1
        print("num and count",count)
    return count
num = 5
print(trailingZeroes(num))