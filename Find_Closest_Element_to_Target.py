def findNearest(arr, target):
	l, r = 0, len(arr) - 1
	while l + 1 < r:
		mid = (l + r) // 2
		if arr[mid] < target:
			l = mid
		else:
			r = mid

	if abs(target - arr[l]) <= abs(target - arr[r]):
		return l
	else:
		return r

findNearest([1,2,3,6,7], 100)