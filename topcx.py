#!/usr/bin/env python

__author__ = 'Diego Manenti Martins'

import Image

def topcx(file_name, mode='1', threshold=127):
    img = Image.open(file_name)
    
    # Threshold function
    thrhldf = lambda x: 255 if x > threshold else 0

    out = img.point(thrhldf).convert(mode)

    return out

def main():
    import sys

    if len(sys.argv) != 3:
        print 'Usage: %s file_input file_output' % sys.argv[0]
        return

    file_input = sys.argv[1]
    file_output = sys.argv[2]

    img = topcx(file_input, threshold=150)
    img.save(file_output)

if __name__ == '__main__':
    main()

