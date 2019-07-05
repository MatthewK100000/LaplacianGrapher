# cd pythonpractice
# python3 laplaciansolver.py

import numpy as np
import math as m
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D

np.set_printoptions(suppress=True,precision=4)

def chunks(l, p):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), p):
        yield l[i:i + p]
        
def laplacianmatrix(x):
	M = np.zeros((x**2,x**2))
	M[0, 0] = 4
	M[0, 1] = -1
	M[0, x] = -1
	M[x - 1, x - 1] = 4
	M[x - 1, x - 2] = -1
	M[x - 1, 2*x - 1] = -1
	M[x**2 - x, x**2 - x] = 4
	M[x**2 - x, x**2 - 2*x] = -1
	M[x**2 - x, x**2 - x + 1] = -1
	M[x**2 - 1, x**2 - 1] = 4
	M[x**2 - 1, x**2 - 2] = -1
	M[x**2 - 1, x**2 - x -1]= -1
	for i in range(2,x):
		M[i - 1, i - 1] = 4
		M[i - 1, i - 2] = -1
		M[i - 1, i] = -1
		M[i - 1, i + x - 1] = -1
	for j in range(1, x - 1):
		M[j*x, j*x] = 4
		M[j*x, j*x + 1] = -1
		M[j*x, j*x + x] = -1
		M[j*x, j*x - x] = -1
	for k in range(2,x):
		M[k*x - 1, k*x - 1] = 4
		M[k*x - 1, k*x - 2] = -1
		M[k*x - 1, k*x - x - 1] = -1
		M[k*x - 1, k*x + x - 1] = -1
	for l in range(2,x):
		M[x**2 - x + l - 1, x**2 - x + l - 1] = 4
		M[x**2 - x + l - 1, x**2 - x + l] = -1
		M[x**2 - x + l - 1, x**2 - x + l - 2] = -1
		M[x**2 - x + l - 1, x**2 - 2*x + l - 1] = -1
	for m in range(2, x):
		for n in range(1, x - 1):
			M[n*x + m - 1, n*x + m - 1] = 4
			M[n*x + m - 1, n*x + m - 2] = -1
			M[n*x + m - 1, n*x + m] = -1
			M[n*x + m - 1, n*x + m + x - 1] = -1
			M[n*x + m - 1, n*x + m - x - 1] = -1
	return M


def laplaciansolver(lower,upper,left,right,n):
	delta = 1/(n-1)
	A = []
	
	A.append(float(left(1*delta)+lower(1*delta)))
	if n - 3 >= 2:
		for i in range(2,n - 2):
			A.append(float(lower(i*delta)))
	A.append(float(lower((n-2)*delta) + right(1*delta)))
	
	if n - 3 >= 2:
		for j in range(2,n - 2):
			A.append(float(left(j*delta)))
			for k in range(1,n - 3):
				A.append(0)
			A.append(float(right(j*delta)))
	
	A.append(float(left((n-2)*delta) + upper(1*delta)))
	if n - 3 >= 2:
		for l in range(2,n - 2):
			A.append(float(upper(l*delta)))
	A.append(float(right((n-2)*delta) + upper((n-2)*delta)))
	
	A = np.asarray(A)
	A = np.resize(A,(len(A),1))
	b = np.dot(np.linalg.inv(laplacianmatrix(n-2)),A)
	b = b.flatten()
	centermatrix = np.asarray(list(chunks(b,n-2))).T
	centermatrix = np.stack(centermatrix).T
	centermatrix = np.flip(centermatrix,axis=0)
	lower = np.vectorize(lower)
	upper = np.vectorize(upper)
	left = np.vectorize(left)
	right = np.vectorize(right)
	leftoutline = left(delta*np.resize([i for i in range(n-2,0,-1)],(n-2,1)))
	rightoutline = right(delta*np.resize([i for i in range(n-2,0,-1)],(n-2,1)))
	upperoutline = upper(delta*np.asarray([i for i in range(0,n)]))
	loweroutline = lower(delta*np.asarray([i for i in range(0,n)]))
	solution = np.hstack((leftoutline,centermatrix))
	solution = np.hstack((solution,rightoutline))
	solution = np.vstack((upperoutline,solution))
	solution = np.vstack((solution,loweroutline))
	return solution

# boundary function examples (use the same format w/ "lambda x:")	
Lower = lambda x: x**2 + (1-x)**2
Upper = lambda x: 1
Left = lambda x: 1
Right = lambda x: 1

grapher = True

print(laplaciansolver(Lower,Upper,Left,Right,6))

if grapher == True:
	nn = 50
	fig = plt.figure()
	ax = fig.gca(projection='3d')
	X = np.arange(0,1,1/(nn-1))
	Y = np.arange(0,1,1/(nn-1))
	X, Y = np.meshgrid(X,Y)
	surf = ax.plot_surface(X,Y,np.flip(laplaciansolver(Lower,Upper,Left,Right,nn),0), 
	cmap=cm.autumn,edgecolor='none',antialiased=False,rstride=1,cstride=1)
	fig.colorbar(surf, shrink=0.5, aspect=5)
	ax.set_xlabel('$x$',fontsize=15)
	ax.set_ylabel('$y$',fontsize=15)
	ax.set_zlabel('$z$',fontsize=15)
	plt.show()
