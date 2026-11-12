import math
def nyquist(bandwidth_hz, levels):
    return 2 * bandwidth_hz * math.log2(levels)
def shannon(bandwidth_hz, snr_db):
    snr = 10 ** (snr_db / 10)
    return bandwidth_hz * math.log2(1 + snr)
media = [("Telephone line", 3100, 30), ("Cat6 pair", 250e6, 40), ("Wi-Fi 6 channel", 160e6, 25)]
for name, bw, snr in media:
    print(f"{name:<16} Shannon limit {shannon(bw, snr)/1e6:10.2f} Mbps")
print(f"Nyquist, 3,100 Hz with 4 levels: {nyquist(3100,4)/1e3:.1f} kbps")
print(f"Cat6 at 15 dB SNR: {shannon(250e6,15)/1e6:.2f} Mbps")
print(f"Wi-Fi 6 at 15 dB SNR: {shannon(160e6,15)/1e6:.2f} Mbps")
snr_req=10*math.log10(2**(56000/3100)-1)
print(f"SNR required for 56 kbps on 3100 Hz: {snr_req:.2f} dB")
