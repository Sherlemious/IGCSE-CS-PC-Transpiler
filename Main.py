import Classes
import os
import Commands as Do
import Config
import Functions as Fun


# Taking in the Pseudocode (currently through a text file)
dirname = os.path.dirname(__file__)
dirname += "\\To be translated"
File = open(dirname, "r")
Config.FileList = list(File)
File.close()

Fun.rem_end(Config.FileList)

Fun.object_gen()
Config.Iteratables[0] = Classes.FUNCTION(Config.FileList)

# Iterates through the list of the lines
while Config.Iteratables[0].line_number < len(Config.Iteratables[0].line_list):
    cur_line = Config.Iteratables[0].line_list[Config.Iteratables[0].line_number]
    Do.main(cur_line)
    Config.Iteratables[0].line_number += 1
