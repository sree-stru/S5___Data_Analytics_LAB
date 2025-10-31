import numpy as np

x_list = list(map(float, input("Enter the first set of numbers (space separated): ").split()))
y_list = list(map(float, input("Enter the second set of numbers (space separated): ").split()))

x = np.array(x_list)
y = np.array(y_list)

if len(x) != len(y):
    print("ERROR: Length of first set and length of second set must be equal")
    exit()

n = len(x)

def manual_calculation(x, y, n):
    x_mean = np.sum(x) / n
    y_mean = np.sum(y) / n
  
    numerator = np.sum((x - x_mean) * (y - y_mean))
    covariance = numerator / (n - 1)

    std_x = np.sqrt(np.sum((x - x_mean)**2) / (n - 1))
    std_y = np.sqrt(np.sum((y - y_mean)**2) / (n - 1))
    
    correlation = covariance / (std_x * std_y)
    
    print("\n--- Manual Calculation ---")
    print("Covariance:", covariance)
    print("Correlation:", correlation)

def function_calculation(x, y):
    cov_matrix = np.cov(x, y)
    covariance = cov_matrix[0, 1]
    
    corr_matrix = np.corrcoef(x, y)
    correlation = corr_matrix[0, 1]
    
    print("\n--- Built-in Function Calculation (NumPy) ---")
    print("Covariance:", covariance)
    print("Correlation:", correlation)

manual_calculation(x, y, n)
function_calculation(x, y)
