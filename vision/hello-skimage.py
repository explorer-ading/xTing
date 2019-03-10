#!/usr/bin/python3
# -*- coding: utf-8 -*-


from skimage import data, io, filters

image = data.coins()
# .. or any other numpy array !

edges = filters.sobel(image)
io.imshow(edges)
io.show()

