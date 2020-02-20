def read_file(file_name):
    f = open(file_name, 'r')

    f.close()
def calc_pts(L,D_remain,b_pts):
  numB = L['B/D']*min(D_remain-L['signup'],L['totalD']):
  sim = i = 0
  while i < numB and numB < len(L['books']):
    sum+=b_pts[L['books'[i]]]
    i+=1
  return sum,numB
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

