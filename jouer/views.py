from shlex import join

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    import random

    # Liste de mots
    mots = ['chat', 'chien', 'oiseau', 'poisson', 'lapin', 'tortue', 'souris', 'cheval', 'cochon', 'vache', 'mouton',
            'poulet', 'canard', 'oie', 'cygne', 'abeille', 'fourmi', 'araignée', 'guêpe', 'sauterelle', 'criquet',
            'scarabée', 'papillon', 'chenille', 'limace', 'escargot', 'serpent', 'lézard', 'grenouille', 'têtard',
            'crocodile', 'alligator', 'ours', 'loup', 'renard', 'raton laveur', 'blaireau', 'hermine', 'chauve-souris',
            'écureuil', 'castor', 'rat', 'furet', 'opossum', 'lynx', 'tigre', 'lion', 'léopard', 'panthère', 'jaguar',
            'guépard', 'éléphant', 'rhinocéros', 'hippopotame', 'girafe', 'chameau', 'dromadaire', 'kangourou', 'koala',
            'singe', 'gorille', 'chimpanzé', 'orang-outan', 'phoque', 'otarie', 'marsouin', 'dauphin', 'baleine',
            'requin', 'méduse', 'étoile de mer', 'crabe', 'homard', 'crevette', 'moule', 'huître', 'escargot de mer',
            'anguille', 'anguillon', 'truite', 'saumon', 'requin', 'morue', 'sole', 'carpe', 'brochet', 'perche',
            'grondin', 'rascasse', 'merlan', 'bar', 'sardine', 'hareng', 'anchois', 'thon', 'maquereau', 'crevette',
            'langoustine', 'homard', 'crabe', 'calamar', 'poulpe', 'méduse', 'étoile de mer', 'oursin', 'corail',
            'algue', 'fleur', 'arbre', 'herbe', 'fruit', 'légume', 'pain', 'viande', 'poisson', 'fromage', 'oeuf',
            'lait', 'eau', 'vin', 'bière', 'café', 'thé', 'chocolat', 'bonbon', 'gâteau', 'crème glacée', 'pizza',
            'hamburger', 'frites', 'salade', 'soupe', 'riz', 'nouilles', 'pâtes', 'pain', 'beurre', 'huile', 'sel',
            'poivre', 'sucre']

    # Liste aléatoire de 100 mots
    mot = '' + join(random.sample(mots, 1))
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
        return render(request, 'jouer/devine.html',{'mot': mot, 'motHidden': motHidden, 'vie':vie})
