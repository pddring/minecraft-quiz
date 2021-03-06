"""
This file contains a dictionary containing all the capital letters as 2d bitmap images
so that they can be converted into minecraft blocks
"""
letters = {
'A':"""
.    1    .
.   1 1   .
.  1   1  .
. 1     1 .
. 1111111 .
. 1     1 .
. 1     1 .
.         .
""",
'B':"""
. 11111   .
. 1    1  .
. 1     1 .
. 111111  .
. 1     1 .
. 1    1  .
. 11111   .
.         .
""",
'C':"""
.   11111 .
.  1      .
. 1       .
. 1       .
. 1       .
.  1      .
.   11111 .
.         .
""",
'D':"""
. 11111   .
. 1    1  .
. 1     1 .
. 1     1 .
. 1    1  .
. 1   1   .
. 1111    .
.         .
""",
'E':"""
. 1111111 .
. 1       .
. 1       .
. 111111  .
. 1       .
. 1       .
. 1111111 .
.         .
""",
'F':"""
. 1111111 .
. 1       .
. 1       .
. 111111  .
. 1       .
. 1       .
. 1       .
.         .
""",
'G':"""
.  111111 .
. 1       .
. 1       .
. 1  1111 .
. 1    1  .
. 1     1 .
.  11111  .
.         .
""",
'H':"""
. 1     1 .
. 1     1 .
. 1     1 .
. 1111111 .
. 1     1 .
. 1     1 .
. 1     1 .
.         .
""",
'I':"""
.  11111  .
.    1    .
.    1    .
.    1    .
.    1    .
.    1    .
.  11111  .
.         .
""",
'J':"""
. 111111  .
.     1   .
.     1   .
.     1   .
.     1   .
.     1   .
.  111    .
.         .
""",
'K':"""
. 1    1  .
. 1   1   .
. 1  1    .
. 111     .
. 1  1    .
. 1   1   .
. 1    1  .
.         .
""",
'L':"""
. 1       .
. 1       .
. 1       .
. 1       .
. 1       .
. 1       .
. 1111111 .
.         .
""",
'M':"""
.  1   1  .
. 1 1 1 1 .
. 1  1  1 .
. 1     1 .
. 1     1 .
. 1     1 .
. 1     1 .
.         .
""",
'N':"""
. 1     1 .
. 11    1 .
. 1 1   1 .
. 1  1  1 .
. 1   1 1 .
. 1    11 .
. 1     1 .
.         .
""",
'O':"""
.  11111  .
. 1     1 .
. 1     1 .
. 1     1 .
. 1     1 .
. 1     1 .
.  11111  .
.         .
""",
'P':"""
. 111111  .
. 1    11 .
. 1    11 .
. 111111  .
. 1       .
. 1       .
. 1       .
.         .
""",
'Q':"""
.  1111   .
. 1    1  .
. 1     1 .
. 1     1 .
. 1   1 1 .
. 1    1  .
.  1111 1 .
.         .
""",
'R':"""
. 11111   .
. 1    1  .
. 1    1  .
. 11111   .
. 1  1    .
. 1   1   .
. 1    1  .
.         .
""",
'S':"""
.  111111 .
. 1       .
. 1       .
.  11111  .
.       1 .
.       1 .
. 111111  .
.         .
""",
'T':"""
. 1111111 .
.    1    .
.    1    .
.    1    .
.    1    .
.    1    .
.    1    .
.         .
""",
'U':"""
. 1     1 .
. 1     1 .
. 1     1 .
. 1     1 .
. 1     1 .
. 1     1 .
.  11111  .
.         .
""",
'V':"""
. 1     1 .
. 1     1 .
.  1   1  .
.  1   1  .
.   1 1   .
.   1 1   .
.    1    .
.         .
""",
'W':"""
. 1     1 .
. 1     1 .
. 1     1 .
. 1     1 .
. 1     1 .
.  1 1 1  .
.   1 1   .
.         .
""",
'X':"""
. 1     1 .
.  1   1  .
.   1 1   .
.    1    .
.   1 1   .
.  1   1  .
. 1     1 .
.         .
""",
'Y':"""
. 1     1 .
.  1   1  .
.   1 1   .
.    1    .
.    1    .
.    1    .
.    1    .
.         .
""",
'z':"""
. 1111111 .
.      1  .
.     1   .
.    1    .
.   1     .
.  1      .
. 1111111 .
.         .
""",
'0':"""
.  11111  .
. 1    11 .
. 1   1 1 .
. 1  1  1 .
. 1 1   1 .
. 11    1 .
.  11111  .
.         .
""",
'1':"""
.     1   .
.   111   .
.     1   .
.     1   .
.     1   .
.     1   .
.  111111 .
.         .
""",
'2':"""
.  1111   .
. 1    1  .
.      1  .
.     1   .
.    1    .
.   1     .
. 1111111 .
.         .
""",
'3':"""
. 111111  .
.       1 .
.       1 .
.  11111  .
.       1 .
.       1 .
. 111111  .
.         .
""",
'4':"""
.      1  .
.     11  .
.    1 1  .
.   1  1  .
.  1   1  .
. 1111111 .
.      1  .
.         .
""",
'5':"""
. 1111111 .
. 1       .
. 11111   .
.      1  .
.       1 .
.      1  .
. 11111   .
.         .
""",
'6':"""
.    1111 .
.  11     .
. 1       .
. 111111  .
. 1     1 .
. 1     1 .
.  11111  .
.         .
""",
'7':"""
. 1111111 .
.      1  .
.     1   .
.    1    .
.   1     .
.  1      .
. 1       .
.         .
""",
'8':"""
.  11111  .
. 1     1 .
. 1     1 .
.  11111  .
. 1     1 .
. 1     1 .
.  11111  .
.         .
""",
'9':"""
.  11111  .
. 1     1 .
. 1     1 .
.  111111 .
.      1  .
.     1   .
.   11    .
.         .
""",
' ':"""
.         .
.         .
.         .
.         .
.         .
.         .
.         .
.         .
"""
}
