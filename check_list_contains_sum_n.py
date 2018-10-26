#07/18/2018----------------------------------------------------------------------------------------------------
#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
def check_list_contains_sum_n(testList, n):
	for i in range(len(testList)-1,0,-1):
		for x in testList:
			#print(testList[i])
			if testList[i] + x == n:
				return [True, 'sum found: {0} + {1}'.format(testList[i],x)]
		testList.pop(i)
		#print(testList)
	return [False, 'no 2 list values sum to {0}'.format(n)]


if __name__ == '__main__':
	testList = [1, 15, 13, 11, 7, 4]
	testList2 = [1, 14, 13, 11, 7, 4]
	testN = 21
	print(check_list_contains_sum_n(testList,testN))
	print(check_list_contains_sum_n(testList2,testN))
