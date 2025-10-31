-------------------------CODE--------------------------
import pandas as pd

df = pd.read_csv('statistical_description.csv')
data = df['Marks']

def quartiles_outliers(data) :
 
 Q1 = data.quantile(0.25)
 Q3 = data.quantile(0.75)
 IQR = Q3 - Q1 
 Q2 = data.median()
   
 print("Quartiles : ")
 print("Q1 = " , Q1)
 print("Q2(Median) = " , Q2)
 print("Q3 = " , Q3)
 
 lower_bound = Q1 - 1.5 * IQR
 upper_bound = Q3 + 1.5 * IQR

 print("Outliers Boundaries: [ " , lower_bound , "," , upper_bound , "]" )

def mean_median_mode_modality(data) :
 
 mean = data.mean()
 median = data.median()
 mode = data.mode()

 print("MEAN : ", mean)
 print("MEDIAN : " , median)
 print("MODE : ", mode.tolist())
 # Convert the Pandas Series to a Python List for clean output

 modality = len(mode)
 if modality == 1 :
   print("Modality : Unimodal")
 elif modality == 2 :
   print("Modality : Bimodal")
 elif modality == 3 :
   print("Modality : Trimodal")
 else :
   print("Modality : Multimodal")

def std_dev(data) :
 std_dev = data.std()
 print("Standard Deviation : " , std_dev)

quartiles_outliers(data)
print("-"*30)
mean_median_mode_modality(data)
print("-"*30)
std_dev(data)












----------------------CSV FILE-----------------------
NAME : statistical_description.csv

ID,Name,Marks
1,Alice,88
2,Bob,92
3,Charlie,75
4,Diana,95
5,Ethan,81
6,Fiona,78
7,George,90
8,Hannah,85
9,Isaac,99
10,Jasmine,70
11,Kevin,83
12,Lily,91
13,Mike,77
14,Nora,86
15,Oliver,94
