# 99乘法表
print(' \n'.join([' '.join(["%2s x%2s = %2s"%(j,i,i*j) for j in range(1,i+1)]) for i in range(1,10)]))
# print([''.join([''.join('%2s' % j ) for j in range(i) ])for i in range(10)])

# 迷宫实现
print(''.join(__import__('random').choice('╱╲') for i in range(50*24)))

# 心形实现
print(' \n'.join([''.join([('Love'[(x-y) % len('Love')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0else' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))

# 实现求解2的1000次方的各位数之和,map()函数将一个全部为str的列表，转化为全部为int的列表
print(sum(list(map(int,str(2**1000)))))
print(sum(map(int,str(2**1000))))

# FizzBuzz问题：打印数字1到100, 3的倍数打印“Fizz”, 5的倍数打印“Buzz”, 既是3又是5的倍数的打印“FizzBuzz”
for x in range(1, 101): print("fizz\t"[x % 3 * 4:]+"buzz"[x % 5 * 4:] or x)

# Mandelbrot图像：图像中的每个位置都对应于公式N=x+y*i中的一个复数
# print('\n'.join([''.join([ * if abs((lambda a: lambda z, c, n: a(a, z, c, n))(lambda s, z, c, n: z if n == 0 else s(s, z*z+c, c, n-1))(0, 0.02*x+0.05j*y, 40)) < 2 else for x in range(-80, 20)]) for y in range(-20, 20)]))

# 计算出1-100之间的素数(两个版本)
print(''.join([str(item) for item in filter(lambda x: not [x % i for i in range(2, x) if x % i == 0], range(2, 101))]))
print(''.join([str(item) for item in filter(lambda x: all(map(lambda p: x % p != 0, range(2, x))), range(2, 101))]))

# 代码输出斐波那契数列
print([x[0] for x in [(a[i][0], a.append([a[i][1], a[i][0]+a[i][1]])) for a in ([[1, 1]], ) for i in range(30)]])

# 代码实现快排算法
qsort = lambda arr: len(arr) > 1 and qsort(list(filter(lambda x: x <= arr[0], arr[1:]))) + arr[0:1] + qsort(list(filter(lambda x: x > arr[0], arr[1:]))) or arr
print(qsort([17,21,13,5,6,2]))

# 代码解决八皇后问题
# print([__import__( sys ).stdout.write( .join( .  * i +  Q  +  .  * (8-i-1) for i in vec) + "========") for vec in __import__( itertools ).permutations(range(8)) if 8 == len(set(vec[i]+i for i in range(8))) == len(set(vec[i]-i for i in range(8)))])

# 代码实现数组的flatten功能: 将多维数组转化为一维
# flatten = lambda x: [y for l in x for y in flatten(l)] if isinstance(x, list) else [x]

# 代码实现list, 有点类似与上个功能的反功能
array = lambda x: [x[i:i+3] for i in range(0, len(x), 3)]
print(array([4,2,1,3,4,4,3,2,1]))
