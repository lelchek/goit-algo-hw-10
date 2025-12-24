import pulp


def main():
    model = pulp.LpProblem("Maximize_Produce", pulp.LpMaximize)

    L = pulp.LpVariable("Lemonade", lowBound=0, cat="Integer")
    F = pulp.LpVariable("Juice", lowBound=0, cat="Integer")

    model += L + F, "Total_Produce"

    model += 2 * L + F <= 100, "Water"
    model += L <= 50, "Sugar"
    model += L <= 30, "Lemon_Juice"
    model += 2 * F <= 40, "Fruit_Pure"

    model.solve()

    result = {
        "lemonade": L.varValue,
        "fruit_juice": F.varValue,
        "total": pulp.value(model.objective),
    }

    return result


if __name__ == "__main__":
    main()
