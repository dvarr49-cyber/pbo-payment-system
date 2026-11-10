import uuid

def rupiah(nilai: float) -> str:
    """Format angka menjadi Rp1.250.000."""
    return "Rp" + f"{nilai:,.0f}".replace(",", ".")

def buat_id(prefix: str) -> str:
    """Buat ID transaksi unik."""
    return f"{prefix}-{uuid.uuid4().hex[:8].upper()}"