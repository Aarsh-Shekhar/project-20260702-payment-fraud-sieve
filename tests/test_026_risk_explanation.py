import unittest

from payment_fraud_sieve.models import Record
from payment_fraud_sieve.scoring import score_record


class DepthCheck26(unittest.TestCase):
    def test_026_risk_explanation(self):
        record = Record(id="payment-026", exposure=70635, signal=0.843, urgency=5)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
