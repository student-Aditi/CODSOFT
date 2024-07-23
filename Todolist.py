def main():
    tasks =[]
    while True:
        print("1: Add task")
        print("2: Show Tasks")
        print("3: Mark Task as Done")
        print("4: Exit")

        choice=input("Enter your choice")
        if choice=='1':
            print()
            task=int(input("How many task you want to add"))
            for i in range(task):
                ta_sk=input("Enter the task:")
                tasks.append({"task":ta_sk,"done":False})
                print("Task added !!")

                
        elif choice=='2':
            print("\n Tasks:")
            for index, task in enumerate(tasks):
                status="Done" if task["done"] else "Not done"
                print(f"{index+1}.{task['task']}-{status}")
         
        elif choice=='3':
            task_index=int(input("Enter the task number to mark as done:"))-1
            if 0<=task_index < len(tasks):
                tasks[task_index]["done"]=True
                print("Task marked as done")
            else:
                print("Invalid task number")
        
        elif choice=='4':
            print("Exiting the to-do list")
            break
        else:
            print("Invalid choice.Try Again")

if __name__=="__main__":
    main()

   

