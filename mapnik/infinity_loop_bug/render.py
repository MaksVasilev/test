#!/usr/bin/python

import mapnik
import sys, os
import cairo

if __name__ == "__main__":
    try:
        mapfile = os.environ['MAPNIK_MAP_FILE']
    except KeyError:
        mapfile = "infinity_loop_bug.xml"
 
    ll = (49.6722793579102,58.489073506677,49.8791313171387,58.5597023238563)

    z = 13
    imgx = 900 
    imgy = 600

    m = mapnik.Map(imgx,imgy)
    mapnik.load_map(m,mapfile)
    prj = mapnik.Projection("+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m +nadgrids=@null +no_defs +over")
    c0 = prj.forward(mapnik.Coord(ll[0],ll[1]))
    c1 = prj.forward(mapnik.Coord(ll[2],ll[3]))

    bbox = mapnik.Box2d(c0.x,c0.y,c1.x,c1.y)

    m.zoom_to_box(bbox)

    surface = cairo.PDFSurface('out.pdf', m.width, m.height)
    mapnik.render(m, surface)
    surface.finish()


