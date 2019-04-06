from faketrader.executors import *
import logging

class TradingApplication:
    """
    Trading application that manages data flow among distributed nodes.

    Current order support:
        - BUY
        - SELL
        - BUY FUT
        - SELL FUT
        - BUY CALL
        - BUY PUT
    """
    def __init__(self, *args, **kwargs):
        """
        Arguments:
            args: List of exchange/symbols to track
            kwargs:
                name: Application name
                executors: Number of nodes
                file: File to pull symbols from
                symbols: List of symbols to read
                verbose: Log verbosity (1-3)
        """
        self.count = kwargs['executors']
        self.streams = {}

    def __del__(self):
        for id, stream in self.streams.items():
            stream.cancel
            del stream

    def cancel(self):
        del self

    def genStream(self, *args, **kwargs):
        """
        Generates a stream
        """
        return -1

    @property
    def addStreamListener(self, id, *args, **kwargs):
        self.streams[f"{id}"] =  self.genStream(*args, **kwargs)
        return self.streams
    