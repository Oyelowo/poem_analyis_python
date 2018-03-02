The name of the module is "poempy".
The module can be found under the folder/package "text_analysis"

There is  "task_poem_analysis.py" which includes the solution to the tasks and also how to use other funtions in the module.

You can use the below to automatically set your working directory to the path of the module, if the module is in "text_analysis" folder.
 import os
 **_DIR_PATH = os.path.dirname(os.path.realpath('__file__'))
 for dirpath, dirnames, filenames in os.walk(DIR_PATH):
     for dirname in dirnames:
         if dirname == "text_analysis":
             os.chdir(dirpath)_**
