from django.shortcuts import render, redirect
from .models import MyModel
from .forms import MyModelForm
import requests

def my_view(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            new_item = form.save()

            # Prepare the data for the Flask app
            data_to_send = {'name': new_item.name}  # Adjust the key based on your model fields

            # Make a POST request to the Flask app
            try:
                response = requests.post('http://3.93.36.227:5000/generate-sku', json=data_to_send)
                if response.status_code == 200:
                    sku = response.json().get('sku')
                    new_item.sku = sku  
                    new_item.save()
                else:
                    pass
            except requests.exceptions.RequestException as e:
                # Handle any exceptions while making the request
                pass

            return redirect('my_view')  
    else:
        form = MyModelForm()

    my_model_objects = MyModel.objects.all()
    context = {'my_model_objects': my_model_objects, 'form': form}
    return render(request, 'my_template.html', context)
