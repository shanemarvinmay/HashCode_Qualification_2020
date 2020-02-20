libraries = list()
ignore_B = set()
ignore_L = set()
D_remaining = 0
B_to_pts = list()
library_order = list()

def read_file(file_name, libraries, B_to_pts, D_remaining):
    f = open(file_name, 'r')#open file
    lines = f.read() #read from file
    lines = lines.split('\n')#split by /n
    lines.pop(-1)

    for x in range(len(lines)):
        if x is 0: #get D_remaining
    
            D_remaining = lines[x][-1]
            continue
        elif x is 1: #get B_to_pts
    
            for number in lines[x]:
                if number is not ' ':
                    B_to_pts.append(int(number))
            continue

        #current & next line be sent to create_libraries
        if (x % 2 is 0):
            info = list()
            info.append(lines[x])
            info.append(lines[x+1])

            libraries.append(create_libraries(libraries, info))
    
    return int(D_remaining)

def create_libraries(libraries, lines):
    library_info = dict()
    books = list()
    totD = 0

    lines[0] = lines[0].replace(" ", "")
    lines[1] = lines[1].replace(" ", "")

    library_info['signup'] = int(lines[0][1])#'signup' --> 2nd pos
    library_info['B/D'] = int(lines[0][2])#'B/D' --> 3rd pos
    
    for book in lines[1]:
        books.append(int(book))#add to 'books'
    library_info['books'] = books

    totD = int(library_info.get('signup')) + int(len(library_info.get('books'))/ library_info.get('B/D'))
    library_info['totD'] = totD

    return library_info

def order_libraries(ignore_B, ignore_L, D_remaining, libraries, B_to_pts):
    # ordering the libraries by the most pts/D 
    while len(ignore_L) < libraries:
        # finding L with most pts/D 
        idx = -1
        most = -1
        most_numB = -1
        for L in range(len(libraries)):
            if L in ignore_L or libraries[L]['signup'] >= D_remaining:
                continue
            pts, numB = calc_pts(libraries[L], D_remaining, B_to_pts)
            if pts > most:
                idx = L
                most = pts
                most_numB = numB
        D_remaining -= libraries[idx]['signup']
        # adding all B to ignore_B
        for i in range(most_numB):
            ignore_B.add(libraries[idx]['books'][i])
        ignore_L.add(idx)
        library_order.append(idx)
    return library_order

def calc_pts(L,D_remain,b_pts):
  numB = L['B/D'] * min(D_remain - L['signup'], L['totD'])
  s = i = 0
  while i < numB and numB < len(L['books']):
    s+=b_pts[L['books'[i]]]
    i+=1
  return s,numB
    # return 0

def write_to_file(library_order, libraries):
    output = ""

    output += str(len(library_order)) + "\n\n"

    for x in range(len(library_order)):
        output += str(library_order[0]) + " " + str(len(libraries[x]['books'])) + "\n\n"

        if x is 0:
            output += "\n"
        
        for book in libraries[x]['books']:
            output += str(book) + " "
        
        output += "\n\n"


    print(output)


D_remaining = read_file('a-example.txt', libraries, B_to_pts, D_remaining)


print(order_libraries(ignore_B, ignore_L, D_remaining, libraries, B_to_pts))
# order_libraries(ignore_B, ignore_L, D_remaining, libraries, B_to_pts)

# write_to_file(library_order, libraries)