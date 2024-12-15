from scapy.all import RawPcapReader

# Open the PCAP file
with RawPcapReader('PCAPdroid_15_Nov_16_56_33.pcap') as reader:
    for (pkt_data, pkt_metadata,) in reader:
        # Get the timestamp
        tshigh = pkt_metadata.sec
        tslow = pkt_metadata.usec

        # Convert the timestamp to a Unix timestamp (microseconds since epoch)
        timestamp = (tshigh << 32) + tslow

        # Convert the timestamp to a human-readable format
        timestamp_str = f"{timestamp:.3f}"
        print(timestamp_str)
