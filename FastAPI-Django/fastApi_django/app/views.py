from audioop import reverse
import json
from django.shortcuts import  render,redirect
import requests
from django.urls import reverse
from django.views import View
from django.http import Http404


# # Create your views here.

############# get driver list random limit 50  ###################
class Driverall(View):
    def get(self,request):
        try:
            drivers = requests.get(f"http://127.0.0.1:8000/get")
     
            _drivers=drivers.json()
            drivers=_drivers['body']
        
            return render(request, 'driver.html', {
                  "drivers": json.loads(drivers)
                
            })
        except drivers.DoesNotExist:
              raise Http404


#############get parameters link ##################  
class Drivers(View):
    def get(self,request,startDate ,endDate ,minScore  ,maxScore):
        try:
           drivers_call = requests.get(f"http://127.0.0.1:8000/api?startDate={startDate}&endDate={endDate}&minScore={minScore}&maxScore={maxScore}")
        

           _drivers_call=drivers_call.json()
           drivers_calls=_drivers_call['body']
          
           

           return render(request, 'driver_filter.html', {
                  "drivers_calls": json.loads(drivers_calls)
                
            })
        except drivers_call.DoesNotExist:
              raise Http404




############# html button select all params filter and reverse Drivers class  #####################
class Button(View):
        try:
                def post(self,request):
                    startDate=request.POST.get('startDate')
                    endDate=request.POST.get('endDate')
                    minScore=request.POST.get('minscore')
                    maxScore=request.POST.get('maxscore')
                    redirect_path=reverse('driver',kwargs={'startDate':str(startDate),'endDate':str(endDate),'minScore':str(minScore),'maxScore':str(maxScore)})

                    return redirect(redirect_path)
        except redirect_path.DoesNotExist:
               raise Http404

    



   
