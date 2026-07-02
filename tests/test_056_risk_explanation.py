import unittest

from payment_fraud_sieve.models import Record
from payment_fraud_sieve.scoring import score_record


class DepthCheck56(unittest.TestCase):
    def test_056_risk_explanation(self):
        record = Record(id="payment-056", exposure=66922, signal=0.355, urgency=6)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
