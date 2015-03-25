import os
import sys
import shutil

templateDir = "./Cylinder/WidgetTemplate"
widgetOutDir = "./Cylinder/rapyd/Widgets/"


if len(sys.argv) > 1:
    name = sys.argv[1]
    widgetDir = os.path.join(widgetOutDir, name)
    if not os.path.exists(widgetDir):
        if os.path.exists(templateDir):
            os.mkdir(widgetDir)
            for item in os.listdir(templateDir):
                widgetTemplateItem = os.path.join(templateDir, item)
                widgetItem = os.path.join(widgetDir, name + os.path.splitext(item)[1] )
                print "Copying %s as %s" % (widgetTemplateItem, widgetItem)
                shutil.copy(widgetTemplateItem, widgetItem)
            print "Done"
        else:
            print "Unable to find template dir"
    else:
        print "Widget already exists"
else:
    print "Specify widget name"