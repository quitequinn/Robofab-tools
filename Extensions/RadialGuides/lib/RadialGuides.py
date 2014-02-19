import os
from vanilla import *
from mojo.UI import CurrentFontWindow, CurrentSpaceCenter
from mojo.events import addObserver
from AppKit import NSImage, NSImageNameAdvanced
from mojo.extensions import getExtensionDefault, setExtensionDefault
from lib.UI.integerEditText import NumberEditText
 
### link to font opening 
class AddToolbarItemObserver(object):
    
    base_path = os.path.dirname(__file__)
    
    def __init__(self):
        addObserver(self, "didOpen", "fontDidOpen")
        addObserver(self, "didOpen", "newFontDidOpen")
        
### add menu stuff
    def didOpen(self, notification):
 
        window = CurrentFontWindow()
        if window is None:
            return
        toolbarItems = window.getToolbarItems()
        toolbarIcon = NSImage.alloc().initByReferencingFile_(os.path.join(self.base_path, "icon.pdf"))
        newItem = dict(
            itemIdentifier='radialguides',
            label='Radial Guides',
            imageObject=toolbarIcon,
            view=toolbarIcon,
            callback=self.openSheet
            )
        index=-2
        toolbarItems.insert(index, newItem)
        vanillaWindow = window.window()
        vanillaWindow.addToolbar(
             toolbarIdentifier='radialguides',
             toolbarItems=toolbarItems, 
             addStandardItems=False
             )
 
    def openSheet(self, sender):
        window = CurrentFontWindow().window()
        if window is None:
            return
        Guides(window) 
 
### build the slide out menu
class Guides(object):
 
    def __init__(self, parentWindow):
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
 
AddToolbarItemObserver()