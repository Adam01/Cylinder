import sys
import os

#import clean_js

script_list = list()

main_script = os.path.abspath( os.path.join("rapyd", "Cylinder.pyj") )

for root, dirs, files in os.walk("rapyd"):
    path = root.split(os.sep)
    path.pop(0)
    outdir = os.path.join("js", *path)

    if not os.path.exists(outdir):
        os.mkdir(outdir)

    for file in files:
        cmd = ""
        if file.lower().endswith(".pyj"):
            infile = os.path.abspath( os.path.join(root, file) )
            outfile = os.path.abspath( os.path.join(outdir, file[:-4]+".js") )

            if not os.path.exists(outfile) or os.path.getmtime(outfile) < os.path.getmtime(infile):
                cmd = 'rapydscript -p --screw-ie8 "%s" -o "%s"' % (infile, outfile)
        elif file.lower().endswith(".scss"):
            infile = os.path.abspath( os.path.join(root, file) )
            outfile = os.path.abspath( os.path.join(outdir, file[:-5]+".css") )
            if not os.path.exists(outfile) or  os.path.getmtime(outfile) < os.path.getmtime(infile):
                cmd = 'node-sass "%s" "%s"' % (infile, outfile)
        else:
            infile = os.path.abspath( os.path.join(root, file) )
            outfile = os.path.abspath( os.path.join(outdir, file) )
            if not os.path.exists(outfile) or os.path.getmtime(outfile) < os.path.getmtime(infile):
                    if sys.platform.startswith("win"):
                        cmd = 'copy /Y "%s" "%s"' % (infile, outfile)
                    elif sys.platform == "linux":
                        #TODO
                        pass

        if len(cmd) > 0:
            print cmd
            ret = os.system(cmd)
            if ret != 0:
                exit()

#script_list.append(main_script)
#cmd = 'rapydscript -p --screw-ie8 "%s" -o ./js/Cylinder.js' % ('" "'.join(script_list))
#print cmd
#os.system(cmd)