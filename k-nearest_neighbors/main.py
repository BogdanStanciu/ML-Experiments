# from __future__ import absolute_import
from NearestNeighbor import NearestNeighbor
import numpy as np

colors = dict(); 
colors['lower-left'] = 'bo';
colors['upper-left'] = 'ro';
colors['lower-right'] = 'go';
colors['upper-right'] = 'yo';

train = np.array([[0, 1], [0, 0], [-1, -1], [-2, 0], 
				[1, 10], [-1, 10], [-2, 12], [0, 11],
				[10, 1], [13, 0], [20, -1], [14, 2],
				[10, 10], [13, 12], [20, 11], [14, 14]])

label = np.array(['lower-left', 'lower-left', 'lower-left', 'lower-left', 
				'upper-left', 'upper-left', 'upper-left', 'upper-left', 
				'lower-right', 'lower-right', 'lower-right', 'lower-right', 
				'upper-right', 'upper-right', 'upper-right', 'upper-right'])

predict = np.array([10, 5])

t = NearestNeighbor(colors)
t.train(train, label)
t.visualizeTrain()

print(t.predict(predict))