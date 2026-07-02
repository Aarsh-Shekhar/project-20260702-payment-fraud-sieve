import unittest

from payment_fraud_sieve.models import Record
from payment_fraud_sieve.scoring import score_record


class DepthCheck41(unittest.TestCase):
    def test_041_edge_case_review(self):
        record = Record(id="payment-041", exposure=19437, signal=0.858, urgency=9)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
