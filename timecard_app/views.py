from django.shortcuts import render
import pandas as pd

# Create your views here.

def index(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        if uploaded_file.name.endswith(('.csv', '.xlsx', '.xls')):
            data = pd.read_excel(uploaded_file) if uploaded_file.name.endswith(('.xlsx', '.xls')) else pd.read_csv(uploaded_file)

            # You can process or manipulate the data as needed

            return render(request, 'time_card_app/display_data.html', {'data': data})
        else:
            error_message = 'Invalid file format. Please upload a CSV or Excel file.'
            return render(request, 'time_card_app/index.html', {'error_message': error_message})
    return render(request, 'time_card_app/index.html')

def display_data(request):
    return render(request, 'time_card_app/display_data.html', {'data': None})
