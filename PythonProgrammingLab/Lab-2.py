''' 2.	Write a program that asks the user to enter three numbers (use three separate input statements). Create variables called total and average that hold the sum and average of the three numbers and print out the values of total and average.  '''

a1=input("Enter 1st number: \t")
a2=input("Enter 2nd number: \t")
a3=input("Enter 3rd number:\t")
total=float(a1)+float(a2)+float(a3)
print("Sum of three numbers is : \t {}".format(total))
average=total/3
print("Average of three numbers is : \t{}".format(average))
