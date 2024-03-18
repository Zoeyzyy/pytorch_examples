# 1s
python3 parse_by_time.py --accuracy=8 --pcap_file from106 &
python3 parse_by_time.py --accuracy=8 --pcap_file from108 &
python3 parse_by_time.py --accuracy=8 --pcap_file to106 &
python3 parse_by_time.py --accuracy=8 --pcap_file to108 &

# 0.1s
python3 parse_by_time.py --accuracy=10 --pcap_file from106 &
python3 parse_by_time.py --accuracy=10 --pcap_file from108 &
python3 parse_by_time.py --accuracy=10 --pcap_file to106 &
python3 parse_by_time.py --accuracy=10 --pcap_file to108 &

# 0.01s
python3 parse_by_time.py --accuracy=11 --pcap_file from106 &
python3 parse_by_time.py --accuracy=11 --pcap_file from108 &
python3 parse_by_time.py --accuracy=11 --pcap_file to106 &
python3 parse_by_time.py --accuracy=11 --pcap_file to108 &

# 0.001s
python3 parse_by_time.py --accuracy=12 --pcap_file from106 &
python3 parse_by_time.py --accuracy=12 --pcap_file from108 &
python3 parse_by_time.py --accuracy=12 --pcap_file to106 &
python3 parse_by_time.py --accuracy=12 --pcap_file to108 &