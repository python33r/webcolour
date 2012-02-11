#!/usr/bin/env python3
#
# Copyright (c) 2012 Nick Efford <nick.efford (at) gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


import argparse
import sys
from webcolour import parse_colour, contrast, wcag_level


def parse_command_line():

    parser = argparse.ArgumentParser(
      description='Checks contrast & WCAG conformance of two web colours.'
    )

    parser.add_argument(
      '-l', '--large',
      dest='large',
      action='store_true',
      help='assume large text'
    )
    parser.add_argument(
      'colour1',
      help='first web colour (hex format)'
    )
    parser.add_argument(
      'colour2',
      help='second web colour (hex format)'
    )

    return parser.parse_args()


try:
    args = parse_command_line()
    colour1 = parse_colour(args.colour1)
    colour2 = parse_colour(args.colour2)

    ratio = contrast(colour1, colour2)
    print('Contrast ratio = {:.3f}'.format(ratio))

    level = wcag_level(ratio, large=args.large)
    if level:
        print('Conformance level is', level)

except ValueError as error:
    sys.exit('Error: {}'.format(error))
