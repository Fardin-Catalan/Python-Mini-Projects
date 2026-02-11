
name=input("Enter your name:")
print("Welcome to short task python program,"+name+"!")
tasks=[
     "Complete Python tutorial",
    "Practice coding challenges",
    "Read tech blogs",
    "Watch AI documentary",
    "Build a mini game",
    "Debug old projects",
    "Write a blog post",
    "Learn Git basics",
    "Contribute to open source",
    "Prepare for interviews"
]
while True:
      print("\n1. Add task")
      print("2. Show tasks")
      print("3. Remove task")
      print("4. Exit")
      choice=input("Enter your choice(1-4):")
      if choice=='1':
         task=input("Enter a new task:")
         tasks.append(task)
      elif choice=='2':
           for i,t in enumerate(tasks,1):
               print(str(i)+"."+str(t))
      elif choice == '3':
           for i, t in enumerate(tasks, 1):
               print(f"{i}. {t}")
               num = int(input("Enter the number of the task to remove: "))
               if 0 < num <= len(tasks):
                  tasks.pop(num - 1)
      elif choice == '4':
           break
      else:
           print("Invalid")
