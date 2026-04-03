# Données d'émissions en gCO2e par unité
EMISSIONS = {
    'emails_simples': 4,       # par email
    'emails_pj': 19,           # par email avec pièce jointe
    'streaming_sd': 36,        # par heure
    'streaming_hd': 100,       # par heure
    'recherches': 7,           # par recherche
    'stockage_cloud': 10       # par Go par mois
    'jeu_en_ligne': 80
    
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

Noah = { 'emails_simples': 8,
'emails_pj': 5,
'streaming_sd': 10,
'streaming_hd': 25,
'recherches': 500,
'stockage_cloud': 15

}

#############################################################################
# Écrire le code de la fonction calculer_empreinte de la question 1         #
#############################################################################
def calculer_empreite(utilisateur):
    total=0
    
    for i,j in utilisateur.items():
        if i in EMISSIONS.keys():
            
            total+=j*EMISSIONS[i]
    return total

#print(calculer_empreite(utilisateur1))
#############################################################################
# Écrire le code de la fonction classer_par_impact de la question 2         #
#############################################################################
def impact(utilisateur):
    memo={'fort':[],'moyen':[],'faible':[]}
    for i,j in utilisateur.items():
        if i in EMISSIONS.keys():
            cal=j*EMISSIONS[i]
            if cal>=1000:
                memo['fort'].append(i)
            elif cal<1000 and cal>=200:
                memo['moyen'].append(i)
            else:
                memo['faible'].append(i)
    return memo

#print(impact(utilisateur2))
        

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
    assert diff['emails_pj']==0
    
    diff=comparer(utilisateur1, utilisateur2)
    
    assert diff['streaming_sd']==-10
    
#print(test_comparer())
    


#############################################################################
# Fonction fournie pour la question 4                                       #
#############################################################################
def comparer_v2(u1, u2):
    """Compare les émissions de deux utilisateurs pour toutes les activités.
    Renvoie un dictionnaire avec, pour chaque activité, l'écart des émissions
    sous forme de pourcentage, en proportion de la première émission."""
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
            
            ecarts[activite] = (emission2 - emission1)/emission1 * 100
    return ecarts

print(comparer_v2(utilisateur4 , utilisateur2))
print(comparer_v2(utilisateur2, utilisateur4))