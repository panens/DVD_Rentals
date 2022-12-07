#worker / executer is the same function in this project so I am naming it execute_queue()

from collections import deque
import time


def execute_queue(queue): 
    '''Executes a queue given to the function
    Args: 
      queue: a queue that contains tasks (or maybe an int for pause time) 
    '''
    counter = 0 #set the counter at 0 so we can know first time through the for loop that we are on the first task
    #this is done because the first task needs to be connection, and that task gives us the cur and conn object
    #that all the other tasks need to use
    
    
    for task in queue: 
        if type(task) == int: #if type of task is int, we pause the queue for that many seconds
            #for minutes we can multiply by 60, and so on. 
            print(f'Queue paused for {task} seconds')
            time.sleep(task)
            
        else: 
            if counter == 0: #if it is the first task, we need to save the cur and conn objects and run without inputs
                cur, conn = task.run()
                counter = counter + 1
            else: 
                task.run(cur,conn) #if it is not the first task we need to use the cur and conn objects as inputs. No output is needed per task. 
                counter = counter + 1