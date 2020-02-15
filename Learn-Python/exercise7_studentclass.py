students = [("George", 4.0),("Marsha", 2.7), ("Sidney", 3.1), ("Qazi", 4.0), ("Tom", 3.5), ("Ryan", 3.9), ("Andy", 1.9), ("Billy", 3.8)]


def class_average(students):
  total = float()
  for s in students:
    total = total + s[1]
  return (total / len(students))

def filter_students(students, filter):
  final_students = []
  for s in students:
    if s[1] > filter:
      final_students.append(s[0])
  return final_students

def failing_students(students, filter):
  final_students = []
  for s in students:
    if s[1] < filter:
      final_students.append(s[0])
  return final_students


print(f"\nThe classes average is: {class_average(students)}\n")
print(f"\nThe best students are {filter_students(students, 3)}\n")
print(f"\nThe students that are failing are {failing_students(students, 2.0)}\n")
