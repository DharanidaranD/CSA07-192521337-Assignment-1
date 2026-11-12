# Task 1 - Traffic sizing
robot = 40 * (200/0.002) * 8
sensors = 600 * 50 * 8
cctv = 24 * 4_000_000
office = 150 * 2_000_000 * 0.10
total = robot + sensors + cctv + office
alternative = robot + sensors + cctv*0.05 + office
print(f"Robot controllers: {robot/1e6:.2f} Mbps")
print(f"Vibration sensors: {sensors/1e6:.2f} Mbps")
print(f"CCTV: {cctv/1e6:.2f} Mbps")
print(f"Office: {office/1e6:.2f} Mbps")
print(f"Total per line: {total/1e6:.2f} Mbps")
print(f"8 lines: {total*8/1e6:.2f} Mbps")
print(f"5% CCTV alternative: {alternative/1e6:.2f} Mbps")
