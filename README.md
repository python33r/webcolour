webcolour
=========

Some tools for checking the accessibility of web colours.

The ```webcolour``` module provides functions to parse web colours
expressed in a hexadecimal format, compute the contrast ratio between
two colours and determine the level of WCAG 2.0 conformance.
The WCAG 2.0 Luminosity Contrast Ratio algorithm is used; for more
details, see Guideline 1.4.3 and the glossary definitions of contrast
ratio & relative luminance in the WCAG 2.0 document,
http://www.w3.org/TR/2008/REC-WCAG-20081211/.

The program ```contrastchecker.py``` provides a simple way of checking
the contrast between two web colours specified on the command line.
