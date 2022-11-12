import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kassa_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_kassan_rahamaara_ja_lounasmaarat_oikein_alussa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_toimii_edulliset_raha_riittaa(self):
        self.kassapaate.syo_edullisesti_kateisella(300)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(str(self.kassapaate.syo_edullisesti_kateisella(300)), "60")

    def test_kateisnosto_toimii_maukkaat_raha_riittaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(str(self.kassapaate.syo_maukkaasti_kateisella(500)), "100")

    def test_kateisosto_toimii_edulliset_raha_ei_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(str(self.kassapaate.syo_edullisesti_kateisella(200)), "200")

    def test_kateisosto_toimii_maukkaat_raha_ei_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(str(self.kassapaate.syo_maukkaasti_kateisella(200)), "200")

    def test_korttiosto_toimii_edulliset_kortilla_tarpeeksi_rahaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.60 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        return True

    def test_korttiosto_toimii_edulliset_kortilla_ei_tarpeeksi_rahaa(self):
        self.maksukortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 2.00 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        return False

    def test_korttiosto_toimii_maukkaat_kortilla_tarpeeksi_rahaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 6.00 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        return True

    def test_korttiosto_toimii_maukkaat_kortilla_ei_tarpeeksi_rahaa(self):
        self.maksukortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 2.00 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        return False

    def test_kortille_rahaa_ladattaessa_kortin_ja_kassan_saldo_muuttuu_positiivinen_summa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 20.00 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)

    def test_kortille_rahaa_ladattaessa_kortin_ja_kassan_saldo_muuttuu_negatiivinen_summa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)