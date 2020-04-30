from Data_Structure_Programs.Prime_Number import Prime

print("Prime Number in range 0 to 1000 is : ")
obj = Prime()
itr = 0
arr = []
for number in range(0, 1000, 100):
    array = obj.prime(number, number + 100)
    itr += 1
    arr.append(array)

obj.Print(itr)
