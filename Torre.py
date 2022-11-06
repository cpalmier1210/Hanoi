import argparse
import logging
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

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
    
    logger.info('Hanoi Tower Solution')
    parser = argparse.ArgumentParser()
    parser.add_argument('cant_discos',
                        help='Quantity of disks of the Hanoi Tower',
                        type=int)
    args = parser.parse_args()

    print(Torre(args.cant_discos,"ori","des","aux"))
    