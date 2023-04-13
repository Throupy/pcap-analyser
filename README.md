# Create dependency diagram - Requires python 3.7
> py -3.7 deps.py

# Run main program - Requires python 3.10
> py -3.10 pcap_analyser.py [pcap_filename] [command]

> py -3.10 pcap_analyser.py example.pcap summarise
> 
| Protocol | Number of Packets | First timestamp | Last timestamp | Avg packet length |
|----------|-------------------|-----------------|----------------|-------------------|
| TCP | 13708 | 18:52:22.484 | 18:57:20.768 | 666.58 |
| UDP | 501 | 18:52:39.603 | 18:57:20.989 | 150.41 |
| ARP | 18 | 18:53:52.941 | 18:57:10.955 | 51.0 |
| ICMP | 34 | 18:54:19.161 | 18:56:50.385 | 149.35 |


Commands:
-   Summarise - Create summary of PCAP file including packet types / protocols, average length, first and last timestamps
-    URIs - Display all detected HTTP URIs from the PCAP file
-    Filenames - Display filenames embedded in the URIs from the URIs command output
-    Emails - Display all SMTP emails found in the PCAP file
-    Conversations - Display number of packets sent in conversations between two hosts
-    Plength - Display average packets length for each detected protocol
-    Timestamps - Display first and last timestamps for each detected protocol
-    Graph - Display a graph which plots number of packets over time
-    KML - Create a KML graph with source and destination locations for each packet
-    All - Execute all of the above commands

# Output Location
- By default all outputs are saved to pcapanalyser/outputs
- 
# Third party packages
- See requirements.txt
- `pip install -r requirements.txt`

# Notes
- pcap_analyser.py and all associated scripts MUST be run with python 3.10 as they
  make use of the Type Union operator and the Type Alias annotation which was added
  with 3.10
- pylint: disable=E0401 is commented at the start of each module
  this is due to the installed packages specified in the requirements.txt
  are not always pylint compliant.