from faketrader.run import *

"""
The module `faketrader` provides resources to execute trades on a distributed platform
  based on a data stream provided by vfneunet.

run.py:
    - TradingApplication: initializes NodeFactory, accepts a data source and output location

`faketrader.executors`
"""

__all__ =  ['TradingApplication',
            'AppReader',
            'AppWriter',
            'executors']
