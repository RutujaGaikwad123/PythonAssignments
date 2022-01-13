Write a python function, create_largest_number(), which accepts a list of numbers and returns the largest number possible by concatenating the list of numbers. 
Note: Assume that all the numbers are two digit numbers.
 

Sample Input              Expected Output

23,34,55                       553423

def create_largest_number(number_list):
    leng=len(number_list)
    str1=""
    for i in range(leng-1):
        for j in range(leng-1):
            if(number_list[j]<number_list[j+1]):
                temp=number_list[j]
                number_list[j]=number_list[j+1]
                number_list[j+1]=temp
    string_ints = [str(int) for int in number_list]
    str_of_ints = int("".join(string_ints))
    
        
  
    return str_of_ints
    #remove pass and write your logic here

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)
