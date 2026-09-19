# Digital Communication System Simulator (BPSK/QPSK over AWGN)

A Python-based simulation of digital modulation schemes (**BPSK** and **QPSK**)
transmitted over an **AWGN (Additive White Gaussian Noise) channel**, with
**Bit Error Rate (BER) vs Eb/N0** analysis — the standard performance metric
used to evaluate real-world digital communication systems.

## What this project does

1. Generates random binary data (the "message" to transmit).
2. Modulates the bits into BPSK and QPSK symbols.
3. Passes the symbols through a simulated noisy (AWGN) channel.
4. Demodulates the received (noisy) symbols back into bits.
5. Compares transmitted vs received bits to compute the **Bit Error Rate**.
6. Repeats this across a range of signal-to-noise ratios (Eb/N0, 0–10 dB).
7. Plots simulated BER curves against the theoretical BPSK BER curve.

## Why this matters (for your CV / viva)

This is the same core technique used to evaluate real wireless/telecom
systems before deployment. Being able to explain:
- what BER and Eb/N0 mean,
- why QPSK carries 2x the data rate of BPSK for similar noise performance,
- and how simulated results align with theory,

demonstrates solid understanding of digital communication fundamentals —
a strong talking point in interviews and vivas.

## Project structure

```
digital-comm-simulator/
├── modulation.py     # BPSK/QPSK modulation & demodulation functions
├── channel.py         # AWGN noise channel simulation
├── simulate.py         # Main script: runs experiment, plots BER curve
├── requirements.txt    # Python dependencies
└── README.md
```

## Setup instructions (step by step)

### 1. Install Python
Make sure Python 3.8+ is installed. Check with:
```bash
python3 --version
```
If not installed, download from https://www.python.org/downloads/

### 2. Download/clone this project
If you're pushing this to GitHub yourself, place these files in a folder,
e.g. `digital-comm-simulator/`.

### 3. Install dependencies
From inside the project folder:
```bash
pip install -r requirements.txt
```

### 4. Run the simulation
```bash
python simulate.py
```

This will:
- print BER values for each Eb/N0 level in the terminal
- save a plot as `ber_vs_snr.png`
- display the plot in a window

## Understanding the output

- **X-axis (Eb/N0 in dB):** signal quality — higher = less noisy channel
- **Y-axis (BER, log scale):** fraction of bits received incorrectly
- As Eb/N0 increases, BER should drop sharply (fewer errors) — this is
  the expected "waterfall curve" seen in all real communication systems.
- Your simulated BPSK curve should closely match the black dashed
  theoretical curve — this validates your simulation is correct.

## How to extend this (optional, for a stronger project/paper)

Once the basic version works, you can add:
- **8-PSK or 16-QAM** modulation schemes for comparison
- **Channel coding** (e.g., Hamming code or convolutional coding) to show
  error correction improving BER
- **Rayleigh fading channel** instead of just AWGN (models real wireless
  multipath environments — used heavily in research papers)
- A **Jupyter notebook** version with more visualizations and explanations
- **OFDM simulation** (used in 4G/5G/WiFi) as a bigger extension

Any of these upgrades would strengthen this into a genuinely
publishable/paper-worthy mini-project.

## Pushing this to GitHub

From inside the project folder:
```bash
git init
git add .
git commit -m "Initial commit: BPSK/QPSK BER simulation over AWGN channel"
git branch -M main
git remote add origin https://github.com/<your-username>/digital-comm-simulator.git
git push -u origin main
```
(Create the empty repository on GitHub first, then copy its URL into the
`git remote add` command above.)

## Suggested CV bullet point

> Built a Python-based simulator for BPSK/QPSK digital modulation over an
> AWGN channel, analyzing Bit Error Rate performance across varying SNR
> levels and validating results against theoretical error bounds.

## Tech stack
- Python 3
- NumPy (signal generation & math)
- Matplotlib (plotting results)
- SciPy (theoretical error function calculations)
