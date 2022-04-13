def subset_sum(a: list, n: int, sum: int):
    
	# Initializing the matrix
	tab = [[0] * (sum + 1) for i in range(n + 1)]
	for i in range( sum + 1):
		tab[0][i] = 0
	
	for i in range(1, n+1):
		for j in range(sum + 1):
			if a[i-1] <= j:
				tab[i][j] = tab[i-1][j] + tab[i-1][j-a[i-1]]
			else:
				tab[i][j] = tab[i-1][j]
	return tab[n][sum]

if __name__ == '__main__':
	a = [3, 3, 3, 3]
	n = 4
	sum = 6
	print(subset_sum(a, n, sum))
