import random, sys, time

PAUSE = 0.15

ROWS = [
    '         ##',
    '        #{}-{}#',
    '       #{}---{}#',
    '      #{}-----{}#',
    '     #{}------{}#',
    '    #{}------{}#',
    '    #{}-----{}#',
    '     #{}---{}#',
    '     #{}-{}#',
    '      ##',
    '     #{}-{}#',
    '     #{}---{}#',
    '    #{}-----{}#',
    '    #{}------{}#',
    '     #{}------{}#',
    '      #{}-----{}#', 
    '       #{}---{}#',
    '        #{}-{}#'
]

try:
    
    print('Press Ctrl-C to quit...')
    time.sleep(2)
    rowIndex = 0

    while True:
        rowIndex = (rowIndex + 1) % len(ROWS)
        print(ROWS[rowIndex]) if rowIndex in (0, 9) else print(ROWS[rowIndex].format(*random.choice([('A', 'T'), ('T', 'A'), ('C', 'G'), ('G', 'C')])))
        time.sleep(PAUSE)
except KeyboardInterrupt:
    sys.exit()
