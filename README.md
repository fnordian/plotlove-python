PlotLove - Python client
========================

Plotlove-python lets you push datapoints to [plot.love](http://plot.love) easily where you can view than plotted in a diagram.

Usage
-----

```python
import math
from plotlove import Measurement

m = Measurement(name="sincos", x_column_name="x")
xradx = [ (x, (x / 360 * 2 * math.pi)) for x in range(360) ]
for (x, radx) in xradx:
    m.log_measurement(data={"x": x, "sin": math.sin(radx), "cos": math.cos(radx)})

print(m.plot_url())
```

Visit the plot url (```m.plot_url```) with your browser.
