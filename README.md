# IGCSE CS PseudoCode Transpiler [![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

This program translates the Pseudocode syntax studied in the IGCSE Computer Science 0478/0984 Syllabus.


## Note
This program is usage-ready with just a couple additional features under development. For any suggestions or bug reports, please send me a message on GitHub. 
If you liked it, please don't forget to star this repository. Thanks!

## Prerequisites
[Python 3](https://www.python.org/downloads/)


## How to use

### Syntax
For starters, it is required to leave a space character between each variable, function or operator.
For example, when assigning a value to a variable, this is the correct way to do it.
  ```
  variable = 16 * 14 + variable2
  ```
While this, on the other hand, will not work.
  ```
  variable=16*14+variable2
  ```
##### Arrays (example):
  ```
  Numbers = [ 3, 4 ]
  Numbers[Count] = 123
  INPUT Numbers[3]
  ```


### Available Functions

#### PRINT (Fully functional):
This is a simple statement use as in the following examples
  ```
  PRINT "HELLO WORLD !"
  ```
The OUTPUT keyword also works
  ```
  OUTPUT "HELLO WORLD !"
  ```
To print the string between two quotation marks " ".
###### Note that you should ***never** put quotations within pre-existing quotations and/or use a backslash character "\\".
It is also possible to print/output the contents of a variable.
  ```
  PRINT Variable
  ```
The OUTPUT keyword also works
  ```
  OUTPUT Variable
  ```
To print multiple strings, or variable or both, separate them using commas.
sum = 99
  ```
  PRINT "The sum is equal to:" , sum
  ```
Output: The sum is equal to: 99

Note that spaces are automatically added between printed entites


#### INPUT (Fully functional):
This is a simple statement that can be used as in the following example.
  ```
  INPUT Variable
  ```
The keyword, "USERINPUT", can also be used.
  ```
  Variable = USERINPUT
  ```
#### IF (Fully functional):
A conditional statement that carries out a number of statements between the IF statement and the ENDIF statement. The ELSE statement will also be functional.
  ```
  IF I = T THEN
  PRINT "HELLO WORLD !"
  I = I + 1
  ELSE 
  "Print Hello"
  ENDIF
  ```
(The 'THEN' keyword is optional)


#### FOR Loop (Fully functional):
This is to repeat a number of statements, which are inserted between the FOR "LCV" = "Start" TO "End" and the NEXT "LCV", for a set number of times.
  ```
  FOR I = 1 TO 5
  PRINT "HELLO WORLD !"
  NEXT I
  ```


#### WHILE Loop (Fully functional):
A conditional loop that is repeated as long as a condition is true. Any statements should be inserted between the WHILE "Condition" and the ENDWHILE STATEMENT.
  ```
  WHILE I < 5 DO
  PRINT "HELLO WORLD !"
  I = I + 1
  ENDWHILE
  ```
(The 'DO' keyword is optional)


#### REPEAT Loop (Fully functional):
A conditional loop that is repeated until a certain condition is met. Any statements should be inserted between the REPEAT and the UNTIL statement.
  ```
  REPEAT
  PRINT "HELLO WORLD !"
  I = I + 1
  UNTIL I = 5
  ```


#### Commenting (Functional):
Comments should be preceded by two slashes and a space character as follows.
  ```
  // This is a comment
  ```


### Contributing
Please read [CONTRIBUTING.md](https://github.com/Sherlemious/IGCSE-CS-PC-Transpiler/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.
