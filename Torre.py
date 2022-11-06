

i = 0

def Torre(disco, ori,des, aux):
    global i
     
    if disco == 1:
        i +=1
        print(i,"-mover ", disco, "de ", ori, "a", des)
    else:
        Torre(disco - 1, ori, aux, des)
        i += 1
        print(i,"-mover ", disco, "de ", ori, "a", des)
        Torre(disco - 1, aux, des, ori)
    return

if __name__ == '__main__':
    
    
    print(Torre(5,"ori","des","aux"))
    