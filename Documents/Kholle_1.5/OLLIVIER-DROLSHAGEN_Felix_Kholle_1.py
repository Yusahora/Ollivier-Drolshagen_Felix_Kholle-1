#!/usr/local/bin/python3

# Import module
import argparse
import csv

# Variables
listeValues = []
fileList = 'liste.csv'


#Functions déclaration

#Write in fileList
def write(msg):
    with open(fileList, 'w') as csv_fileList:
        write = csv.writer(csv_fileList, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        write.writerow(msg)

#read in fileList
def read():
    with open(fileList, 'r') as csv_fileList:
        reader = csv.reader(csv_fileList)
        for row in reader:
            for i in range(len(row)):
                if len(row) > 0:
                    listeValues.append(row[i])

#suppr all item in the list
def suppr():
    while len(listeValues) != 0:
        print(listeValues)
        del listeValues[0]
    write(listeValues)
    print('la liste est maintenant vide')

#min value
def min(array):
    min_value = array[0]
    for value in array:
        if value < min_value:
            min_value = value
    return min_value

#max value
def max(array):
    max_value = array[0]
    for value in array:
        if value > max_value:
            max_value = value
    return max_value

#arguments
parser = argparse.ArgumentParser(conflict_handler='resolve')
parser.add_argument("-l", action="store_true", help="Affiche le contenu de la liste")
parser.add_argument("-a", nargs="*", help="Ajoute des items à la liste")
parser.add_argument("-c", action="store_true", help="Supprime la liste")
parser.add_argument("-s", "--max", action="store_true", help="Affiche le plus grand nombre de la liste")
parser.add_argument("-s", "--min", action="store_true", help="Affiche le plus petit nombre de la liste")
parser.add_argument("-s", "--moy", action="store_true", help="Affiche la moyenne des éléments de la liste")
parser.add_argument("-s", "--sum", action="store_true", help="Affiche la somme des éléments de la liste")
parser.add_argument("-t", "--desc", action="store_true", help="Trie la liste de manière décroissante")
parser.add_argument("-t", "--asc", action="store_true", help="Trie la liste de manière croissante")
parser.add_argument("--help", action="store_true", help="Affiche l'aide")
args = parser.parse_args()

if args.l:
    read()
    print(listeValues)

elif args.a:
    read()
    for value in args.a:
        if value.isnumeric():
            listeValues.append(value)
            write(listeValues)
            print('la valeur', value, 'a été ajouter')
        else:
            print('Entrez une valeur correcte')
            exit()
            
elif args.c:
    suppr()

elif args.max:
    read()
    highest = max(listeValues)
    print('La plus grosse valeur est', highest)

elif args.min:
    read()
    lowest = min(listeValues)
    print('La plus petite valeur est', lowest)

elif args.moy:
    read()
    values = [int(nbr) for nbr in listeValues]
    moy = (sum(values)/len(listeValues))
    print('la moyenne est de ', moy)

elif args.sum:
    read()
    values = [int(nbr) for nbr in listeValues]
    print('la somme est de ', sum(values))

elif args.desc:
    read()
    values = [int(nbr) for nbr in sorted(listeValues, key=int, reverse=True)]
    print('Trie de manière decroissante:', values)

elif args.asc:
    read()
    values = [int(nbr) for nbr in sorted(listeValues, key=int)]
    print('Trie de manière croissante:', values)

else:
    parser.print_help()