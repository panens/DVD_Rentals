from collections import deque


def creation_queue():  
    
    create_stack = deque() #creates an empty deque
    create_stack.appendleft("close_conn") #adds last task to be completed first
    create_stack.appendleft("create_agg") 
    create_stack.appendleft("create_dim")
    create_stack.appendleft("create_conn") #adds tasks until the first one to be executed
    
    return create_stack

def deletion_queue(): 
    
    delete_stack = deque()
    delete_stack.appendleft("close_conn")
    delete_stack.appendleft("breakdown")
    delete_stack.appendleft("create_conn")
    
    return delete_stack

def full_queue_time(x:int):
    
    full_stack = deque() #creates an empty deque
    full_stack.appendleft("close_conn") #adds last task to be completed first
    full_stack.appendleft("breakdown")
    full_stack.appendleft(x) #the idea is to give a number to the queue that will determine how long the executor will hold te connection 
    full_stack.appendleft("create_agg") 
    full_stack.appendleft("create_dim")
    full_stack.appendleft("create_conn") #adds tasks until the first one to be executed
    
    return full_stack
    
