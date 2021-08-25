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

    if len(list_arguments) >3:
        print("Ingrese un comando valido, Por Favor.")
    else:
        if list_arguments[1]=="-create":
            #create una nueva tarea
            name_task= None
            name_duplicate= False
            while name_task==None or name_duplicate==True:
                print("-"*4,"*"*3,"-"*4)
                print("ingrese el nombre de la tarea: ")
                print("-"*4,"*"*3,"-"*4)
                name_task=input("")

                if view_duplicate(name_task)!=0:
                    name_duplicate=True
                else:
                    name_duplicate=False

            duration_task=0
            while duration_task <= 0:
                print("-"*4,"*"*3,"-"*4)
                print("ingrese la duración de la tarea: ")
                print("-"*4,"*"*3,"-"*4)
                duration_task=int(input(""))

            add_task(name_task,duration_task)        
            print("name_task: ",name_task)
        if list_arguments[1]=="-view":
            list_task=view()
            for element in list_task:
                print(element)
            
        
        if list_arguments[1]=="-search":
            task_search= search(list_arguments[2])

            print("task_search: ",task_search)
        
        if list_arguments[1]=="-delete":
            delete(list_arguments[2])

    

    pass
if __name__ == '__main__':
    run()
    


