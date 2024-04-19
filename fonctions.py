
def hotel_frais(nbr_nuits):
    return nbr_nuits*900
def Location_voiture_frais(nbr_jours):
    cout_location=350
    reduction=0
    if(nbr_jours>=3):
        reduction=200
    elif(nbr_jours>=7):
        reduction=500
    cout_jour_location=cout_location*nbr_jours-reduction
    return cout_jour_location

def vol_frais(nom_de_ville):
    ville={
        "Marrakech":350,
        "Paris":2000,
        "Oran":780,
        "Dakar":250,
        "Cartage":1820
    }
    return ville[nom_de_ville]
def voyage_frais(nm_ville,nbr_jours,nbr_nuits,autres_fais):
    return vol_frais(nm_ville)+hotel_frais(nbr_nuits)+Location_voiture_frais(nbr_jours)+autres_fais
