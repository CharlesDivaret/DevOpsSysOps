from shlex import join

from django.http import HttpResponse
from django.shortcuts import render


def getMot():
    import random

    # Liste de mots
    mots = ['']
    
    return mots[random.randint(0, len(mots)-1)]

def index(request):
    
    # Liste aléatoire de 100 mots
    mot = getMot()
    motHidden = ""
    for i in range(len(mot)):
        motHidden += "*"
    request.session['mot'] = mot
    print(request.session.get('mot'))
    request.session['motHidden'] = motHidden
    request.session['vie'] = 8
    return render(request, 'jouer/home.html', {'mot': mot, 'motHidden': motHidden})


def devine(request):
    vie=request.session.get('vie')
    if vie > 0:
        mot = request.session.get('mot')
        letter = request.POST.get("letter")

        motHidden = request.session.get("motHidden")
        motHidden = list(motHidden)

        for i in range(len(mot)):
            if letter == mot[i]:
                motHidden[i]=letter
        motHidden="".join(motHidden)
        request.session['motHidden'] = motHidden

        if letter not in mot:
            vie-=1
        request.session['vie'] = vie

        if vie == 0:

            return render(request, 'jouer/devine.html',{'mot': mot, 'motHidden': motHidden, 'vie':0})

        return render(request, 'jouer/devine.html', {'mot': mot, 'motHidden': motHidden, 'vie': vie})
