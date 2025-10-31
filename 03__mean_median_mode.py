import statistics

user_input=input("Enter the numbers separated by space : ")
num=list(map(int, user_input.split()))

def mean(num):
   mean=statistics.mean(num)
   print("MEAN :" , mean)

def median(num):
   median=statistics.median(num)
   print("MEDIAN :" , median)

def mode(num):
   mode=statistics.mode(num)
   print("MODE :" , mode)

mean(num)
median(num)
mode(num)
