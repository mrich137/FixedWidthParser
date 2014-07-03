FixedWidthParser
================

Python Fixed Width Parser

This project is used to take an input file, define the field names, position and
length, and output the results to an ASCII formated table with the same file
name as the original file, but with a '.rpt' extension.

Current Issues
================
* Not flexible, field values are hard-coded into the reader/writer
* Can only read files hard-coded into reader/writer

TODO
================
* Fix Current issues
* Create API so any input format can be supported