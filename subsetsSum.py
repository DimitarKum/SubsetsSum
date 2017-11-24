def subsetsSum(multiset, target):
	sol = [[0 for j in range(len(multiset) + 1)] for i in range(target + 1)]
	for i in range(1, target + 1):
		for j in range(1, len(multiset) + 1):
			if multiset[j - 1] == i:
				sol[i][j] = sol[i][j - 1] + 1
			elif multiset[j - 1] > i:
				sol[i][j] = sol[i][j - 1]
			elif multiset[j - 1] < i:
				sol[i][j] = sol[i][j - 1] + sol[i - multiset[j - 1]][j - 1]
	
	print("   ", [0] + multiset)
	print()
	for i in range(len(sol)):
		print(i, ":", sol[i])

	return sol

def recoverSets(multiset, target):
	sets = []
	locations = [(target, len(multiset), [])]
	while len(locations) > 0:
		i, j, curSet = locations.pop()
		if i < 0 or j < 1:
			continue
		
		if multiset[j - 1] == i:
			sets.append(curSet + [i])
			locations.append((i, j - 1, curSet))
		elif multiset[j - 1] > i:
			locations.append((i, j - 1, curSet))
		elif multiset[j - 1] < i:
			locations.append((i, j - 1, curSet))
			locations.append((i - multiset[j - 1], j - 1, curSet + [multiset[j - 1]]))
	
	print(len(sets))

	sets.sort()
	for i in range(len(sets)):
		sets[i].sort()
	sets.sort()

	for subset in sets:
		print(subset)

def main():
	multiset = [1, 2, 1, 3, 1, 4, 1, 5]
	target = 6
	subsetsSum(multiset, target)
	print()
	recoverSets(multiset, target)

main()