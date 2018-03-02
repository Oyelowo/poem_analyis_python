@author: OYEDAYO OYELOWO
Email: oyelowo.oyedayo@helsinki.fi, oyedayooyelowo@gmail.com
Phone Number: +358469551643

The name of the module is "poempy".
There is a "task_poem_analysis.py" which include the solution to the tasks and also how to use other funtions in the module.

You can use the below to automatically set your working directory to the path of the module.
 import os
 DIR_PATH = os.path.dirname(os.path.realpath('__file__'))
 for dirpath, dirnames, filenames in os.walk(DIR_PATH):
     for dirname in dirnames:
         if dirname == "text_analysis":
             os.chdir(dirpath)

