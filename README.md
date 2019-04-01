# LinearRegression
PyQt application to build linear regression.
Features added:
  * Csv table viewer
  
  ![Table viewer](https://github.com/IntergraDev/LinearRegression/blob/f06ea3304afe1efa53fedf99fbc4b9c162a422a7/screens/app_table.jpg)
  
  * Mplotlib widget integration
  * Show/Hide source data (scatter) and regression result
  
  ![Plot widget](https://github.com/IntergraDev/LinearRegression/blob/f06ea3304afe1efa53fedf99fbc4b9c162a422a7/screens/app_plot.jpg)
  
  * Output of model parameters
  
  ![Model output](https://github.com/IntergraDev/LinearRegression/blob/f06ea3304afe1efa53fedf99fbc4b9c162a422a7/screens/app_output.jpg)
  
  * Clear all data function (table, plot, output)

# Converting .ui file to .py
To make .py file from .ui execute:
```python -m PyQt5.uic.pyuic <src_filepath>.ui -o <target_filepath>.py -x``` in terminal.

Use ```pyrcc5 -o resource_rc.py resource.qrc``` to apply changes made in .qrc file
