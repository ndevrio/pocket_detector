import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import socket
import threading
import struct
import os
import time


# examine N second windows of data (5?)
# do preprocessing to extract features for that window
# pass through RandomForestClassifier() model
# start with just, left/right front/back pockets, all same orientation


if __name__ == '__main__':
