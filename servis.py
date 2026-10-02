#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Buzdolabi Isigi Istihbarat Servisi.

Kapinin arkasindaki isik yaninca devreye giren, gereginden resmi brifing motoru.
Gercekten calisir. Gercekten bir ise yaramaz. Ikisi de tasarimdir.
"""

from __future__ import annotations

import hashlib
import random
import textwrap
from datetime import datetime


BAHANELER = {
    "su": "Hidrasyon operasyonu. Inandirici ama zayif.",
    "yemek": "Lojistik ikmal. Mutfak kurmay heyeti not dustu.",
    "bakmak": "Kesif gorevi. Hedef belirsiz, isik kesin.",
    "canim sikildi": "Moral istihbarati. Peynir masum degildir.",
    "gece": "Karanlik saat baskini. Tutanak agirlasti.",
}


def tehdit_kodu(gerekce: str) -> str:
    oz = hashlib.sha256(gerekce.encode("utf-8")).hexdigest()[:8].upper()
    return f"BIIS-{oz}"


def siniflandir(gerekce: str) -> str:
    g = gerekce.casefold()
    for anahtar, hukum in BAHANELER.items():
        if anahtar in g:
            return hukum
    return "Siniflandirilamadi. Suphe varsayilan politikadir."


def brifing(gerekce: str) -> str:
    simdi = datetime.now().strftime("%d.%m.%Y %H:%M")
    seviye = random.choice(["DUSUK", "ORTA", "YUKSEK", "KAPI ARALIGI"])
    metin = f"""
    BII S BRIFINGI  |  {tehdit_kodu(gerekce)}
    Tarih: {simdi}
    Gerekce: {gerekce.strip() or 'beyan yok'}
    Hukum: {siniflandir(gerekce)}
    Tehdit seviyesi: {seviye}
    Tavsiye: Kapıyı kapat. Raporu sakla. Yarın yine aç.
    """
    return textwrap.dedent(metin).strip()


def main() -> None:
    print("BUZDOLABI ISIGI ISTIHBARAT SERVISI")
    print("Isik yandiysa konus. Yanmadiysa da konus, biz yine yazariz.")
    gerekce = input("Neden actiniz? ")
    print()
    print(brifing(gerekce))
    print()
    print("DAMGA: BIIS-02 | Kayyum Grok | 02.10.2026 | imza: isik")


if __name__ == "__main__":
    main()
