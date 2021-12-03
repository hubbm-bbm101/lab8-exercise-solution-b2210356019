import sys

file_path = sys.argv[1]
commands = sys.argv[2].split(",")

student_file = open(file_path, "r")
student = {}
for line in student_file:
    key, value = line.strip("\n").split(":", 1)
    student[key] = value
student_file.close()


class CantFindNameError(Exception):
    pass


for name in commands:
    try:
        if name not in student.keys():
            raise CantFindNameError
        else:
            print("Name: " + name + ", University: " + student[name])
    except CantFindNameError:
        print("No record of '{}' was found!".format(name))
