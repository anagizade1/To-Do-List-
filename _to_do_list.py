print('welcome to your to do list program')
tasks=[]
while True:
    print('Please type a nuber between 1 and 5')
    print('''1 --- Add a task
        2 --- View list
        3 --- Mark as done
        4 --- Delete task
        5 --- Exit
        ''')
    print("Current tasks:", tasks)
    try:
          command = int(input(' please enter a command number:  '))
    except:
          print('please make sure to type a number:  ')
          continue          
    if command == 5:
        print('goodbye ')
        break
    elif command == 1:
        tasks.append(input('add a task: '))

    elif command == 2:
        i = 1
        print('DEBUG')
        for t in tasks:
            print(i, "--", t)
            i += 1

    elif command == 3:
    
        done=int(input('which task has done?  '))
        if done <= len(tasks):
            tasks[done-1] = '[DONE]' + tasks[done-1]

        else:
          print('please enter correct numuber:  ')

    elif command == 4:
     delete=int(input('please enter the number of task which you want to delete:  '))
     tasks.pop(delete-1)
     
    else: 
        print('please enter between 1 and 5: ')

