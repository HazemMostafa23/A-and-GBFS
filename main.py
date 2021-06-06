

adjacent_list = {
    'A' : ['S', 'T','Z'],
    'S' :['A','F','O','R'],
    'F':['B','S'],
    'B':['F','G','P','U'],
    'U':['B','H','V'],
    'H':['E','U'],
    'E':['H'],
    'G':['B'],
    'Z':['A','O'],
    'O':['S','Z'],
    'R':['C','P','S'],
    'P':['B','C','R'],
    'C':['D','P','R'],
    'D':['C','M'],
    'M':['D','L'],
    'L':['M','T'],
    'T':['A','L'],
    'N':['I'],
    'I':['N','V'],
    'V':['I','U']
    }

cost_list = {
    'Z': 374,
    'A': 366,
    'O': 380,
    'S': 253,
    'T': 329,
    'L': 244,
    'M': 241,
    'D': 242,
    'C': 160,
    'P': 100,
    'R': 193,
    'B': 0,
    'G': 77,
    'U': 80,
    'H': 151,
    'E': 161,
    'V': 199,
    'I': 226,
    'N': 234,
    'F': 176

}
E = [['A', 'S', 140], ['A', 'Z', 75], ['A', 'T', 118], ['S', 'F', 99], ['S', 'O', 151], ['F', 'B', 211], ['R', 'S', 80],
     ['R', 'P', 97], ['R', 'C', 146], ['P', 'B', 101], ['P', 'C', 138], ['B', 'G', 90], ['B', 'U', 85], ['U', 'H', 98],
     ['U', 'V', 142], ['H', 'E', 86], ['V', 'I', 92], ['I', 'N', 87], ['Z', 'O', 71], ['T', 'L', 111], ['L', 'M', 70],
     ['M', 'D', 75], ['D', 'C', 120]]


def A_star(intial_value, final):
    explored = []
    frontiers = []
    path_cost = {}

    cost = 0
    tcost = 0

    while (True):
        if (intial_value == final):
            explored.append(intial_value)
            break

        explored.append(intial_value)

        for i in range(len(adjacent_list[intial_value])):
            if adjacent_list[intial_value][i] not in explored:
                frontiers.append(adjacent_list[intial_value][i])

        for i in range(len(frontiers)):
            for j in range(len(E)):
                if (frontiers[i] in E[j] and intial_value in E[j]):
                    x = {frontiers[i]: (E[j][2] + tcost)}
                    path_cost.update(x)

        cost = tcost + cost_list.get(frontiers[0]) + path_cost.get(frontiers[0])
        index = 0
        print("current letter" + ": " + intial_value)
        for i in range(len(frontiers)):
            if (cost > cost_list.get(frontiers[i]) + path_cost.get(frontiers[i])):
                cost = cost_list.get(frontiers[i]) + path_cost.get(frontiers[i])
                index = i

        tcost = path_cost.get(frontiers[index])

        for x in range(len(frontiers)):
            print(frontiers[x] + ":" + str(path_cost.get(frontiers[x]) + cost_list.get(frontiers[x])))

        intial_value = frontiers[index]
        frontiers.remove(intial_value)
        path_cost.pop(intial_value)

    print("The final path is ")
    for x in range(len(explored)):
        print(explored[x])
    print("The total cost equals: " + str(cost))


def gbfs(intial_value, final):
    explored = []
    frontiers = []

    cost = 0
    while (True):
        if (intial_value == final):
            explored.append(intial_value)
            cost = cost + cost_list.get(intial_value)
            break

        explored.append(intial_value)
        cost = cost + cost_list.get(intial_value)
        for i in range(len(adjacent_list[intial_value])):
            if adjacent_list[intial_value][i] not in explored:
                frontiers.append(adjacent_list[intial_value][i])

        minval = cost_list.get(frontiers[0])
        index = 0
        for i in range(len(frontiers)):
            if (minval > cost_list.get(frontiers[i])):
                minval = cost_list.get(frontiers[i])
                index = i

        intial_value = frontiers[index]

        frontiers.remove(intial_value)

    for x in range(len(explored)):
        print(explored[x])
    print(cost)



def callmain():
    print(" 1.  GBFS \n 2. A* \n To Exit Out of the Program Enter -1")
    c = int(input())
    print("Enter your starting Node")
    sp=input()
    if c == 1:

        gbfs(sp, 'B')
        print("\nDo you want to try a different implementation?")
        callmain()
    elif c == 2:

        A_star(sp, 'B')
        print("\nDo you want to try a different implementation?")
        callmain()



def main():
    print("Welcome to Our Simple Graph Implementation Program")
    print("Our Program is based on the Arad to Bucharest traversal Problem")
    print("Choose Which Implementation Method You'd Like : ")
    callmain()


main()