ignore_B = set()
ignore_L = set()
D_remaining = 7
B_to_pts = [1,2,3,6,5,4]

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
    
    return((libraries))

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

    totD = library_info.get('signup') + (len(library_info.get('books'))/ library_info.get('B/D'))
    library_info['totD'] = totD

    # return library_info

    
    #get points
    #loop through library[books]
        #points += B_to_pts[index]
    #return points / library[D_remaining]

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

def order_ls(ignore_B, ignore_L, D_remaining, Ls, B_to_pts):
    output = []
    # ordering the ls by the most pts/D 
    while len(ignore_L) < Ls:
        # finding L with most pts/D 
        idx = -1
        most = -1
        most_numB = -1
        for L in Ls:
            if L in ignore_L or L['signup'] >= D_remaining:
                continue
            pts, numB = calc_pts_D( Ls[L] )
            if pts > most:
                idx = L
                most = pts
                most_numB = numB
        D_remaining -= Ls[idx]['signup']
        # adding all B to ignore_B
        for i in range(most_numB):
            ignore_B.add(Ls[idx]['books'][i])
        ignore_L.add(idx)
        output.append(idx)
    return output

def calc_pts(L,D_remain,b_pts):
  numB = L['B/D']*min(D_remain-L['signup'],L['totalD']):
  sim = i = 0
  while i < numB and numB < len(L['books']):
    sum+=b_pts[L['books'[i]]]
    i+=1
  return sum,numB

libraries = read_file('a-example.txt')

write_to_file([1, 0], libraries)