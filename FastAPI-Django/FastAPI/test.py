import json
import requests


#requests with parameters 
url="http://127.0.0.1:8000/api?startDate=2022-01-20&endDate=2022-02-10&minScore=1.1&maxScore=3.12"
res = requests.get(url)
print(res)
    
    

           
                
             