#def greeting(name):
 #   print("Welcome,"+name)
#greeting("Kay")



#def greeting(name,department):
 #   print("Welcome,"+name)
  #  print("You are part of "+department)
#
#greeting("Blake","IT support")
#greeting("Tatiana" ,"Software Engineering")



#def area_triangle(base,height):
 #   return base*height/2
#area_a=area_triangle(5,4)
#area_b=area_triangle(7,3)
#sum=area_a+area_b
#print("The sum of both areas is:"+str(sum))

#def convert_seconds(seconds):
 #   hours=seconds//3600
  #  minutes=(seconds-hours*3600)//60
   # remaining_seconds=seconds-hours*3600-minutes*60
    #return hours,minutes,remaining_seconds
#hours,minutes,seconds=convert_seconds(5000)
#print(hours,minutes,seconds)



#def greeting(name):
 #   print("Welcome,"+name)
#result=greeting("Christine")
#print(result)

#name="Kay"
#number=len(name)*9
#print("Hello  ,"  + name + ". Your lucky number is "+str(number))


#name="Cameron"
#number=len(name)*9
#print("Hello ,"+name+ ".Your lucky name is "+str(number))




#def lucky_number(name):
 #   number=len(name)*9
  #  print("Hello  "+name + ".Your lucky number is "+str(number))

#lucky_number ("Kay")
#lucky_number ("Cameron")


# This function calculates the number of days in a variable number of
# years, months, and days. These variables are provided by the user and
# are passed to the function through the function’s parameters.
def find_total_days(years, months, days):
    # Assign a variable to hold the calculations for the number of days in
    # a year (years*365) plus the number of days in a month (months*30) plus
    # the number of days provided through the "days" parameter variable.
    my_days = (years * 365) + (months * 30) + days
    # Use the "return" keyword to send the result of the "my_days"


#def greater_value(x,y):
 #   if x > y:
  #      return x
   #else:
   #     return y
#print(greater_value(10,3*5))



def fractional_part(numerator,denominator):
   if dominator==0 or numerator==0 or numerator > denominator
        part=0
    else:
        part=(numerator%denominator)
     return part
print(fractional_part(5,5))
print(fractional_part(5,4))
print(fractional_part(5 ,3))
print(fractional_part(5,2))
print(fractional_part(0,5))

