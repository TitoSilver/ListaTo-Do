import sys,os
from pathlib import Path
from conection import *



class Task:
    def __init__(self,task_name,task_duration):
        self.task_name= task_name
        self.task_duration= task_duration



def complete_list(list_task=[],db_list=view()):

    for element in db_list:
        task=Task(element[0],element[1])

        list_task.append(task)
    
    quick_sort(list_task, 0, len(list_task))

    return list_task

#---------QUICK SORT---------
def partition(list_task,idx_init,idx_final):
    value= list_task[idx_final]
    count= idx_init-1
    
    for i in range(idx_init,idx_final):
        if list_task[i].task_duration <= value.task_duration:
            count += 1
            _save_number= list_task[count]
            list_task[count]= list_task[i]
            list_task[i]= _save_number
    _save_number=list_task[idx_final]
    list_task[idx_final]= list_task[count+1]
    list_task[count+1]= _save_number
    return count+1

def quick_sort(list_task,idx_init,idx_final):
    if idx_init < idx_final:
        pivot= partition(list_task,idx_init,idx_final-1)
        quick_sort(list_task,idx_init,pivot)
        quick_sort(list_task,idx_final+1,idx_final)

#---------END QUICK SORT---------


def run():
    list_arguments= sys.argv

    list_task= complete_list()
    
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
        print("-*"*4,"TASK VIEW","-*"*4)
        for element in list_task:
            print("\t",element.task_name, ":\t ",element.task_duration)


    #Search task
    elif (list_arguments[1]=="-search" or list_arguments[1]=="-sh"):

        task_search= search(list_arguments[2])
        print("\t",task_search[0],": ",task_search[1])

    elif (list_arguments[1]=="-delete" or list_arguments[1]=="-d"):
        delete(list_arguments[2])
    

    pass
if __name__ == '__main__':
    run()
    


