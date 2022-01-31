'''Write a Python function to find all the Strong numbers in a given list of numbers.
Write another function to find and return the factorial of a number. Use it to solve the problem.

Example:
A number is considered to be a Strong number if sum of the factorial of its digits is equal to the number itself. 
145 is a Strong number as 1! + 4! + 5! = 145. 

Sample Input                         Expected Output

num_list = [145,375,0,100,2]            [145, 2]    '''


def factorial(number):
    if number==1:
        return (number)
    elif number==0:
        return 1
    else:
        return number*factorial(number-1)
    

    
def find_strong_numbers(num_list):
    strong_num_list=[]
    for i in num_list:
        temp=str(i)
        answer=0
        for t in temp:
            answer=answer+factorial(int(t))
        
        if(i==answer):
            strong_num_list.append(i)
    return strong_num_list
            
       


num_list=[145,375,100,2,10]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)
