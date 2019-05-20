from sys import stdin

def buildMatrix(n,m):
	matrix = []
	#counter = 1
	for i in range(n+m+1):
		matrix.append([])
		if i <= m:
			for j in range(n+1):
				matrix[i].append([0,0])
				#counter +=1
		else:
			for j in range(n+m+1-i):
				matrix[i].append([0,0])
				#counter +=1
	return matrix




for line in stdin:
	L = line.split()
	n, m = int(L[0]), int(L[1])
	dim = (n+1)*(m+1+n/2)//1
	matrix = buildMatrix(n,m)
	#matrix2 = buildMatrix(n,m)
	matrix[m][n][0] = 1
	top = []
	side = []
	for i in range(n+1):
		top.append(0)
	for i in range(n+m+1):
		side.append(0)
	
	for i in range(max(n,m//2+1)):
		for x in [0,1]:
			for j in range(1, n+m+1):
				if j <= m:
					iterateList = range(1,n+1)
				else:
					iterateList = range(1,n+1+m-j)
				for k in iterateList:
					if matrix[j][k][x] != 0:
						p = matrix[j][k][x]
						matrix[j-1][k][(x+1)%2] += p/2
						matrix[j+1][k-1][(x+1)%2] += p/2
						matrix[j][k][x] = 0
			
			#for k in range(n+1):
			#	top[k] += matrix[0][k][(x+1)%2]
			#for j in range(n+m+1):
			#	side[j] += matrix[j][0][(x+1)%2]

		#print(matrix)
		#print()
		#matrix2 = buildMatrix(n,m)
	top = sum([sum(matrix[0][i]) for i in range(n+1)])
	#print(top)
	#print(matrix)
	#print(side)
	print("The living win " + str(top) + " of the time.")
