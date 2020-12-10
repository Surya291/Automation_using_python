

'''
/html/body/div[4]/div/div[1]/div[3]/div[1]/div[3]/div[9]/div[1]/div[1]/div[1]/div[2]/input[1]
/html/body/div[4]/div/div[1]/div[3]/div[1]/div[3]/div[9]/div[4]/div[1]/div[1]/div[2]/input[1]


/html/body/div[4]/div/div[1]/div[3]/div[1]/div[3]/div[12]/div[1]/div[1]/div[1]/div[2]/input[1]
/html/body/div[4]/div/div[1]/div[3]/div[1]/div[3]/div[12]/div[9]/div[1]/div[1]/div[2]/input[1]

/html/body/div[4]/div/div[1]/div[3]/div[1]/div[3]/div[15]/div[1]/div[1]/div[1]/div[2]/input[1]
/html/body/div[4]/div/div[1]/div[3]/div[1]/div[3]/div[15]/div[4]/div[1]/div[1]/div[2]/input[1]


/html/body/div[4]/div/div[1]/div[3]/div[1]/div[3]/div[18]/div[1]/div[1]/div[1]/div[2]/input[1]
/html/body/div[4]/div/div[1]/div[3]/div[1]/div[3]/div[18]/div[3]/div[1]/div[1]/div[2]/input[1]
'''

A = [9,12,15,18]
B = [range(1,5),range(1,10),range(1,5),range(1,4)]



def generate_xpath(i,j):
	prefix = str('/html/body/div[4]/div/div[1]/div[3]/div[1]/div[3]/')
	suffix = str('/div[1]/div[1]/div[1]/div[2]/input[1]')
	main = str('div[' + str(i) + ']' + 'div[' + str(j) + ']' )
	return str(prefix + main + suffix)
	


for count in range(0,4):
	i = A[count]
	for j in B[count]:
		print(generate_xpath(i,j))
		

	
			
