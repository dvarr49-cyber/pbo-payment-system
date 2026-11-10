from core.base import PaymentMethod
from plugins.transfer_bank import TransferBank


metode: PaymentMethod = TransferBank(saldo=100_000)

print(isinstance(metode, PaymentMethod))

# Contoh kesalahan tipe untuk dideteksi mypy:
metode.proses("seratus")