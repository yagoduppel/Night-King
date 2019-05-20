import random
from sys import stdin

def roundBattle(live,dead):
	if live == 0:
		print("The dead win!")
		return live,dead,"survivor"
	elif dead == 0:
		print("The survivors win!")
		return live,dead,"dead"
	live -= 1
	dead -= 1
	x = random.random()
	if x < 0.5:
		live += 1
		print("SURV")
	else:
		dead += 2
		print("DEAD")
	print("live = " + str(live))
	print("dead = " + str(dead)+"\n")
	return live, dead, True
	
def Game(n,m):
	result = True
	while result == True:
		n,m,result = roundBattle(n,m)
	return result

"""
matrix = []
for i in range(100):
	matrix.append([])

for i in range(100):
	for j in range(100):
		survScore = 0
		deadScore = 0
		for k in range(100):
			result = Game(i+1,j+1)
			if result == "survivor":
				survScore += 1
			else:
				deadScore += 1
		matrix[i].append(survScore-deadScore)
#print(matrix)
closest = []
for i in range(100):
	best_ind, best_val = 0, 1000
	for ind,val in enumerate(matrix[i]):
		if abs(val) < abs(best_val):
			best_ind, best_val = ind, val
	closest.append(best_ind)
print(closest)"""
Game(100,6)
