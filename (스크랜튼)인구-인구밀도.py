from matplotlib.pylab import plot, show, scatter

def main():
    #init
    population = [9705, 3400, 2450, 2939, 1493, 1518, 1154, 304, 1521, 1619, 2180, 1820, 1790, 2674, 3356, 653, 13031]
    population_density = [16034, 4416, 2773, 2764, 2980, 2813, 1088, 653, 90, 219, 265, 226, 145, 141, 318, 353, 1279]
    gangwon = 8
    seoul = 0
    
    area = []
    for i in range(len(population)):
        square = (1/population_density[i]) * population[i] * 1000
        area.append(square)

    X = []
    Y = []
    for i in range(20000):
        X.append(i)
        den_gangwon = density(population[gangwon] - i, area[gangwon])
        den_seoul = density(population[seoul] - i, area[seoul])
        population_density[gangwon] = den_gangwon
        population_density[seoul] = den_seoul
        Y.append(variance(population_density))

    plot(X,Y)
    show()


def average(data):
    sum_x = sum(data)
    average = sum_x / len(data)
    
    return average

def variance(data):
    aver = average(data)
    
    variance = 0
    for x in data:
        variance += x**2 - aver**2
    variance /= len(data) - 1
    
    return variance

def density(population, area):
    density = population * 1000 / area
    return density

if __name__ == "__main__":
    main()
