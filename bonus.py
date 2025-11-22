import sys 
if len(sys.argv) == 2:
  script_name = sys.argv[0]
  empSalary = int(sys.argv[1])
  bonus = empSalary * 0.1
  final_salary = empSalary + bonus
  print("Script Name:" , script_name)
  print("Emp salary: ", empSalary)
  print("Final salary after 10% bonus:", final_salary)
  print("User provided input values:")
else: 
  script_name = sys.argv[0]
  empSalary = 12000
  bonus = empSalary * 0.1
  final_salary = empSalary + bonus
  print("Script Name:" , script_name)
  print("Emp salary: ", empSalary)
  print("Final salary after 10% bonus:", final_salary)
  print("No input given - using default values:")
