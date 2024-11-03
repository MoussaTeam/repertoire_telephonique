liste_contact = [['Mecheh','Mouss','01354361'],['Bidon','Jo','01236545343']]



def ajouterContact () :
    name = input('Enter your name:')
    prenom = input('Enter your prenom :')
    telephone = input('Enter your phone number :')
    
    liste_contact.append([name,prenom,telephone])
    return None

def rechercherNom (nom) :
    i=0 
    for row in liste_contact : #parcours les lignes
        #print(row)
        #print(row[0])
        if row[0] == nom : 
            return i          
        i=i+1
    return None

            
            
    return indice

def rechehrchePrenom ( prenom) : 
    return indice 
 
def rechercheTel (tel) :
    return indice

indice = rechercherNom('Bidon')
print(liste_contact[indice])


