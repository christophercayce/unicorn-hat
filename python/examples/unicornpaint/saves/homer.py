#!/usr/bin/env python
import unicornhat, signal
pixels = [[(0, 0, 0), (0, 0, 0), (132, 132, 132), (0, 0, 0), (132, 132, 132), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (132, 132, 132), (255, 255, 0), (132, 132, 132), (255, 255, 0), (132, 132, 132), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (132, 132, 132), (255, 255, 0), (255, 255, 0), (0, 0, 0)], [(132, 132, 132), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (132, 132, 132)], [(132, 132, 132), (255, 255, 255), (255, 255, 255), (255, 255, 0), (255, 255, 255), (255, 255, 255), (255, 255, 0), (132, 132, 132)], [(0, 0, 0), (255, 255, 255), (255, 255, 255), (255, 255, 0), (255, 255, 255), (255, 255, 255), (255, 255, 0), (0, 0, 0)], [(0, 0, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (0, 0, 0)], [(0, 0, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (0, 0, 0)]]
unicornhat.set_pixels(pixels)
unicornhat.show()
signal.pause()