import os

os.system('rapydscript -p --screw-ie8 rapyd/NamedCallbacks.pyj tests/test_NamedCallbacks.pyj -o tests/js/test_NamedCallbacks.js' )
os.system('node tests/js/test_Namedcallbacks.js')
"""

script_list = list()

for root, dirs, files in os.walk("rapyd"):
    path = root.split(os.sep)
    path.pop(0)

    for file in files:
        if file.lower().endswith(".pyj"):
            infile = os.path.abspath( os.path.join(root, file) )
            script_list.append(infile)

for file in os.listdir("tests"):
    path = os.path.join("tests/", file)
    if os.path.isfile(path):
        print file
        script_list.append( path )

cmd = 'rapydscript -p --screw-ie8 "%s" -o tests/js/Cylinder_test.js' % ('" "'.join(script_list))
print cmd
os.system(cmd)

"""