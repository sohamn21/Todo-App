  while True:
    user_action =input("Type add or show or edit or Complete or exit :")
    user_action = user_action.strip()

    match user_action :
        case 'add':
            todo = input("Enter a todo:") +"\n"
            file =open('todos.txt', 'r')
            todos =file.readlines()
            file.close()
            todos.append(todo)
            file = open("todos.txt",'w')
            file.writelines(todos)
            file.close()

        case 'show'| 'display':
            for index, item in enumerate(todos) :
                row = f"{index +1}-{item}"
                print(row)

        case 'edit':
            number = int(input("Enter the number of todo you want to edit:"))
            number = number-1
            new_todo =input("Enter the nuew todo:")
            todos[number] = new_todo

        case 'complete':
            number =int(input("Enter the to-do you have completed:"))
            todos.pop(number - 1)

        case 'Length':
            print(len(todos))
        case 'exit':
            break
        case x:
            print("wrong Command")
        







