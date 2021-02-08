import Classes
import os
import Commands as Do
import Config
import Functions as Fun


# Taking in the code (currently through a text file)
dirname = os.path.dirname(__file__)
dirname += "\\To be translated"
File = open(dirname, "r")
Config.FileList = list(File)
File.close()

Fun.rem_end(Config.FileList)

Fun.object_gen()
Config.iteratables[0] = Classes.FUNCTION(Config.FileList)

while Config.iteratables[-1].line_number < len(Config.iteratables[-1].line_list):
    cur_line = Config.iteratables[-1].line_list[Config.iteratables[-1].line_number]
    Do.main(cur_line)
    Config.iteratables[-1].line_number += 1
