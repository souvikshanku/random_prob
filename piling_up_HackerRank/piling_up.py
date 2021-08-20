T = int(input())
block = []
for i in range(T):
    n = input()
    new = []
    inpt = list(input().split(" "))
    for j in inpt:
        new.append(int(j))
    block.append(new)


def check(block_):                                      # Checks if the cubes in a particular block is possible to stack up.
    done = False
    while done == False and len(block_)>0:              # If the block size is 1 or 2, it is always possible
        if len(block_) == 1 or len(block_) == 2:
            done = True
            break
        else:                                                   # If the block size is greater than 2, it chooses the maximum value from
            if block_[0] > block_[-1]:                          # the leftmost and rightmost cube from the array and uses (deletes from array)
                max_element = block_[0]                         # the cube whose side-length is larger.
                block_.pop(0)
            else:
                max_element = block_[-1]
                block_.pop(-1)
                if max(block_[0], block_[-1]) > max_element:    # If the previously deleted cube is of lower side-length than any of the end cube
                    done = False                                # the stacking fails
                    break

    return done

for t in range(T):
    if check(block[t]) == True:
        print("Yes")
    else:
        print("No")
