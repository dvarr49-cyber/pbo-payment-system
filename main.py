from core.processor import PaymentProcessor
from core.notifiers import ConsoleNotifier
from plugins.transfer_bank import TransferBank

# Membuat objek notifier
notifier = ConsoleNotifier()

# Membuat payment processor
processor = PaymentProcessor(notifier)

# Membuat metode pembayaran
transfer = TransferBank(saldo=500_000, bank="BCA")

# Memproses pembayaran
print("=== PEMBAYARAN BERHASIL ===")
processor.proses(transfer, 150_000, "Devar")

print("Saldo tersisa:", transfer.saldo)

# Menguji pembayaran gagal
print("\n=== PEMBAYARAN GAGAL ===")
try:
    processor.proses(transfer, 1_000_000, "Devar")
except Exception as e:
    print("Error:", e)