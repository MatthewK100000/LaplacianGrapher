# LaplacianGrapher

## TLDR
Graphs the solution curve to Laplace's equation (using numerical approximations and linear programming) given 4 boundary functions along the unit square. 

## The Math behind this stuff
(coming soon)

## Examples
For the sake of simplicity and github's lack of mathjax support, denote Lower() as the function on the set of points (x,0), where 0 <= x <= 1, Upper() as the function on the set of points (x,1) where 0 <= x <= 1, Left() as the function on the set of points (0,y) where 0 <= y <= 1, and Right() as the function on the set of points (1,y), where 0 <= y <= 1.

Ex 1.  Lower() = 0, Upper() = 1, Left() = 0, and Right() = 1

![](images/Figure_3.png)

Ex 2. Lower() = 0.5*sin(pi*x - pi/2)+0.5, Right() = 0.5*sin(pi*x - pi/2)+0.5, Left() = 0, Right() = 1

![](images/Figure_2.png)

Ex 3. Lower() = 0.5*sin(2*pi*x - pi/2)+0.5, Right() = 0.5*sin(2*pi*x - pi/2)+0.5, Left() = 0.5*sin(2*pi*x - pi/2)+0.5, Right() = 0.5*sin(2*pi*x - pi/2)+0.5

![](images/Figure_1.png)

Ex 4. Lower() = sin(pi*x), Upper() = x(1-x), Left() = 0, Right() = 0

![](images/Figure_4.png)

## Future Updates
I plan to make a javascript web application that is fully interactable in the future
