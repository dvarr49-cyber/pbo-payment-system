import pytest

from core.base import PaymentMethod
from core.registry import buat_metode


def test_abc_tidak_bisa_diinstansiasi():
    with pytest.raises(TypeError):
        PaymentMethod("Pembayaran Tes")


def test_plugin_tidak_dikenal_memunculkan_keyerror():
    with pytest.raises(KeyError):
        buat_metode("plugin_tidak_dikenal")