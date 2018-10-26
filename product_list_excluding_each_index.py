#07/19/2018----------------------------------------------------------------------------------------------------
#Given an array of integers, return a new array such that each element at index i of the new array
#is the product of all the numbers in the original array except the one at i.
#For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
#If our input was [3, 2, 1], the expected output would be [2, 3, 6]
def product_list_excluding_each_index(testList):
	retList = []
	for i in range(0,len(testList)):
		tempVal = 1
		for x in range(0,len(testList)):
			if x != i:
				tempVal *= testList[x]
		retList.append(tempVal)
	return(retList)

if __name__ == '__main__':
	testList = [1,2,3,4,5]
	testList2 = [3,2,1]
	print(product_list_excluding_each_index(testList))
	print(product_list_excluding_each_index(testList2))
