import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_lataus_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 20.00 euroa")

    def test_rahan_ottaminen_toimii_kortilla_on_rahaa(self):
        self.maksukortti.ota_rahaa(500)
        if self.maksukortti.saldo >= 500:
            self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")
            return True

    def test_rahan_ottaminen_toimii_kortilla_ei_ole_rahaa(self):
        self.maksukortti.ota_rahaa(1500)
        if self.maksukortti.saldo < 1500:
            self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
            return False
