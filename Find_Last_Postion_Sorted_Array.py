def getLast(arr, target):
	l, r = 0, len(arr) - 1
	while l + 1 < r:
		mid = (l + r) // 2
		if arr[mid] == target:
			l = mid
		elif arr[mid] < target:
			l = mid
		else:
			r = mid
	
	if arr[l] == target: return l
	if arr[l] == target: return r