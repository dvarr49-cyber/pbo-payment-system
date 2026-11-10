from datetime import datetime, timedelta

from core.base import PaymentMethod
from core.registry import register_plugin
from core.utils import buat_id


@register_plugin("virtual_account")
class VirtualAccount(PaymentMethod):
    def __init__(
        self,
        batas_waktu_detik: int = 300,
        nama_bank: str = "Bank Kampus",
    ):
        super().__init__(f"Virtual Account {nama_bank}")
        self.status = "menunggu"
        self.batas_waktu = datetime.now() + timedelta(
            seconds=batas_waktu_detik
        )

    def validasi(self, jumlah: float) -> bool:
        if datetime.now() > self.batas_waktu:
            self.status = "kedaluwarsa"
            return False

        return self.status == "menunggu"

    def biaya_admin(self, jumlah: float) -> float:
        return 0.0

    def bayar(self, jumlah: float) -> str:
        self.status = "dibayar"
        return buat_id("VA")