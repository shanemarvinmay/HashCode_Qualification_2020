def read_file(file_name):
    D_remaining = 0
    B_to_pts = list()
    libraries = list()


    f = open(file_name, 'r')#open file
    lines = f.read() #read from file
    lines = lines.split('\n')#split by /n
    lines.pop(-1)

    for x in range(len(lines)):
        if x is 0: #get D_remaining
    
            D_remaining
     = lines[x][-1]
            continue
        elif x is 1: #get B_to_pts
    
            for number in lines[x]:
                if number is not ' ':
                    B_to_pts
            .append(int(number))
            continue

        #current & next line be sent to create_libraries
        if (x % 2 is 0):
            info = list()
            info.append(lines[x])
            info.append(lines[x+1])

            libraries.append(create_libraries(libraries, info))
    
    print((libraries))


def create_libraries(libraries, lines):
    library_info = dict()
    books = list()
    D_remaining = 0

    lines[0] = lines[0].replace(" ", "")
    lines[1] = lines[1].replace(" ", "")

    library_info['signup'] = int(lines[0][1])#'signup' --> 2nd pos
    library_info['B/D'] = int(lines[0][2])#'B/D' --> 3rd pos
    
    for book in lines[1]:
        books.append(int(book))#add to 'books'
    library_info['books'] = books

    D_remaining = library_info.get('signup') + (len(library_info.get('books'))/ library_info.get('B/D'))
    library_info['D_remaining'] = D_remaining

    return library_info

#def get_points_per_day(library, B_to_pts
): (passing in one specific library & B_to_pts
)
    
    #get points
    #loop through library[books]
        #points += B_to_pts
        [index]
    #return points / library[D_remaining
    ]


read_file('a-example.txt')