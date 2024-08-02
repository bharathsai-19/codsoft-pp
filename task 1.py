tasks = {}

def add_task(task_name):
    if task_name not in tasks:
        tasks[task_name] = False
        print(f"task'{task_name}' added.")
    else:
        print("task already exists.")
1
def complete_task(task_name):
    if task_name in tasks:
        tasks[task_name]=True
        print(f"task'{task_name}'completed.")
    else:
        print(" task not found.")
def show_tasks():
    if not tasks:
        print(" no tasks found.")
    else:
        print("tasks:")
        for task,completed in tasks.items():
            status ="completed" if completed else "incomplete"
            print(f"{task}:{status}")

def main():
    while True:
        print("\n1.add task")
        print("2. complete task")
        print("3.show tasks")
        print("4.exit")
        choice =input("enter your choice:")


        if choice =="1":
            task_name=input("enter your choice:")
            add_task(task_name)
        elif choice =="2":
            task_name =input("enter task name to complete:")
            complete_task(task_name)
        elif choice =="3":
            show_tasks()
        elif choice == "4":
            print("exiting program.")
            break
        else:
            print("invalid choice.")
if __name__ == '__main__':
     main()