
def find_children(employee, age=18):
    for e in employee:
        for child in e.get('children', []):
            if child.get('age') and child.get('age') > age:
                yield e.get('name')
                break
