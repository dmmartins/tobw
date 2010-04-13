#!/usr/bin/env python

'''
Convert an input image to a 1-bit monochromatic image.
Can be used as a command line script, eg:
    $ tobw.py -t 200 -i input_image.jpg -o output_image.bmp
The options to command line are:
-t  Threshold to apply to the input image (0 to 255)
-i  Input file name
-o  Output file name

Can also be used as a python library, calling tobw function.
'''

__author__ = 'Diego Manenti Martins'


import Image
import getopt
import sys

def tobw(file_name, threshold=127):
    ''' Return a 1-bit monochromatic image converted from 'file_name' input image.
    'threshold' is applied to the image to do the conversion. '''

    # Monochromatic
    mode = '1'

    img = Image.open(file_name)
    
    # Threshold function
    thrhldf = lambda x: 255 if x > threshold else 0

    out = img.point(thrhldf).convert(mode)
    return out

if __name__ == '__main__':
    def usage():
        print 'Usage: %s [-t threshold] -i file_input -o file_output' % sys.argv[0]
        print '''Options:
        -t\tThreshold to apply to the input image (0 to 255)
        -i\tInput file name
        -o\tOutput file name'''

    try:
        opts, args = getopt.getopt(sys.argv[1:], 't:i:o:')
        options = dict(opts)

        input_file = options['-i']
        output_file = options['-o']

        if options.has_key('-t'):
            threshold = int(options['-t'])
        else:
            threshold = 128
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    except KeyError:
        usage()
        sys.exit(2)

    img = tobw(input_file, threshold=threshold)
    img.save(output_file)

