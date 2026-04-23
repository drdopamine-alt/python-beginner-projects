#options = {1:'Add',2:'Edit',3:'Delete', 4:'Mark'}
task = []
options = ['Add task','Edit task','Delete task','Mark task']
print(options)
choice = input('Enter your options: ')
if choice == 'Add task':
    n = input('Enter your task: ')
    date = input('Enter your deadline: ')
    p = {'text': n , 'deadline': date}
    task.append(p)
    print(task)
elif choice == 'Edit task':
    e = int(input('choose your task index to edit: '))
    for index,t in enumerate(task):
        print(f"{index}: {t['text']}")
    if 0 <= e < len(task):
        task[e]['text'] = input('Enter your new task: ')
        task[e]['deadline'] = input('Enter your new deadline: ')
        print(task)
    else:
        print('Invalid Task')
elif choice == "Delete task":
    c = input("Enter task to delete: ") # we can also take task no as an input , so i will edit it acordingly.
    found = False
    for t in task:
        if t['text'] == c:
            task.remove(t)
            print("Task deleted!")
            found = True 
            break

        else:
            print("Task not found!")

elif choice == "Mark task":
    done = input("Enter task to mark complete: ")
    found = False
    for t in task:
        if t['text'] == done:
            t['text'] = "✔ " + t['text']
            print("Task marked complete!")
            found = True
            break
        else:
            print("Task not found!")


            
