# IGCSE CS PseudoCode Transpiler 
This program translates the Pseudocode syntax studied in the IGCSE Computer Science 0478/0984 Syllabus.

## Note
This program is still under development and won't be fully functional for a while. For any suggestions or bug reports, please send me a message on Github. If you liked it, please don't forget to star this repository. Thanks!


## Prerequisites
[Python](https://www.python.org/downloads/)


## How to use
### Syntax
For starters, it is required to leave a space character between each variable, function or operator. 
For example, when assigning a value to a variable, this is the correct way to do this
  ```
  variableexample = 16 * 14 + Varexample2
  ```
While this, on the other hand, will not work
  ```
  variableexample=16*14+Varexample2
  ```

### Available Functions

### FOR Loop (Fully functional)
This is to repeat a number of statements, which are inserted between the FOR "LCV" = "Start" TO "End" and the NEXT "LCV", for a set number of times.
  ```
  FOR I = 1 TO 5
  PRINT "HELLO WORLD !"
  NEXT I
  ```

### PRINT (Fully functional)
This is a simple statement use as in the following examples
  ```
  PRINT "HELLO WORLD !"
  ```
To print a string, which is to be inserted between two quotation marks "". 
##### Note that you should ***never*** insert another quotation mark insider the 2 quotation marks. You should also never use a backslash character "\\".
It is also possible to print/output the contents of a variable
  ```
  PRINT Variableexample
  ```

### INPUT (Fully functional)
This is a simple statement that can be used as in the following example
  ```
  INPUT Variableexample
  ```
### WHILE Loop (Under development)
A conditional loop that is repeated as long as a condition is being met. Any statements should be insterted between the WHILE "Condition" and the ENDWHILE STATEMENT
  ```
  WHILE I < 5
  PRINT "HELLO WORLD !"
  I = I + 1
  ENDWHILE
  ```
##### Note that this does not currently support nested WHILE Loops.

### REPEAT Loop (Under development)
A conditional loop that is repeated until a certin condition is met. Any statements should be insterted between the REPEAT and the UNTIL statement.
  ```
  REPEAT
  PRINT "HELLO WORLD !"
  I = I + 1
  UNTIL I = 5
  ```

### IF (Fully functional)
A conditional statement that carries out a group of statements between the IF statement and the ENDIF statement. The ELSE statement will also be functional.
  ```
  IF I = T THEN 
  PRINT "HELLO WORLD !"
  I = I + 1
  ENDIF
  ```

### Commenting
Comments should be preceded by two slashes and a space character as follows.
  ```
  // This is a comment
  ```


## Contributing
Please read [CONTRIBUTING.md](https://github.com/Sherlemious/IGCSE-CS-PC-Transpiler/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.
