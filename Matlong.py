import arcpy, sys, os, traceback

try:
    arcpy.overwriteOutput = True
    arcpy.env.workspace = r"Drive:\Example\Workspace"

    if arcpy.Exists("Example.gdb"):
        arcpy.Delete_management("Example.gdb")
    arcpy.CreateFileGDB_management(arcpy.env.workspace,"Example.gdb")

    if arcpy.Exists("Jobs"):
        arcpy.Delete_management("Jobs")
    arcpy.CreateFeatureDataset_management("Example.gdb","Jobs",4326)

    FC = arcpy.CreateFeatureclass_management("Example.gdb" + os.sep + "Jobs","February","POINT")
    print (FC)
    arcpy.AddField_management(r"Drive:\Some\Location\Example.gdb\Jobs\February","Job","TEXT",50)

    MatLong = open("MatLong.txt","r",newline="")
    rows = arcpy.da.InsertCursor(FC, ["SHAPE@XY","Job"])

    for line in MatLong:
        splitline = line.split("|")
        Lat = splitline[0]
        Long = splitline[1]
        Job = splitline[2]
        print(Lat)
        print(Long)
        print(Job)
        xy = (float(str(Long)),float(str(Lat)))
        print(xy)
        rows.insertRow([xy, Job])

except:
    print ("Sorry, something went wrong :(. Here's some more information: ")
    print (sys.exc_info()[1])
    raise

MatLong.close()
del rows
