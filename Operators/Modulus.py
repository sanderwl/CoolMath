import numpy as np

number1 = np.random.randint(2, 100)
number2 = np.random.randint(1, number1)

print("Python modulus: ", number1, " modulus ", number2, " equals ", number1 % number2)

# My way
step1 = number1/number2
step2 = number2*np.floor(step1)
modulus = int(number1 - step2)


print("Sander modulus: ", number1, " modulus ", number2, " equals ", modulus)
