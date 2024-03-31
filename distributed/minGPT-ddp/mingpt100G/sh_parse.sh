rm ./*.png 
tcpdump -r ../../../from106.pcap > ../../../from106.txt 
tcpdump -r ../../../to106.pcap > ../../../to106.txt 
python3 parse.py  --sender=106 --reciever=108 --pcap_file from106 & 
python3 parse.py  --sender=108 --reciever=106 --pcap_file to106 & 
tcpdump -r ../../../from112.pcap > ../../../from112.txt 
tcpdump -r ../../../to112.pcap > ../../../to112.txt 
python3 parse.py  --sender=112 --reciever=108 --pcap_file from112 & 
python3 parse.py  --sender=108 --reciever=112 --pcap_file to112 & 
