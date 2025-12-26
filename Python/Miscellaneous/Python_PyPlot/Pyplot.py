import matplotlib.pyplot as plt
x = [1,1,3,5,5,3,1]
y = [2,5,6,5,2,1,2]
ax = [1.15, 2.9]
ay = [4.9,5.8]
bx = [4.87,4.87]
by = [4.9,2.1]
cx = [1.2, 2.9]
cy = [2.05, 1.2]
fig = plt.figure()
ax1 = fig.add_subplot()
ax1.set_aspect('equal', adjustable='box')
plt.plot(x,y,'k', linewidth=3, marker='d')
plt.plot(ax,ay,'k', linewidth=3)
plt.plot(bx,by,'k', linewidth=3)
plt.plot(cx,cy,'k', linewidth=3)
plt.title("Benzene Ring")
plt.show()