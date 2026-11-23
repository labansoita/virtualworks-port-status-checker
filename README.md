
# Port Status Checker

## VirtualWorks Cyber Security Internship – Task 3

### Project Description
The Port Status Checker is a Python-based network utility that checks whether a TCP port on a specified host is open or closed/filtered.

It uses Python's built-in socket library to attempt a TCP connection and report the result.

### Features
- Accepts an IP address or hostname.
- Accepts a port number between 1 and 65535.
- Checks TCP port availability.
- Identifies open and unsuccessful connections.
- Handles invalid port numbers.
- Handles invalid user input.
- Handles hostname resolution errors.
- Uses a 3-second connection timeout.

### Technologies Used
- Python 3
- Socket library
- Kali Linux

### How to Run

1. Clone the repository.
2. Open the project directory.
3. Run the following command:

```bash
python3 port_checker.py
```

4. Enter the target IP address or hostname.
5. Enter the port number.

### Example

Target IP: 127.0.0.1  
Port: 22

Possible output:

PORT 22: OPEN

### Security and Ethical Use
Use this tool only on systems you own or have explicit permission to test.

### Author
Laban Soita

VirtualWorks Cyber Security Internship
