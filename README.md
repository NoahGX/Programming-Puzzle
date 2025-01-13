# Programming Puzzle

## Overview
Returns a path of 'L'/'R' from top to bottom whose product equals 'target', or None if no valid path exists.
**param pyramid**: List of lists of integers (the pyramid)
**param target**:  The target product to find
**param row**:     Current row in the pyramid (for recursive calls)
**param idx**:     Current index in the row (for recursive calls)
**param product**: Current product of all numbers in the path so far
**param path**:    Path string built so far ('L' and 'R')
**return**:        A string of moves like 'LRLL' if found, else None