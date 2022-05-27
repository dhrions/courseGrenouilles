# nbGrenouilles = int(input())
nbGrenouilles = int(input("nbGrenouilles : "))
positionsGrenouilles = [0] * (nbGrenouilles + 1)
print(positionsGrenouilles)

nbVictoires = [0] * (nbGrenouilles + 1)

# nbTours = int(input())
nbTours = int(input("nbTours : "))
idGrenouilleEnTete = 0

for idTour in range(nbTours):
    # Dans la boucle "for" suivante, on vérifie si une grenouille est strictement devant les autres au début du tour.
    for loop2 in range(1, nbGrenouilles + 1):
        if positionsGrenouilles[loop2] > positionsGrenouilles[idGrenouilleEnTete]:
            idGrenouilleEnTete = loop2
            nbVictoires[loop2] += 1
            # idGrenouilleDistance = input().split(" ")
    idGrenouilleDistance = input("idGrenouille + distance").split(" ")
    idGrenouille = int(idGrenouilleDistance[0])
    distance = int(idGrenouilleDistance[1])
    positionsGrenouilles[idGrenouille] += distance
    print(positionsGrenouilles)

print(positionsGrenouilles)
print(nbVictoires)

idVainqueur = 1
for loop3 in range(2, nbGrenouilles + 1):
    if nbVictoires[loop3] > nbVictoires[idVainqueur]:
        idVainqueur = loop3

print(idVainqueur)
