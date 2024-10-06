def pascal_triangle(n):
	if n == 0:
		return []
	if n == 1:
		return [[1]]
	
	list_cont =[]
	for i in range(n):
		temp_list =[]
		for j in range(i+1):
			if j == 0 or j == i:
				temp_list.append(1)
			else:
				temp_list.append(list_cont[i-1][j-1] + list_cont[i-1][j])
		list_cont.append(temp_list)
	print(list_cont)

if __name__ == "__main__":
    pascal_triangle(pascal_triangle(5))