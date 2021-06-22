from django.shortcuts import render
import requests

# Create your views here.

def home(request):

    error_message = ''
    message = ''
    message_class = '' 

    city = request.GET.get('city', 'Faridabad')

    if len(city) < 3 :
        error_message = 'Enter a valid city'
        city = 'Faridabad'
        url = f'http://api.openweathermap.org/data/2.5/find?q={city}&units=metric&appid= yourapikey'

        r = requests.get(url.format(city)).json()

        weather_data = {
                'name': r['list'][0]['name'],
                'temperature': r['list'][0]['main']['temp'],
                'description': r['list'][0]['weather'][0]['description'],
                'icon': r['list'][0]['weather'][0]['icon'],

            }  


    url = f'http://api.openweathermap.org/data/2.5/find?q={city}&units=metric&appid= yourapikey'

    r = requests.get(url).json()

    
    if len(r['list']) != 0:
        weather_data = {
                'name': r['list'][0]['name'],
                'temperature': r['list'][0]['main']['temp'],
                'description': r['list'][0]['weather'][0]['description'],
                'icon': r['list'][0]['weather'][0]['icon'],
            }   
    else:
        error_message = 'City does not exist.'
        city = 'Faridabad'
        url = f'http://api.openweathermap.org/data/2.5/find?q={city}&units=metric&appid= yourapikey'

        r = requests.get(url.format(city)).json()

        weather_data = {
                'name': r['list'][0]['name'],
                'temperature': r['list'][0]['main']['temp'],
                'description': r['list'][0]['weather'][0]['description'],
                'icon': r['list'][0]['weather'][0]['icon'],

            }  

    if error_message:
        message = error_message
        message_class = 'is-danger'


    context = {
        'weather_data': weather_data,
        'message': message,
        'message_class': message_class
    }
    print(context['weather_data'])
        
    return render(request, 'base/index.html', context)
