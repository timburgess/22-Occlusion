#!/usr/bin/env python3

# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
# 
# For more information, please refer to <http://unlicense.org/>


import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


fig, ax = plt.subplots()

# we need to set axes to be equal to get a circle not an ellipse
# and plt was devised in a non-metric country
fig.set_size_inches(4,4)

# create 0 to 2 bounding box
ax.set_xlim((0, 2))
ax.set_ylim((0, 2))

# remove ticks & labels
ax.tick_params(axis=u'both',
               which=u'both',
               bottom='off',
               top='off',
               left='off',
               right='off',
               labelleft='off',
               labelbottom='off')


# add Area 1.0 (radius = 0.564) circle
circle1 = Circle((1.0, 1.0), 0.564, color='yellow', alpha=0.4)

# add Area 0.22 (radius = 0.2646) circle
circle2 = Circle((1.0, 1.0), 0.2646, color='black', alpha=0.6)

ax.set_xlabel('22% Occulsion', fontsize=10)

ax.add_artist(circle1)
ax.add_artist(circle2)

fig.savefig('kic8462852_occlude.png')
