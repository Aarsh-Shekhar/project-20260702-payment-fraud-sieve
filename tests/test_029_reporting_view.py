import unittest

from payment_fraud_sieve.models import Record
from payment_fraud_sieve.scoring import score_record


class DepthCheck29(unittest.TestCase):
    def test_029_reporting_view(self):
        record = Record(id="payment-029", exposure=22499, signal=0.517, urgency=3)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
