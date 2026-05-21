from django.shortcuts import render
import random
import time

# Create your views here.

daily_special = [
    {"name": "Milkshake", "price": 21, "description": "With a cherry on top"},
    {"name": "Pepperoni pizza", "price": 25, "description": "With pineapples"},
    {"name": "Sparkling Mango Water", "price": 12, "description": "With Ice"},
    {"name": "Slushing Ice cream", "price": 9, "description": "With strawberry flavor"},
    
]


def main(request):
    '''Show the web page for the main.'''
 
 
    template_name = "restaurant/main.html"
    return render(request, template_name)
    
    




def order(request):
    
    special = random.choice(daily_special)
    
    context = {
        "special_name": special["name"],
        "special_price": special["price"],
        "special_description": special["description"],
    }

    return render(request, "restaurant/order.html", context)
    

    

    
def submit(request):
    return render(request, "restaurant/confirmation.html")
    
          
    
def confirmation(request):
    
    name = request.POST.get("name")
    phone = request.POST.get("phone")
    email = request.POST.get("email")
    
    total = 0
    ordered_items = []

    if "burgers" in request.POST:
        total += 15
        ordered_items.append("burgers")

    if "french_toast" in request.POST:
        total += 5
        ordered_items.append("french_toast")

    if "milkshake" in request.POST:
        total += 21
        ordered_items.append("milkshake")

    if "french_fries" in request.POST:
        total += 19
        ordered_items.append("french_fries")

    if "water" in request.POST:
        total += 3
        ordered_items.append("water")



    minutes = random.randint(30, 60)
    ready_timestamp = time.time() + (minutes * 60)
    ready_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ready_timestamp))
    
    context = {
        "items": ordered_items,
        "total": total,
        "name" : name,
        "phone": phone,
        "email": email,
        "ready_time": ready_time,
    }

    return render(request, "restaurant/confirmation.html", context)
    
    

    
    
    
    