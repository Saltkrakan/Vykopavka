# -*- coding: utf-8 -*-
import sys

def liniovka(sazba_linie, delka, doprava_1_km, vzdalenost_v_km):
    cena = (sazba_linie * delka) + (doprava_1_km * 2 * vzdalenost_v_km)
    return(cena)