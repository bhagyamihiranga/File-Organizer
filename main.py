import function
import os
categories = {
    "videos" : ['mp4','kmv'],
    "music" : ['mp3','mp2','mp1'],
    "image" : ['png','jpg','jpeg','webp'],
    "text_file" : ['txt','csv']
     
}


while True:
    function.create_all_dir()
    try:
        for i in function.get_all_files():
         extention = i.split('.')[-1]
         
         
        for index,value in categories.items():
            
            
            if extention in value:
                
                os.rename(f'./{i}',f'./{index}/{i}')
            else:
                os.rename(f'./{i}',f'./{'genaral'}/{i}')
                
    except Exception as e:
        continue       
            
    
    
    



