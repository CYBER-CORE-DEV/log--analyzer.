import time
import random
#print(time.localtime())
from datetime import datetime
print(datetime.now())

with open ("new2.txt","w",encoding="utf-8") as ofile:
                for i in range (1,50001,random.randint(1,20)):
                                        ofile.writelines(f"{datetime.now()} [error] [authservice] user authentication failed:invalid token.\n")