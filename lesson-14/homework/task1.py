import numpy as np

@np.vectorize
def ToCelsius(F):
    return (F-32)*5/9

arr1 = np.array([32, 68, 100, 212, 77])
C = np.round(ToCelsius(arr1), 2)
print(C)
