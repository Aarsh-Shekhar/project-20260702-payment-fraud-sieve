import unittest

from payment_fraud_sieve.models import Record
from payment_fraud_sieve.scoring import score_record


class DepthCheck20(unittest.TestCase):
    def test_020_threshold_calibration(self):
        record = Record(id="payment-020", exposure=33265, signal=0.483, urgency=2)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
