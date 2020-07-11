# IGCSE CS PseudoCode Transpiler 
This program translates the Pseudocode syntax studied in the IGCSE Computer Science 0478 Syllabus as no other application is available to do this.

## Note
This program is still under development and won't be fully functional for a while. For any suggestions or bug reports, please send me a message on Github. If you liked it, please don't forget to star this repository. Thanks!
In order to use this repository, Python should be installed first.

## Syntax
For starters, it is required to leave a space character between each variable, function or operator. 
For example, when assigning a value to a variable, this is the correct way to be used
  ```
  variableexample = 16 * 14 + Varexample2
  ```
While this, on the other hand, will not work,
  ```
  variableexample=16*14+Varexample2
  ```

## Available Functions

### FOR Loop
This is to repeat a number of statements, which are inserted between the FOR "LCV" = "Start" TO "End" and the ENDFOR/ NEXT "LCV", for a set number of times.
For example,
  ```
  FOR I = 1 TO 5
  PRINT "HELLO WORLD !"
  ENDFOR
  ```
or 
  ```
  FOR I = 1 TO 5
  PRINT "HELLO WORLD !"
  NEXT I
  ```
###### Note that If you use the ENDFOR version, you should ***never*** use nested loops.

### PRINT 
This is a simple statement use as in the following examples
  ```
  PRINT "HELLO WORLD !"
  ```
To print a string, which is to be inserted between two quotation marks "". 
###### Note that you should ***never*** insert another quotation mark insider the 2 quotation marks. You should also never use a backslash character "\".
It is also possible to print a variable
  ```
  PRINT Variableexample
  ```
