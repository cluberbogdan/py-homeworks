import numpy as np

zeros_array = np.zeros((4, 3))
print("a)")
print(zeros_array)

ones_array = np.ones((4, 3))
print(ones_array)

numbers_array = np.arange(12).reshape((4, 3))
print(numbers_array)


x = np.arange(1, 101)
F = 2 * x ** 2 + 5
table_data = np.column_stack((x, F))
print("b)\n", table_data)


x_values = np.arange(-10, 11)
F_values = np.exp(-x_values)
table_data2 = np.column_stack((x_values, F_values))

print("c)\n" "{:<5} {:<10}".format("x", "F(x)"))
for row in table_data2:
    print("{:<5} {:<10}".format(int(row[0]), row[1]))