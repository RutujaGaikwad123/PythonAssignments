#Write a Python program to generate the next 15 leap years starting from a given year. Populate the leap years into a list and display the list. 
 def find_leap_years(given_year):
    list_of_leap_years=[0]*15

    # Write your logic here
    if given_year%100==0 and given_year%400!=0:
        for i in range(0,15):
             temp=given_year+(4*(i+1))
             list_of_leap_years[i]=temp
    elif given_year%400==0:
        for i in range(0,15):
            temp=given_year+(4*i)
            list_of_leap_years[i]=temp
    elif given_year%4==0:
        for i in range(0,15):
            temp=given_year+(4*i)
            list_of_leap_years[i]=temp
    elif given_year%4==1:
        for i in range(0,15):
            temp=given_year+3+(4*i)
            list_of_leap_years[i]=temp
    elif given_year%4==2:
        for i in range(0,15):
            temp=given_year+2+(4*i)
            list_of_leap_years[i]=temp
    elif given_year%4==3:
        for i in range(0,15):
            temp=given_year+1+(4*i)
            list_of_leap_years[i]=temp
        
             


    # Write your logic here
    
    return list_of_leap_years

list_of_leap_years=find_leap_years(2000)
print(list_of_leap_years)
