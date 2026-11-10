from core.base import PaymentMethod, PembayaranGagal
from core.protocols import Notifier
from core.utils import rupiah


class PaymentProcessor:
    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def proses(
        self,
        metode: PaymentMethod,
        jumlah: float,
        penerima: str
    ) -> str:
        try:
            transaksi_id = metode.proses(jumlah)
            pesan = (
                f"Pembayaran {rupiah(jumlah)} berhasil. "
                f"ID: {transaksi_id}"
            )
            self.notifier.kirim(penerima, pesan)
            return transaksi_id
        except PembayaranGagal as e:
            self.notifier.kirim(penerima, f"Pembayaran gagal: {e}")
            raise