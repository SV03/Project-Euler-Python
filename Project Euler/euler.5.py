
import fractions
def smallest_muliti():
	max = 1
	for i in range(1, 21):
		max *= i // fractions.gcd(i, max)
	return str(max)


if __name__ == "__main__":
	print(smallest_muliti())
