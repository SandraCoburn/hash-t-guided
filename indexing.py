records = [
    ("Alice", "Engineering"),
    ("Bob", "Sales"),
    ("Carol", "Sales"),
    ("Dave", "Engineering"),
    ("Erin", "Engineering"),
    ("Frank", "Engineering"),
    ("Grace", "Marketing")
]
'''
Write some code to build something like this:
dept_indx = {
    "SAles": ['Bob', 'Carol'],
    "marketing": ['Grace'],
    "Engineering": ['Frank', 'Erin']
}
'''
dept_idx = {}
#Build index by dept
for name, dept in records:
    if dept not in dept_idx:
        dept_idx[dept] = []
    dept_idx[dept].append(name)

#Which employees are in a given department?

def emp_by_dept(d):
    emp = []

    for name, dept in records:
        if dept == d:
            emp.append(name)
    return emp

def add_employee(name, dept):
    records.append((name, dept))
    if dept not in dept_idx:
        dept_idx[dept] = []
    dept_idx[dept].append(name)

print(emp_by_dept("Sales"))
add_employee('Hank', 'Marketing')
print(emp_by_dept("Marketing"))

