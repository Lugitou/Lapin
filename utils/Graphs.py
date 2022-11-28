import matplotlib.pyplot as plt

rabbits = []
carrots = []
dates = []


def logRabbit(nbRabbit, date):
    rabbits.append(nbRabbit)
    dates.append(date)


def logCarrot(nbCarrot, date):
    carrots.append(nbCarrot)


def printPlot():
    plt.style.use('_mpl-gallery')

    # Plotting the Graph
    plt.plot(dates, rabbits)
    plt.plot(dates, carrots)
    plt.xlabel("Date")
    plt.ylabel("Nb de lapins et de carottes")
    plt.show()

