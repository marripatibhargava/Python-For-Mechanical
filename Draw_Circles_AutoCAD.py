# importing pyautocad
import pyautocad
# creating AutoCAD instance
acad = pyautocad.Autocad()
print(acad.doc.Name)

# specify x and y coordinates of circle center point
from pyautocad import APoint
point1 = APoint(100.0,100.0) # x and y coordinates of points
# add circle to drawing
circle1 = acad.model.AddCircle(point1,100)

# check layer assignment
print("current layer: "  + str(circle1.Layer))
# check current linetype
print("current linetype: " + str(circle1.Linetype))
# check linetype scale
print("current linetype scale: " + str(circle1.LinetypeScale))
# check current line weight
print("current line weight: " + str(circle1.Lineweight))
# check current thickness
print("current thickness: " + str(circle1.Thickness))
# check current material
print("current material:" + str(circle1.Material))


# adding two circles to drawing
circle2 = acad.model.AddCircle(APoint(200.0,200.0),100)
circle3 = acad.model.AddCircle(APoint(300.0,300.0),100)

