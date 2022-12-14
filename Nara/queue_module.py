from collections import deque


def create_queue(*args): 
    '''Creates a queue from given tasks
    Args: 
      *args: can be tasks or int values 
    
    Returns:
      create_stack: dequeu object containing the list of tasks (and ints for pauses) that needs to be completed. 
    '''
    
    create_stack = deque() #creates an empty deque
    list_of_arguments = list() #instanciates an empty list
    
    for j in args: #appends each argument in order to the list
        list_of_arguments.append(j)
    
    list_of_arguments.reverse() #reverses the list
    
    for i in list_of_arguments: #appendsleft every item in the queue so they're in proper order. 
        create_stack.appendleft(i)
    
    return create_stack #returns the created stack. 


'''def deletion_queue(): 
    
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
    
'''