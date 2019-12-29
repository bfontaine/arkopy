# -*- coding: UTF-8 -*-


import unittest
import arko


class ArkoTest(unittest.TestCase):
    def test_parse(self):
        self.assertEqual(42, arko.parse("i:42"))


    def test_dump(self):
        self.assertEqual("i:2", arko.dump(2))
        self.assertEqual("b:1", arko.dump(True))
        self.assertEqual('s:4:"abcd"', arko.dump("abcd"))


    def test_roundtrip(self):
        # real-life payloads
        for payload in (
                ("YTo0OntzOjQ6ImRhdGUiO3M6MTA6IjIwMTktMTItMjkiO3M6MTA6In"
                    "R5cGVfZm9uZHMiO3M6MTE6ImFya29fc2VyaWVsIjtzOjQ6InJlZjEiO2k"
                    "6MTI7czo0OiJyZWYyIjtpOjQ2Njk7fQ=="),
                ("YTo2OntzOjQ6ImRhdGUiO3M6MTA6IjIwMTktMTItMjkiO3M6MTA6InR5cGVf"
                    "Zm9uZHMiO3M6MTE6ImFya29fc2VyaWVsIjtzOjQ6InJlZjEiO2k6MTI7c"
                    "zo0OiJyZWYyIjtpOjQ2Njk7czoxNjoidmlzaW9ubmV1c2VfaHRtbCI7Yj"
                    "oxO3M6MjE6InZpc2lvbm5ldXNlX2h0bWxfbW9kZSI7czo0OiJwcm9kIjt"
                    "9"),
        ):
            decoded = arko.decode(payload)
            parsed = arko.parse(decoded)
            dumped = arko.dump(parsed)

            self.assertEqual(decoded, dumped)

            encoded = arko.encode(dumped)
            self.assertEqual(payload, encoded)

if __name__ == "__main__":
    unittest.main()
