print()
expenses = []
for i in range(2):
    expenses.append(int(input("enter expense:")))

total = sum(expenses)
print(str(total))