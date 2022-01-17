'''Write a python function, find_correct() which accepts a dictionary and returns a list as per the rules mentioned below.
The input dictionary will contain correct spelling of a word as key and the spelling provided by a contestant as the value.

The function should identify the degree of correctness as mentioned below:
CORRECT, if it is an exact match
ALMOST CORRECT, if no more than 2 letters are wrong
WRONG, if more than 2 letters are wrong or if length (correct spelling versus spelling given by contestant) mismatches.

and return a list containing the number of CORRECT answers, number of ALMOST CORRECT answers and number of WRONG answers. 
Assume that the words contain only uppercase letters and the maximum word length is 10.

Sample Input                                    Expected Output

{"THEIR": "THEIR", "BUSINESS": "BISINESS",        [2, 2, 1]
 "WINDOWS":"WINDMILL","WERE":"WEAR",
 "SAMPLE":"SAMPLE"}            '''

def find_correct(word_dict):
    #start writing your code here
    key=[]
    value=[]
    count=0
    correct=0
    wrong=0
    atmost=0
    result=[]
    for i,j in word_dict.items():
            key.append(i)
            value.append(j)
    for i in range(len(key)):
        if(len(key[i])==len(value[i]) and key[i]==value[i]):
            correct+=1
        elif((len(key[i])==len(value[i]))==False):
            wrong+=1
        else:
            for j in range(len(key[i])):
                if((key[i][j]==value[i][j])==False):
                    count+=1
                    if(count>2):
                        wrong+=1
                        break
            if(count<=2):
                atmost+=1
            count=0
           
           
    result=[correct,atmost,wrong]
    return result

word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))



