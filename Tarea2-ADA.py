class Startup:
    def __init__(self, costo, roi):
        self.costo = costo
        self.roi = roi

def max_roi_investment(startups, capital):
    startups = [Startup(costo, roi) for costo, roi in startups]
    startups.sort(key=lambda x: x.roi / x.costo, reverse=True)  # Ordenar por ROI/costo decreciente

    def bnb(capital, suma, i, invertido):
        nonlocal max_roi, mejor

        if i == len(startups):
            if suma > max_roi:
                max_roi = suma
                mejor = invertido[:]
            return

        if capital >= startups[i].costo:
            # Explore el nodo izquierdo (incluir la startup)
            invertido[i] = 1
            bnb(capital - startups[i].costo, suma + startups[i].roi, i + 1, invertido)
            invertido[i] = 0

        # Explore el nodo derecho (excluir la startup)
        if suma + greedy(startups, i, capital) > max_roi:
            bnb(capital, suma, i + 1, invertido)

    def greedy(startups, i, capital):
        # Utilizacion de un enfoque Greedy para estimar el máximo ROI posible
        roi = 0
        capRestante = capital
        for i in range(i, len(startups)):
            if startups[i].costo <= capRestante:
                roi += startups[i].roi
                capRestante -= startups[i].costo
            else:
                roi += (startups[i].roi / startups[i].costo) * capRestante
                break
        return roi

    max_inversiones = [0] * len(startups)
    max_roi = 0
    mejor = [0] * len(startups)
    bnb(capital, 0, 0, max_inversiones)

    return [startup for i, startup in enumerate(startups) if mejor[i]], max_roi


startups = [(10, 50), (5, 30), (8, 20), (3, 10), (15, 30), (5, 8), (8, 20)]
initial_capital = 30
mejores_inversiones, max_roi = max_roi_investment(startups, initial_capital)

print("Mejores inversiones:")
for startup in mejores_inversiones:
    print("(" + str(startup.costo) + "," + str(startup.roi) + ")")

print("Máximo ROI obtenido:", max_roi)