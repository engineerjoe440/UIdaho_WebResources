"""
Analog Deadband Example Figure Generator
----------------------------------------

This simple script uses NumPy and MatPlotLib to create an animated
figure that illustrates how deadbands are applied to analog data to
reduce communication burden for systems using DNP3, SEL-Protocol,
or any other industrial/industry-standard communications to provide
analog data points.

"""

# Import Required Packages
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants Used to Define Plot Parameters
nValues = 150
offset = 100
maximum = 50
deadband = 20
lastval = 0
large_oscillation = -35
large_rate = 8
small_oscillation = 3
small_rate = 2

# Define Random Array Function
def random(n):
    a = np.random.rand(n)
    b = np.random.rand(n)
    return a*5**(b)

# Define Simple Function to Evaluate the Deadband
def eval_db(values):
    db = np.array([])
    last = 0
    # Iterate over Values to Evaluate Current Deadband
    for value in values:
        if (last-deadband) < value < (last+deadband):
            db = np.append(db, last)
        else:
            db = np.append(db, value)
            last = value
    return db

# Evaluate Plotted Points
x = np.linspace(0, maximum, nValues)
y = (
        small_oscillation*np.sin(small_rate*x) 
            + large_oscillation*np.sin(x/large_rate)
            + offset + random(nValues)
    )
db = eval_db(y)

# Create Figure and Axes
fig, ax = plt.subplots()
line, = ax.plot(x, y, color='k', label='Instantaneous Magnitude')
dblin, = ax.plot(x, db, color='g', linestyle=':', label='Deadbanded Magnitude')
posdb, = ax.plot(x, db+deadband, color='r', linestyle='--', label='+ Threshold')
negdb, = ax.plot(x, db-deadband, color='b', linestyle='--', label='- Threshold')

# Provide Information on Plot
fig.suptitle('Analog Deadband Example')
fig.legend(loc=(0.54,0.12))
ax.set_xlabel('time')
ax.set_ylabel('value')

# Define Plot Updating Function
def update(num, x, y, db, line, dblin, posdb, negdb):
    line.set_data(x[:num], y[:num])
    line.axes.axis([0, maximum, 0, maximum*3])
    dblin.set_data(x[:num], db[:num])
    dblin.axes.axis([0, maximum, 0, maximum*3])
    posdb.set_data(x[:num], db[:num]+deadband)
    negdb.set_data(x[:num], db[:num]-deadband)
    posdb.axes.axis([0, maximum, 0, maximum*3])
    negdb.axes.axis([0, maximum, 0, maximum*3])
    return line, dblin, posdb, negdb,

# Animate the Plot
ani = animation.FuncAnimation(fig, update, len(x),
                              fargs=[x, y, db, line, dblin, posdb, negdb],
                              interval=35, blit=True)
# Save the Plot
ani.save('images/deadbandexample.gif')
fig.savefig('images/deadbandexample.png')
plt.show()
