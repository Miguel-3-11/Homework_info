s = input()

arr = s.split('student_')
arr.pop(0)

rate = []

for student in arr:
    rate.append(int(student[3::]))

print(arr[rate.index(max(rate))][0:3])