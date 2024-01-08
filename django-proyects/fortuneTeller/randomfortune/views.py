import random
from django.shortcuts import render

# Create your views here.
def fortune(request):
    fortuneList = [
    "La suerte favorece a los valientes.",
    "Nada es imposible para un corazón dispuesto.",
    "El futuro pertenece a aquellos que creen en la belleza de sus sueños.",
    "La vida es 10% lo que nos sucede y 90% cómo reaccionamos ante ello.",
    "El fracaso es la oportunidad de comenzar de nuevo, pero con más inteligencia.",
    "La perseverancia es la madre del éxito."
]
    fortune = random.choice(fortuneList)
    context = {'fortune': fortune}
    return render(request, 'randomfortune/fortune.html', context)