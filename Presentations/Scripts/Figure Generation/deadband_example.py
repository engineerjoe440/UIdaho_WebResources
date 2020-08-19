import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

nValues = 100
offset = 50
deadband = 15
lastval = 0

def rand(n):
    return np.random.rand(n)

def eval_db(values):
    db = np.array([])
    last = 0
    for value in values:
        if (last-deadband) < value < (last+deadband):
            db = np.append(db, last)
        else:
            db = np.append(db, value)
            last = value
    return db

x = np.linspace(0, offset, nValues)
y = 3*np.sin(2*x) + 10*np.sin(x/10) + offset + rand(nValues)*5**(2*rand(nValues))
db = eval_db(y)

fig, ax = plt.subplots()
line, = ax.plot(x, y, color='k')
dblin, = ax.plot(x, db, color='b', linestyle=':')
posdb, = ax.plot(x, db+deadband, color='r', linestyle='--')
negdb, = ax.plot(x, db-deadband, color='r', linestyle='--')

def update(num, x, y, db, line, dblin, posdb, negdb):
    line.set_data(x[:num], y[:num])
    line.axes.axis([0, offset, 0, offset*2])
    dblin.set_data(x[:num], db[:num])
    dblin.axes.axis([0, offset, 0, offset*2])
    posdb.set_data(x[:num], db[:num]+deadband)
    negdb.set_data(x[:num], db[:num]-deadband)
    posdb.axes.axis([0, offset, 0, offset*2])
    negdb.axes.axis([0, offset, 0, offset*2])
    return line, dblin, posdb, negdb,

ani = animation.FuncAnimation(fig, update, len(x),
                              fargs=[x, y, db, line, dblin, posdb, negdb],
                              interval=15, blit=True)
#ani.save('test.gif')
plt.show()
