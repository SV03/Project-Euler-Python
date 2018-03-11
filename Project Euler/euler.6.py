def sum_sqaure_diff(to):
    v1 = sum(i for i in xrange(1, to+1))
    v2 = sum(j**2 for j in xrange(1, to+1))
    return v1**2 - v2

if __name__ == "__main__":
	print(sum_sqaure_diff(100))
