# Vector-Field Neural Network
Source provides two packages: `vfneunet` and `faketrader` for use with high frequency trading applications.

`vfneunet` provides a neural network providing n x n linear transformations on streaming data.   
`faketrader` provides distributed applications for tracking and executing trades based on activity from data input.
___
## Installation Instructions
### Generating environment:
For anaconda-environments:
```cmd
conda env create -f environment.yml
source activate vfneunet
```
virtualenv can be created manually.

### Installing packages:
```cmd
pip install ./vfneunet ./faketrader
python -u build/main/main.py
```
