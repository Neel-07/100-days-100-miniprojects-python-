import copy
import sys

TOTAL_DISKS = 5
COMPLETE_TOWER = list(range(TOTAL_DISKS, 0, -1))

def main():
    towers = {'A': copy.copy(COMPLETE_TOWER), 'B': [], 'C': []}
    while True:
        displayTowers(towers)
        fromTower, toTower = askForPlayerMove(towers)
        moveDisk(towers, fromTower, toTower)

def askForPlayerMove(towers):
    while True:
        response = input('Enter the letters of "from" and "to" towers, or QUIT: ').upper().strip()
        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        if isValidMove(response, towers):
            return response[0], response[1]

def isValidMove(response, towers):
    if response not in ('AB', 'AC', 'BA', 'BC', 'CA', 'CB'):
        print('Enter one of AB, AC, BA, BC, CA, or CB.')
        return False

    fromTower, toTower = response[0], response[1]

    if len(towers[fromTower]) == 0:
        print('You selected a tower with no disks.')
        return False
    elif len(towers[toTower]) == 0:
        return True
    elif towers[toTower][-1] < towers[fromTower][-1]:
        print("Can't put larger disks on top of smaller ones.")
        return False
    else:
        return True

def moveDisk(towers, fromTower, toTower):
    disk = towers[fromTower].pop()
    towers[toTower].append(disk)
    if COMPLETE_TOWER in (towers['B'], towers['C']):
        displayTowers(towers)
        print('You have solved the puzzle! Well done!')
        sys.exit()

def displayTowers(towers):
    for level in range(TOTAL_DISKS, -1, -1):
        for tower in (towers['A'], towers['B'], towers['C']):
            if level >= len(tower):
                displayDisk(0)
            else:
                displayDisk(tower[level])
        print()

    emptySpace = ' ' * (TOTAL_DISKS)
    print('{0} A{0}{0} B{0}{0} C\n'.format(emptySpace))

def displayDisk(width):
    emptySpace = ' ' * (TOTAL_DISKS - width)

    if width == 0:
        print(emptySpace + '||' + emptySpace, end='')
    else:
        disk = '@' * width
        numLabel = str(width).rjust(2, '_')
        print(emptySpace + disk + numLabel + disk + emptySpace, end='')

if __name__ == '__main__':
    main()
