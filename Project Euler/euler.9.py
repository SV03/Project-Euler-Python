def pyth_triplet(value):
    for a in xrange(1, value + 1):
        for b in xrange(1, value + 1):
            c = value - a - b
            if a*a + b*b == c*c:
                print 'a: ' + str(a) + \
                        ' b: ' + str(b) + \
                        ' c: ' + str(int((a**2 +b**2)**0.5))
                return str(a*b*c)

if __name__ == "__main__":
    print (pyth_triplet(1000))
