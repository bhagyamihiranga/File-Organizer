import os


def get_all_files():
     files = []
     
     for file in os.listdir():
         if not os.path.isfile(file) or file == "main.py" or file == "function.py":
             
             continue
         else:
             files.append(file)
     return files
 
def create_all_dir():
    dir_need = ['videos','music','image','text_file','genaral']
    
    dir_list = []
    
    for i in os.listdir():
        
        if os.path.isfile(i):
            continue
        else:
            dir_list.append(i)
    
    for file in dir_need:
        
        if file not in dir_list:
          
          os.mkdir(file)
            
    