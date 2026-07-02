import unittest

from payment_fraud_sieve.models import Record
from payment_fraud_sieve.scoring import score_record


class DepthCheck62(unittest.TestCase):
    def test_062_operator_handoff(self):
        record = Record(id="payment-062", exposure=62339, signal=0.641, urgency=2)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
