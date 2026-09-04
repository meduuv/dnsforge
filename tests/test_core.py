import unittest
from unittest.mock import patch

from dnsforge.core import lookup


class LookupTests(unittest.TestCase):
    @patch("dnsforge.core.socket.getaddrinfo", return_value=[(2, 1, 6, "", ("192.0.2.1", 0)), (2, 1, 6, "", ("192.0.2.1", 0))])
    def test_lookup_deduplicates_addresses(self, resolver):
        records = lookup("example.test")
        self.assertEqual([record.value for record in records], ["192.0.2.1"])
        resolver.assert_called_once()

    def test_rejects_unknown_type(self):
        with self.assertRaises(ValueError):
            lookup("example.test", "AXFR")


if __name__ == "__main__":
    unittest.main()
