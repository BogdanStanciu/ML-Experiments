"""
	the purpose of this script is to implement the k-nearest neighbors algorithm
	with simple k = 1

	In pattern recognition k-nearest neighbors algorithm (k-NN) 
	is a non parametric method for classification and regression
	where the k consists in the closest traning example in the feature space 
	(k is a integer > 0 typically small)
"""
import numpy as np 
import matplotlib.pyplot as plt
import math


class NearestNeighbor: 

	def __init__(self, dict): 
		self.colors = dict; 

	# "Train" the algorithm: O(1)
	def train(self, X, y): 
		# remember all the training data without doing anything else 
		self.Xtr = X; 
		self.ytr = y; 

	# Predict new data: O(n)
	def predict(self, X):
		min = math.inf
		i = 0; 
		y_ = ''; 

		# loop over all training data 
		for point in self.Xtr: 
			tmp = abs(point[0]-X[0])+abs(point[1]-X[1])
			
			# find the nearest point 
			if tmp < min: 
				min = tmp
				y_ = self.ytr[i];

			i = i+1;

		# draw the new point in the space
		self.draw();

		plt.plot(X[0], X[1], self.colors[y_].replace('o', 'x'))
		plt.axhline(0, color='black')
		plt.axvline(0, color='black')
		
		plt.show();

		return y_;

	# Draw the training data
	def draw(self): 
		i = 0; 

		for point in self.Xtr: 
			plt.plot(point[0], point[1], self.colors[self.ytr[i]]);
			i = i+1; 

		plt.axhline(0, color='black')
		plt.axvline(0, color='black')

		
	def visualizeTrain(self):
		self.draw()
		plt.show()
