"""
modulation.py
-------------
Implements modulation and demodulation for BPSK and QPSK.

Modulation = converting bits (0s and 1s) into signal symbols that can be
transmitted. Demodulation = the reverse process at the receiver.
"""

import numpy as np


def bpsk_modulate(bits):
    """
    BPSK: Binary Phase Shift Keying.
    Maps bit 0 -> -1, bit 1 -> +1.

    Parameters:
        bits (np.array): array of 0s and 1s

    Returns:
        np.array of modulated symbols (complex, but imaginary part = 0)
    """
    symbols = 2 * bits - 1  # 0 -> -1, 1 -> +1
    return symbols.astype(complex)


def bpsk_demodulate(received_symbols):
    """
    Demodulate BPSK: if real part > 0 -> bit 1, else bit 0.
    """
    bits = (received_symbols.real > 0).astype(int)
    return bits


def qpsk_modulate(bits):
    """
    QPSK: Quadrature Phase Shift Keying.
    Groups bits in pairs, maps each pair to one of 4 symbols
    (each symbol carries 2 bits of information).

    Bit pairs -> symbol (using Gray coding):
        00 -> (-1 - 1j)
        01 -> (-1 + 1j)
        10 -> ( 1 - 1j)
        11 -> ( 1 + 1j)
    All scaled by 1/sqrt(2) to normalize average energy to 1.

    Parameters:
        bits (np.array): array of 0s and 1s, length must be even

    Returns:
        np.array of complex modulated symbols
    """
    if len(bits) % 2 != 0:
        bits = np.append(bits, 0)  # pad with a 0 if odd length

    bits = bits.reshape(-1, 2)
    i_bits = bits[:, 0]
    q_bits = bits[:, 1]

    i_component = 2 * i_bits - 1  # 0 -> -1, 1 -> +1
    q_component = 2 * q_bits - 1

    symbols = (i_component + 1j * q_component) / np.sqrt(2)
    return symbols


def qpsk_demodulate(received_symbols):
    """
    Demodulate QPSK: sign of real part -> first bit,
    sign of imaginary part -> second bit.
    """
    i_bits = (received_symbols.real > 0).astype(int)
    q_bits = (received_symbols.imag > 0).astype(int)

    bits = np.empty(2 * len(received_symbols), dtype=int)
    bits[0::2] = i_bits
    bits[1::2] = q_bits
    return bits
