from __future__ import absolute_import
import unittest

#from trade import Accumulator as AssetAccumulator, Event
#from trade import Asset, Operation
import trade


class StockSplit(trade.Event):

    def __init__(self, date, asset,  factor):
        self.factor = factor
        self.asset = asset
        self.date = date

    def update_portfolio(self, quantity, price, results):
        quantity = quantity * self.factor
        price = price / self.factor
        return quantity, price


class Test_accumulate_event_Case_00(unittest.TestCase):

    def setUp(self):
        self.asset = trade.Asset()
        self.operation = trade.Operation(
                            quantity=100,
                            price=10,
                            asset=self.asset,
                            date='2015-01-01'
                        )
        self.event = StockSplit('2015-09-24', self.asset, 2)
        self.accumulator = trade.Accumulator(self.asset, logging=True)
        self.accumulator.accumulate_operation(self.operation)
        self.accumulator.accumulate_event(self.event)

    def test_accumulator_price(self):
        self.assertEqual(self.accumulator.price, 5)

    def test_accumulator_quantity(self):
        self.assertEqual(self.accumulator.quantity, 200)


class Test_accumulate_event_Case_01(unittest.TestCase):

    def setUp(self):
        self.asset = trade.Asset()
        self.other_asset = trade.Asset('other')
        self.operation = trade.Operation(
                            quantity=100,
                            price=10,
                            asset=self.asset,
                            date='2015-01-01'
                        )
        self.event = StockSplit('2015-09-24', self.other_asset, 2)
        self.accumulator = trade.Accumulator(self.asset, logging=True)
        self.accumulator.accumulate_operation(self.operation)
        self.accumulator.accumulate_event(self.event)

    def test_accumulator_price(self):
        self.assertEqual(self.accumulator.price, 5)

    def test_accumulator_quantity(self):
        self.assertEqual(self.accumulator.quantity, 200)
