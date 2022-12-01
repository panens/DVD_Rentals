from collections import deque


def creation_queue():  
    
    create_stack = deque()
    create_stack.appendleft("close_conn")
    create_stack.appendleft("create_agg")
    create_stack.appendleft("create_dim")
    create_stack.appendleft("create_conn")
    
    return create_stack

create_stack = creation_queue()
print(create_stack)

def deletion_queue(): 
    
    delete_stack = deque()
    delete_stack.appendleft("close_conn")
    delete_stack.appendleft("breakdown")
    delete_stack.appendleft("create_conn")
    
    return delete_stack

delete_stack = deletion_queue()
print(delete_stack) 

