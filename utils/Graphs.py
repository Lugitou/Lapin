import matplotlib.pyplot as plt

rabbits = []
carrots = []
dates = []

# On marque les nombre de lapins chaque semaine
# On fait correspondre un numéro de semaine
def logRabbit(nbRabbit, date):
    rabbits.append(nbRabbit)
    dates.append(date)

# On marque le nombre de carotte chaque semaine
# Pas besoin des dates ici, elles correspondent aux dates des lapins
def logCarrot(nbCarrot):
    carrots.append(nbCarrot)

# Fonction permettant d'afficher le graphique avec les données stockées pendant la simulation
def printPlot():
    plt.style.use('_mpl-gallery')

    # Plotting the Graph
    plt.plot(dates, rabbits, "b-", label="Rabbits")
    plt.plot(dates, carrots, "r-", label="Carrots")
    plt.ylabel("Nb de lapins et de carottes")
    plt.xticks(dates, rotation=45)
    plt.show()

