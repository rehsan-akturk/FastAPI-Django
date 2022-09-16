from datetime import datetime, date,timezone
from fastapi import FastAPI, HTTPException
import psycopg2
import json





app = FastAPI()


############ connetion database ####################
try:
    conn = psycopg2.connect(
    database='xxxxxx', user='xxxxxx', password='xxxxx', host='xxxxx', port= 'xxxx')

    cursor = conn.cursor()
    print ("Connected!\n")
except:
    print ("UnConnected!\n")




#########get data all test limit 10#########
@app.get("/get/")
async def get():
    try:
        cursor.execute("SELECT * FROM driver_driver limit 50;")
    
        r = [dict(( cursor.description[i][0], value) \
           for i, value in enumerate(row)) for row in cursor.fetchall()]
      
                  
        return {
               "code":0, 
               "msg":"Success", 
               "limit": 50,
               "offset": 200,

               "headers": {"Content-Type": "application/json"},
               "body": json.dumps(r, indent=4, sort_keys=True, default=str,ensure_ascii=False)
             }
    except Exception as err:
        raise HTTPException(400, "failed to do something")

############get data with  params limit 50 offset 200 """"""""""""""
#http://127.0.0.1:8000/api?startDate=2022-01-26&endDate=2022-02-26&minScore=1.123123&maxScore=3.124123123&limit=50&offset=200
@app.get("/api")
async  def get_driver(startDate :str,endDate :str ,minScore :str ,maxScore:str,limit: int=50,offset: int=200):
    

    try:
       
        cursor.execute(f"SELECT * FROM driver_driver where  to_char(updated_at, 'YYYY-MM-DD') between '{startDate}'and '{endDate}'  and driving_score between '{minScore}' and '{maxScore}' order by updated_at desc limit '{limit}' offset '{offset}'   ;")
  ### Mapping rows with column names with dictionary #####
        r = [dict(( cursor.description[i][0], value) \
           for i, value in enumerate(row)) for row in cursor.fetchall()]
        
        return {
               "code":0, 
               "msg":"Success", 
               "limit": 50,
               "offset": 200,
               "headers": {"Content-Type": "application/json"},
                "body": json.dumps(r, indent=4, sort_keys=True, default=str,ensure_ascii=False)
             }
    except Exception as err:
        raise HTTPException(400, "failed to do something")



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)






	

	