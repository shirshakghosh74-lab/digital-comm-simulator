"""
simulate.py
-----------
Main script: simulates BPSK and QPSK transmission over an AWGN channel
across a range of Eb/N0 values, measures Bit Error Rate (BER), and plots
simulated results against the theoretical BER curve.

Run this file to generate results:
    python simulate.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc

from modulation import bpsk_modulate, bpsk_demodulate, qpsk_modulate, qpsk_demodulate
from channel import awgn


def run_bpsk_simulation(num_bits, eb_n0_db_range):
    ber_results = []
    for eb_n0_db in eb_n0_db_range:
        bits = np.random.randint(0, 2, num_bits)
        tx_symbols = bpsk_modulate(bits)
        rx_symbols = awgn(tx_symbols, eb_n0_db, bits_per_symbol=1)
        rx_bits = bpsk_demodulate(rx_symbols)

        errors = np.sum(bits != rx_bits)
        ber = errors / num_bits
        ber_results.append(ber)
        print(f"[BPSK] Eb/N0 = {eb_n0_db:>3} dB | BER = {ber:.6f}")
    return ber_results


def run_qpsk_simulation(num_bits, eb_n0_db_range):
    ber_results = []
    for eb_n0_db in eb_n0_db_range:
        bits = np.random.randint(0, 2, num_bits)
        tx_symbols = qpsk_modulate(bits)
        rx_symbols = awgn(tx_symbols, eb_n0_db, bits_per_symbol=2)
        rx_bits = qpsk_demodulate(rx_symbols)

        # trim in case of odd-length padding
        rx_bits = rx_bits[:len(bits)]

        errors = np.sum(bits != rx_bits)
        ber = errors / num_bits
        ber_results.append(ber)
        print(f"[QPSK] Eb/N0 = {eb_n0_db:>3} dB | BER = {ber:.6f}")
    return ber_results


def theoretical_bpsk_ber(eb_n0_db_range):
    """Theoretical BER for BPSK: BER = 0.5 * erfc(sqrt(Eb/N0))"""
    eb_n0_linear = 10 ** (np.array(eb_n0_db_range) / 10)
    return 0.5 * erfc(np.sqrt(eb_n0_linear))


def main():
    num_bits = 200_000          # more bits = smoother/more accurate curve
    eb_n0_db_range = np.arange(0, 11, 1)  # 0 dB to 10 dB

    print("Running BPSK simulation...")
    bpsk_ber = run_bpsk_simulation(num_bits, eb_n0_db_range)

    print("\nRunning QPSK simulation...")
    qpsk_ber = run_qpsk_simulation(num_bits, eb_n0_db_range)

    theory_ber = theoretical_bpsk_ber(eb_n0_db_range)

    # --- Plot results ---
    plt.figure(figsize=(9, 6))
    plt.semilogy(eb_n0_db_range, bpsk_ber, 'o-', label='BPSK (Simulated)')
    plt.semilogy(eb_n0_db_range, qpsk_ber, 's-', label='QPSK (Simulated)')
    plt.semilogy(eb_n0_db_range, theory_ber, 'k--', label='BPSK (Theoretical)')

    plt.xlabel('Eb/N0 (dB)')
    plt.ylabel('Bit Error Rate (BER)')
    plt.title('BER Performance of BPSK and QPSK over AWGN Channel')
    plt.grid(True, which='both', linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig('ber_vs_snr.png', dpi=150)
    print("\nPlot saved as ber_vs_snr.png")
    plt.show()


if __name__ == "__main__":
    main()
