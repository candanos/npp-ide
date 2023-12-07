
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")

try:
  print("Hello" + x)  # hata alan satira kadar çalısir. Hata alınan satirdan sonrası atlanır.
  print("Hello again.")   
except Exception as e:
  print("Something went wrong, Exception is: " + str(e)) # try fail olursa calisir.
else:
  print("Nothing went wrong")   # try success olursa calisir. 
finally: 
  print("try block runned.")  # her durumde calisir. 
  
  # except Exception, e: # work on python 2.x
    # logger.error('Failed to upload to ftp: '+ str(e))    
