from collections import deque

def creation_queue():  
    create_stack = deque()
    create_stack.appendleft("close_connection")
    create_stack.appendleft("create_aggregated_table")
    create_stack.appendleft("create_dimension_tables")
    create_stack.appendleft("create_conn")
    return create_stack

#print(create_stack)

def deletion_queue(): 
    
    delete_stack = deque()

    delete_stack.appendleft("close_connection")
    delete_stack.appendleft("breakdown_tables")
    delete_stack.appendleft("create_conn")
    
    return delete_stack

#print(delete_stack) 

