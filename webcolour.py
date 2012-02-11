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


"""Tools for analysing colour & contrast in web pages.

   The WCAG 2.0 Luminosity Contrast Ratio algorithm is used; for
   further details, see Guideline 1.4.3 and the glossary definitions
   of contrast ratio & relative luminance in the WCAG 2.0 document,
   http://www.w3.org/TR/2008/REC-WCAG-20081211/
"""


__author__  = 'Nick Efford'
__version__ = '0.2'


import re


# Regex for hex web colours

COLOUR_PATTERN = re.compile('([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})')

# WCAG 2.0 thresholds
# (www.w3.org/TR/UNDERSTANDING-WCAG20/visual-audio-contrast-contrast.html)

WCAG_THRESHOLDS = {
    False : { 'AA' : 4.5, 'AAA' : 7.0 },   # regular text
    True  : { 'AA' : 3.0, 'AAA' : 4.5 }    # large text
}


def parse_colour(colour):
    """Parses a string representing a colour in web hexadecimal format,
       returning the decimal R, G & B values as a tuple.
    """
    # Eliminate leading '#' if present

    if colour.startswith('#'):
        colour = colour[1:]

    # Convert a 3-digit representation into canonical 6-digit form

    if len(colour) == 3:
        colour = colour[0]*2 + colour[1]*2 + colour[2]*2

    # Check that colour is valid

    match = COLOUR_PATTERN.match(colour.lower())
    if not match:
        raise ValueError('invalid hex colour')

    # Extract decimal R, G & B components

    r = int('0x'+match.group(1), 16)
    g = int('0x'+match.group(2), 16)
    b = int('0x'+match.group(3), 16)

    return r, g, b


def _norm(component):
    """Normalises an 8-bit R, G or B colour component to a 0.0-1.0 range
       so that it can be used in luminance calculations.
    """
    c = float(component) / 255   # for Python 2.x compatibility 
    if c <= 0.03928:
        return c / 12.92
    else:
        return ((c + 0.055)/1.055)**2.4


def luminance(colour):
    """Returns the relative luminance associated with the given
       8-bit RGB colour.
    """
    r, g, b = colour

    return 0.2126*_norm(r) + 0.7152*_norm(g) + 0.0722*_norm(b)


def contrast(colour1, colour2):
    """Returns the colour contrast ratio associated with the given
       RGB colour tuples, assuming one of them to be the foreground
       colour and the other the background colour.
    """
    lum1 = luminance(colour1)
    lum2 = luminance(colour2)

    if lum1 > lum2:
        return (lum1 + 0.05) / (lum2 + 0.05)
    else:
        return (lum2 + 0.05) / (lum1 + 0.05)


def conforms(contrast, level='AA', large=False):
    """Returns True if the given contrast conforms to the given WCAG
       level ('AA' by default), False otherwise.  Normal text is
       assumed; the test can be done for large text by calling the
       function with 'large=True' as an argument.
    """
    return contrast >= WCAG_THRESHOLDS[large][level]


def wcag_level(contrast, large=False):
    """Returns a string identifying the level of WCAG conformance
       ('AA' or 'AAA') for the given colour contrast.  If the contrast
       does not satisfy WCAG guidelines, an empty string is returned.
       Normal text is assumed by default; large text can be specified
       by supplying 'large=True' as an argument.
    """
    if contrast >= WCAG_THRESHOLDS[large]['AAA']:
        return 'AAA'
    elif contrast >= WCAG_THRESHOLDS[large]['AA']:
        return 'AA'
    else:
        return ''
