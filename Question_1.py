def stack(new_list, operations, number = None):
    if operations == 'add':
        new_list.insert(0, number)
    elif operations == 'remove':
        if new_list:
            new_list.pop(0)
        else:
            print("Stack is empty")
    return new_list

def queue(new_list, operations, number = None):
    if operations == 'add':
        new_list.append(number)
    elif operations == 'remove':
        if new_list:
            new_list.pop(0)
        else:
            print("Queue is empty")
    return new_list


new_list = [1, 2, 3, 4]
print("Adding new element to the stack")
new_list = stack(new_list, 'add', 0)
print(new_list)
print("Adding remove an element from stack")
new_list = stack(new_list, 'remove')
print(new_list)

print("Adding new element to the queue")
new_list = queue(new_list, 'add', 5)
print(new_list)
print("Adding remove an element from the queue")
new_list = queue(new_list, 'remove')
print(new_list)

