import unittest

from payment_fraud_sieve.models import Record
from payment_fraud_sieve.scoring import score_record


class DepthCheck59(unittest.TestCase):
    def test_059_reporting_view(self):
        record = Record(id="payment-059", exposure=64194, signal=0.377, urgency=7)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
