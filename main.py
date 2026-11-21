"""Entri koran satu halaman untuk kompetisi make.fun news-image-20261120.

Halaman depan bergaya klasik di atas kertas krem berjudul "THE WORLD IN
ONE DAY" ini merangkum hari Jumat, 20 November 2026: 40 cerita yang
dipetik dari 8 region dunia, disusun seperti koran cetak — berita utama
di atas, kolom-kolom berita di bawahnya, lengkap dengan peta dan daftar
cek tanggal di bagian kaki halaman.

Tugas skrip ini sesederhana mungkin: gambar final sudah jadi dan tersimpan
sebagai image.png di samping berkas ini. Saat dijalankan, skrip hanya
menyalinkannya ke /output/entry.png tanpa mengubah satu byte pun, supaya
yang dinilai panitia adalah gambar yang persis sama dengan yang dibuat.
"""

import hashlib
import os
import shutil
import sys


def cari_gambar_sumber():
    """Kembalikan path absolut image.png yang duduk sebelahan dengan skrip ini."""
    folder_skrip = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(folder_skrip, "image.png")


def sidik_jari(path_berkas):
    """Hitung SHA-256 sebuah berkas, dibaca potongan demi potongan."""
    pencerna = hashlib.sha256()
    with open(path_berkas, "rb") as gagang:
        while True:
            potongan = gagang.read(1024 * 1024)
            if not potongan:
                break
            pencerna.update(potongan)
    return pencerna.hexdigest()


def antar_ke_output(sumber, tujuan):
    """Salin berkas sumber ke tujuan, buat folder tujuan bila belum ada."""
    os.makedirs(os.path.dirname(tujuan), exist_ok=True)
    shutil.copyfile(sumber, tujuan)
    return tujuan


def main():
    berkas_asal = cari_gambar_sumber()
    berkas_tujuan = "/output/entry.png"

    if not os.path.isfile(berkas_asal):
        print(f"image.png tidak ditemukan di {berkas_asal}", file=sys.stderr)
        return 1

    antar_ke_output(berkas_asal, berkas_tujuan)

    asal = sidik_jari(berkas_asal)
    hasil = sidik_jari(berkas_tujuan)
    if asal != hasil:
        print("Salinan tidak identik dengan aslinya!", file=sys.stderr)
        return 1

    print(f"entry tersalin: {berkas_tujuan} (sha256 {hasil})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
