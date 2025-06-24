# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.





if __name__ == '__main__':
    N = int(input())
    my_list = [] 
    for _ in range(N):
        command =input().split()
        cmd =command[0]
        arg = (map(int,command[1:]))
        
        if cmd =="print":
           print(my_list)
        else:
            getattr(my_list,cmd)(*arg)           
    
        
         
        
    