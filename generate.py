import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", type=str, help="Name of job to execute.")
parser.add_argument("-e", "--executors", type=int, help="Number of executor nodes to initialize.")
parser.add_argument("-f", "--file", type=str, help="File containing list of exchanges/symbols to track.")
parser.add_argument("-s", "--symbols", nargs="+", help="List of symbols to track.")
parser.add_argument("-v", "--verbose", action="count", help="Log verbosity.  -v to -vvv")
setup = parser.parse_args()

from faketrader.run import TradingApplication

"""
Generate trading application using arguments
"""
app = TradingApplication(**vars(setup))
app.cancel()