from core.base import PaymentMethod
from core.registry import register_plugin
from core.utils import buat_id


@register_plugin("qris")
class QRIS(PaymentMethod):
    BATAS_TRANSAKSI = 5_000_000

    def __init__(self, saldo: float = 0):
        super().__init__("QRIS")
        self.saldo = saldo

    def validasi(self, jumlah: float) -> bool:
        return jumlah <= self.BATAS_TRANSAKSI and self.saldo >= jumlah

    def bayar(self, jumlah: float) -> str:
        self.saldo -= jumlah
        return buat_id("QRS")