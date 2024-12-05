"""
Code Syracuse : Analyse et visualisation de la suite de Syracuse.
"""

# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """Affiche le graphique de la suite de Syracuse.

    Cette fonction génère un graphique interactif à l'aide de Plotly pour visualiser
    les valeurs d'une suite de Syracuse donnée.

    Args:
        lsyr (list): La suite de Syracuse à afficher.
    """
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({
        'layout': {
            'title': {'text': title},
            'xaxis': {'title': {'text': "x"}},
            'yaxis': {'title': {'text': "y"}},
        }
    })

    x = list(range(len(lsyr)))
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color="blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
#######################

def syracuse_l(n):
    """Génère la suite de Syracuse pour une source donnée.

    Cette fonction calcule la suite de Syracuse en appliquant les règles :
    - Si n est pair : n = n // 2
    - Si n est impair : n = 3 * n + 1
    La suite s'arrête lorsque n atteint 1.

    Args:
        n (int): La source de la suite (doit être un entier positif).

    Returns:
        list: La suite de Syracuse générée.
    """
    l = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        l.append(n)
    return l

def temps_de_vol(l):
    """Calcule le temps de vol d'une suite de Syracuse.

    Le temps de vol correspond au nombre total de valeurs dans la suite,
    incluant la valeur finale 1.

    Args:
        l (list): La suite de Syracuse.

    Returns:
        int: Le temps de vol de la suite.
    """
    return len(l)

def temps_de_vol_en_altitude(l):
    """Calcule le temps de vol en altitude d'une suite de Syracuse.

    Le temps de vol en altitude est défini comme le nombre de termes successifs
    où la valeur est supérieure ou égale à la valeur initiale de la suite.

    Args:
        l (list): La suite de Syracuse.

    Returns:
        int: Le temps de vol en altitude.
    """
    n0 = l[0]
    count = 0
    for value in l:
        if value >= n0:
            count += 1
        else:
            break
    return count

def altitude_maximale(l):
    """Détermine l'altitude maximale d'une suite de Syracuse.

    L'altitude maximale correspond à la valeur la plus élevée atteinte
    au cours de la suite.

    Args:
        l (list): La suite de Syracuse.

    Returns:
        int: La valeur maximale atteinte dans la suite.
    """
    return max(l)

#### Fonction principale ####

def main():
    """Point d'entrée principal du programme.

    Cette fonction génère et affiche les informations des suites de Syracuse
    pour plusieurs valeurs de départ. Elle inclut :
    - La suite complète.
    - Le temps de vol.
    - Le temps de vol en altitude.
    - L'altitude maximale.
    """
    # Vos appels à la fonction secondaire ici
    n_values = [3, 4, 5, 6, 15]
    for n in n_values:
        lsyr = syracuse_l(n)
        print(f"Suite de Syracuse pour n = {n} : {lsyr}")
        print(f"Temps de vol pour n = {n} : {temps_de_vol(lsyr)}")
        print(f"Temps de vol en altitude pour n = {n} : {temps_de_vol_en_altitude(lsyr)}")
        print(f"Altitude maximale pour n = {n} : {altitude_maximale(lsyr)}")
        print("-" * 50)
        # Pour visualiser le graphique, décommentez la ligne suivante :
        # syr_plot(lsyr)

if __name__ == "__main__":
    main()
