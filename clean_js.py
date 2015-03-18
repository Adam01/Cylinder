import shutil
import os

for entity in os.listdir("js"):
    path = os.path.abspath( os.path.join("js", entity) )
    if os.path.isdir(path):
        shutil.rmtree( path )
    elif os.path.isfile(path):
        os.remove(path)

print "Cleaned JS output directory"