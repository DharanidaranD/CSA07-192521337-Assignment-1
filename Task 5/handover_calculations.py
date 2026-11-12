route=1200
wifi_spacing=30
wifi_handover=0.150
g5_cell=300
g5_handover=0.020
wifi_handover_count=route//wifi_spacing-1
g5_handover_count=route//g5_cell-1
print("Wi-Fi handovers:", wifi_handover_count)
print("Wi-Fi unreachable time:", wifi_handover_count*wifi_handover, "s")
print("5G handovers:", g5_handover_count)
print("5G unreachable time:", g5_handover_count*g5_handover, "s")
sensor_bps=600*50*8
print("600 sensors:", sensor_bps/1000, "kbps")
print("LoRa gateway capacity:", 5, "kbps")
