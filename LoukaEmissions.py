# Données d'émissions en gCO2e par unité
EMISSIONS = {
    'emails_simples': 4,       # par email
    'emails_pj': 19,           # par email avec pièce jointe
    'streaming_sd': 36,        # par heure
    'streaming_hd': 100,       # par heure
    'recherches': 7,           # par recherche
    'stockage_cloud': 10,      # par Go par mois
    'telechargement': 200      # par Go
}

# Exemples d'utilisateurs pour les tests
utilisateur1 = {
    'emails_simples': 150,
    'emails_pj': 20,
    'streaming_sd': 10,
    'streaming_hd': 25,
    'recherches': 500,
    'stockage_cloud': 15
}

utilisateur2 = {
    'streaming_hd': 15,
    'emails_simples': 100,
    'recherches': 10
}

utilisateur3 = {
    'emails_simples': 50,
    'emails_pj': 5,
    'streaming_sd': 30,
    'streaming_hd': 5,
    'recherches': 200,
    'stockage_cloud': 5
}

utilisateur4 = {
    'emails_simples': 100,
    'recherches': 50
}

utilisateur5 = {
    'emails_simples': 50,
    'recherches': 100
}

utilisateur6 = {}

utilisateur7 = {
    'ABCDEFG' : 1234567    
}

louka = {
    'telechargement' : 120,
    'recherches': 450,
    'stockage_cloud': 35.82,
    'streaming_hd': 8,
}

#############################################################################
# Écrire le code de la fonction calculer_empreinte de la question 1         #
#############################################################################

def calculer_empreinte(user):
    assert type(user) == dict, "user n'est pas un dictionnaire"
    emission = 0
    for key,value in user.items():
        try:
            emission += EMISSIONS[key] * value
        except: 
            KeyError()
    return emission

assert calculer_empreinte(utilisateur1) == 7490
assert calculer_empreinte(utilisateur7) == 0

#############################################################################
# Écrire le code de la fonction classer_par_impact de la question 2         #
#############################################################################

def classer_par_impact(user, classement={"faible":[],"moyen":[],"fort":[]}):
    assert type(user) == dict, "user n'est pas un dictionnaire"
    for key,value in user.items():
        emission = 0
        try:
            emission += EMISSIONS[key] * value
        except:
            KeyError() 
        if emission < 200:
            classement["faible"].append(key)
        elif 200 <= emission and emission < 1000:
            classement["moyen"].append(key)
        elif emission >= 1000:
            classement["fort"].append(key)
    return classement

assert classer_par_impact(utilisateur2) == {'faible': ['recherches'], 'moyen': ['emails_simples'], 'fort': ['streaming_hd']}

#############################################################################
# Fonction fournie pour la question 3                                       #
#############################################################################

def comparer(u1, u2):
    """Compare les émissions de deux utilisateurs pour toutes les activités.
    Renvoie un dictionnaire avec, pour chaque activité, la différence des
    émissions (émissions de l’utilisateur 2 moins celles de l’utilisateur 1).
    Si une activité est absente chez un utilisateur, on considère que
    son émission vaut 0."""
    differences = {}
    for activite in EMISSIONS:
        quantite1 = 0
        quantite2 = 0
        if activite in u1:
            quantite1 = u1[activite]
        if activite in u2:
            quantite2 = u2[activite]
        emission1 = quantite1 * EMISSIONS[activite]
        emission2 = quantite2 * EMISSIONS[activite]
        differences[activite] = emission2 - emission1
    return differences

def test_comparer():
    diff = comparer(utilisateur4, utilisateur5)
    assert diff['emails_simples'] == -200  # (50-100) * 4
    assert diff['recherches'] == 350     # (100-50) * 7
    
    # Ajouter vos tests ci-dessous avec justifications
    diff = comparer(utilisateur1, utilisateur2) 
    assert diff['stockage_cloud'] == -150 # (0-15) * 10 si un utilisateur n'utilise pas un service, son emission est égale à 0
    diff = comparer(utilisateur6, utilisateur2)
    assert diff['stockage_cloud'] == 0 # (0-0) * 10 si deux utilisateurs n'utilisent pas un service, leur emission est égale à 0, tout comme la différence

test_comparer()

#############################################################################
# Fonction fournie pour la question 4                                       #
#############################################################################
def comparer_v2(u1, u2):
    """Compare les émissions de deux utilisateurs pour toutes les activités.
    Renvoie un dictionnaire avec, pour chaque activité, l'écart des émissions
    sous forme de pourcentage, en proportion de la première émission."""
    assert type(u1) == dict and type(u2) == dict, "u1 et u2 ne sont pas des dictionnaires" 
    ecarts = {}
    for activite in EMISSIONS:
        quantite1 = 0
        quantite2 = 0
        if activite in u1:
            quantite1 = u1[activite]
        if activite in u2:
            quantite2 = u2[activite]
        emission1 = quantite1 * EMISSIONS[activite]
        emission2 = quantite2 * EMISSIONS[activite]
        try:
            ecarts[activite] = (emission2 - emission1)/emission1 * 100
        except:
            ZeroDivisionError()
    return ecarts

assert comparer_v2(utilisateur6,utilisateur3) == {}
assert comparer_v2(utilisateur3,utilisateur6) == {'emails_simples': -100.0, 'emails_pj': -100.0, 'streaming_sd': -100.0, 'streaming_hd': -100.0, 'recherches': -100.0, 'stockage_cloud': -100.0}
assert comparer_v2(utilisateur2,utilisateur3) == {'emails_simples': -50.0, 'streaming_hd': -66.66666666666666, 'recherches': 1900.0}



assert calculer_empreinte(louka) == 28308.2
