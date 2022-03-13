model = []
test_array = []
array_of_test_array = []
final_ans = 0

test_data_file = open("test_data.txt")
f = open("model.txt","r")

for line in f:
    lst = line.split()
    model.append(lst)

f.close()

for line in test_data_file:
    lst_num = line.split()
    test_array.append(lst_num)
    if line == "\n":
        array_of_test_array.append(test_array)
        test_array = []

test_data_file.close()

###goes through every number in the test case and adds values to final ans
#goes through every test case
for lst in array_of_test_array:
    #ever row in test case
    for i in range(32):
        #every column in test case
        for j in range(32):
            #if there is a value in a specific grid, add the value of the specific grid from model to the final ans
            if lst[i][j] != 0:
                final_ans+=model[i][j]

    #checks to see what our final result is
    if final_ans==0:
        print('idk')
    elif final_ans>0:
        print(square)
    else final_ans<0:
        print(circle)
