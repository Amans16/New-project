import csv, io
from django.shortcuts import render
from django.contrib import messages
from MainApp.models import Nifty_Data 
# Create your views here.
# one parameter named request
def Record_View(request):
    # declaring template
    template = "niftyupload.html"
    data = Nifty_Data.objects.all()
    # prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be BANKNIFTY,DATE,TIME,OPEN,HIGH,LOW,CLOSE,VOLUME',
        'records': data    
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Nifty_Data.objects.update_or_create(
            BANKNIFTY=column[0],
            DATE=column[1],
            TIME=column[2],
            OPEN=column[3],
            HIGH=column[4],
            LOW=column[5],
            CLOSE=column[6],
            VOLUME=column[7]        
        )
    context = {}
    return render(request, template, context)

