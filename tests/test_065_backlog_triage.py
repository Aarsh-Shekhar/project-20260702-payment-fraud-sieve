import unittest

from payment_fraud_sieve.models import Record
from payment_fraud_sieve.scoring import score_record


class DepthCheck65(unittest.TestCase):
    def test_065_backlog_triage(self):
        record = Record(id="payment-065", exposure=9899, signal=0.645, urgency=3)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
