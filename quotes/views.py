from django.shortcuts import render
import random

# MUST BE GLOBAL
quotes = [
    "The only thing we have to fear is fear itself.",
    "We must be the great arsenal of democracy.",
    "The only limit to our realization of tomorrow will be our doubts of today.",
    "Courage is not the absence of fear, but rather the assessment that something else is more important than fear.",
    "A smooth sea never made a skilled sailor."
]

images = [
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTIqG9BfeNLaWZ9y-nd_R9xZujJDZHKTQ3BQs6shH2okAmvFRMUnJzgoYetn4MdonE31sxzyh3XkwPe2ymBz4SbL-tw8Z-IQDCIQRC0bgmy&s=10",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQkyFov7RbGHLAeFpEjfhosCLGN6mUuCcNOey2phutl4TLH-U3ZEJQvtd4QRd-tTEko72iDYdtD3S9hpTGPHKbr2Q-z8zqXZbmQJ7TA8TsCHA&s=10",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQVnkqb0RH75LkcALDOv04hqj1oqFeAnj2DP597OGqh5gJ8YvpSRvsda8QttZBOQ_0Rlf7s1y3JTo8E6HJNKibk8Zak3FU-jyXk02rXINRItQ&s=10",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Recueil._Portraits_de_Franklin_Delano_Roosevelt_-_btv1b10336803v_%2803_of_19%29.jpg/250px-Recueil._Portraits_de_Franklin_Delano_Roosevelt_-_btv1b10336803v_%2803_of_19%29.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Recueil._Portraits_de_Franklin_Delano_Roosevelt_-_btv1b10336803v_%2804_of_19%29.jpg/960px-Recueil._Portraits_de_Franklin_Delano_Roosevelt_-_btv1b10336803v_%2804_of_19%29.jpg"
]

def quote(request):
    index = random.randint(0, len(quotes) - 1)

    context = {
        "quote": quotes[index],
        "image": images[index],
    }

    return render(request, "quotes/quote.html", context)


def show_all(request):
    context = {
        "quotes": quotes,
        "images": images,
    }
    return render(request, "quotes/show_all.html", context)


def about(request):
    return render(request, "quotes/about.html")