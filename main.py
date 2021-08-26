import sys,os
from pathlib import Path
from conection import *

class Task:
    def __init__(self,task_name,task_duration):
        self.task_name= task_name
        self.task_duration= task_duration
    
    def add_stack(task):
        pass


def run():
    list_arguments= sys.argv

    print("list_arguments",list_arguments)
    #Create a new task
    if (list_arguments[1]=="-create" or list_arguments[1]=="-c"):
        
        if (len(list_arguments)== 4):
            if not (view_duplicate(list_arguments[2])):
               task= Task(list_arguments[2],list_arguments[3])
               add_task(task.task_name,task.task_duration)
               print("Task create successfully!")
            else:
                print("Task existent!, Plase, try again.")
        else:
            #posible creación de un error en el futuro.
            print("Invalid command")

    #View all task
    elif (list_arguments[1]=="-view" or list_arguments[1]=="-v"):
        list_task=view()

        for element in list_task:
            print(element)

    #Search task
    elif (list_arguments[1]=="-search" or list_arguments[1]=="-sh"):

        task_search= search(list_arguments[2])
        print("task_search: ",task_search)

    elif (list_arguments[1]=="-delete" or list_arguments[1]=="-d"):
        delete(list_arguments[2])
    

    pass
if __name__ == '__main__':
    run()
    


