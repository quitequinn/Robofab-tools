# Add Radial Guides - Quinn Keaveney
# qkeave@gmail.com
# quinnkeaveney.com

from mojo.events import BaseEventTool, installTool
from AppKit import *
import os

from lib.tools.drawing import strokePixelPath

from dialogKit import ModalDialog, TextBox, EditText, PopUpButton
from vanilla import RadioGroup

## collecting the image data for building cursors and toolbar icons
dirname = os.path.dirname(__file__)

toolbarIcon = NSImage.alloc().initByReferencingFile_(os.path.join(dirname, "toolbarIcon.png"))

class DrawGeometricShapesTool(BaseEventTool):

        ## setup is called when the tool gets active
        ## use this to initialize some attributes
        ancs = []
        gd = []

        g = CurrentGlyph()

        for angle in range(0, 180, 15):
            gd.append("Radial {0}deg".format(angle))

        for a in g.anchors:
            b = a.name
            ancs.append(b)
            
        if 'Radial Guide' not in ancs:
            g.appendAnchor("Radial Guide", (500, 500))

        for a in g.guides:
            if a.name in gd:
                g.removeGuide(a)

        for a in g.anchors:
            if a.name == 'Radial Guide':
                x = a.x
                y = a.y
                for angle in range(0, 180, 15):
                    g.addGuide((x, y), angle, name=("Radial {0}deg".format(angle)))
                    guide = g.addGuide((x, y), angle, name=("Radial {0}deg".format(angle)))
                    guide.naked().showMeasurements = True

        CurrentFont().update() 


    def getToolbarIcon(self):
        ## return the toolbar icon
        return toolbarIcon

    def getToolbarTip(self):
        ## return the toolbar tool tip
        return "Radial Guides Tool"

## install the tool!!
installTool(RadialGuideTool())

