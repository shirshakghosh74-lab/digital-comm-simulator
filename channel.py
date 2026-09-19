"""
channel.py
----------
Simulates an AWGN (Additive White Gaussian Noise) channel.

Every real communication channel (wireless, fiber, etc.) adds random noise
to the transmitted signal. AWGN is the standard, simplest model used to
represent this noise in simulations.
"""

import numpy as np


def awgn(symbols, eb_n0_db, bits_per_symbol):
    """
    Add AWGN noise to modulated symbols based on a target Eb/N0 (in dB).

    Eb/N0 = energy per bit / noise power spectral density.
    This is the standard way to express "signal quality" in digital
    communication research and papers.

    Parameters:
        symbols (np.array): complex modulated symbols (unit average energy)
        eb_n0_db (float): desired Eb/N0 in dB
        bits_per_symbol (int): 1 for BPSK, 2 for QPSK

    Returns:
        np.array: noisy received symbols
    """
    eb_n0_linear = 10 ** (eb_n0_db / 10)

    # Energy per symbol = bits_per_symbol * Eb (assuming Eb = 1 here since
    # our symbols already have unit average energy)
    es_n0_linear = eb_n0_linear * bits_per_symbol

    # Noise spectral density N0, then noise variance per dimension
    noise_variance = 1 / (2 * es_n0_linear)

    noise = np.sqrt(noise_variance) * (
        np.random.randn(len(symbols)) + 1j * np.random.randn(len(symbols))
    )

    return symbols + noise
