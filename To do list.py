#options = {1:'Add',2:'Edit',3:'Delete', 4:'Mark'}
task = []
while True:
    print("1.ADD TASK")
    print("2.Edit TASK")
    print("3.Delete list")
    print("4.Mark task")
    choice = input('Enter your options: ')
    if choice == '1':
        n = input('Enter your task: ')
        date = input('Enter your deadline: ')
        p = {'text': n , 'deadline': date}
        task.append(p)
    elif choice == '2':
        e = int(input('choose your task index to edit: '))
        for index,t in enumerate(task):
            print(f"{index}: {t['text']}")
        if 0 <= e < len(task):
            task[e]['text'] = input('Enter your new task: ')
            task[e]['deadline'] = input('Enter your new deadline: ')
            print(task)
        else:
            print('Invalid Task')
    elif choice == "3":
        c = input("Enter task to delete: ") # we can also take task no as an input , so i will edit it acordingly.
        if c in task:
            task.remove(task)
            print("Task deleted!")
        else:
            print("Task not found!")

    elif choice == "4":
        done = input("Enter task to mark complete: ")
        if done in task:
            index = task.index(task)
            task[index] = "✔ " + task
            print("Task marked complete!")
        else:
            print("Task not found!")
    elif choice == '5':
        break


            
