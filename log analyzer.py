import time
import random
#print(time.localtime())
from datetime import datetime
q=datetime.now()

 
                                        
                                                                                     
with open ("new2.txt","r",encoding="utf-8") as p:
        for lines  in p:
                lines.strip()
log_level_counts={}
error_message_counts={}                                        
def extractor(lines):
        with open ("new2.txt","r",encoding="utf-8") as p:
                for lines  in p:
                        x=lines.split(" ")
                        level=x[2]
                        message=x[4:6]
                        if level =="[error]":
                                if message in error_message_counts:
                                        error_message_counts[message]+=1
                                else:
                                        error_message_counts[message]=1
with open ("new2.txt","r",encoding="utf-8") as p:
                for lines  in p:
                        x=lines.split(" ")
                        level=x[2]
                        message=x[6]
                        if level =="[error]":
                                if message in error_message_counts:
                                        error_message_counts[message]+=1
                                else:
                                        error_message_counts[message]=1                                        
print("final errors count:",error_message_counts) 
sorted_errors=sorted(error_message_counts.items(),key=lambda item:item[1],reverse=True)
top_3_ones=sorted_errors[:3]
for index,(msg,count) in enumerate(top_3_ones,start=1):
        print(f"{index}. {msg} occured {count} times.")
with open ("log_analysis file.txt","w") as fb:
        fb.write("------------------system logs report-------------------\n")
        fb.write("==================log level summary\n============")
        for level,count in log_level_counts.items():
                fb.write(f"{level}---{count} occurences\n")     
        fb.write("===========top three occurences==========\n")  
        for index,(msg,count) in enumerate(top_3_ones,start=1):
            fb.write(f"{index}. {msg} occured {count} times.")                                 

r=datetime.now()
print(f"program executed in  {(r-q)} seconds.")

                
                       

        

