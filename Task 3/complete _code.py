LAYERS = [("Application", "HTTP"), ("Transport", "TCP"), ("Network", "IP"), ("Data link", "ETH")]

def send(message):
    pdu = message
    for layer, tag in LAYERS:
        head = "[" + tag + "|"
        tail = "|FCS]" if tag == "ETH" else "]"
        pdu = head + pdu + tail
        print(f"{layer:<12} adds {tag:<3} -> {len(pdu)} bytes")
    return pdu

def receive(frame):
    pdu = frame
    for layer, tag in reversed(LAYERS):
        head = "[" + tag + "|"
        tail = "|FCS]" if tag == "ETH" else "]"
        assert pdu.startswith(head) and pdu.endswith(tail), f"{layer}: bad header"
        pdu = pdu[len(head):-len(tail)]
    return pdu

for message in ("GET /results", "A"*1400):
    print("\nMESSAGE LENGTH:", len(message))
    frame = send(message)
    print("on the wire:", frame if len(message) < 100 else frame[:60] + "..."+frame[-20:])
    print("delivered length:", len(receive(frame)))
    print(f"overhead: {len(frame)-len(message)} bytes; percentage: {(len(frame)-len(message))/len(frame)*100:.2f}%")
