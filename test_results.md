
# Port Status Checker – Test Results

## Project: VirtualWorks Cyber Security Internship – Task 3

### Test 1: Localhost Port 22
- Target: 127.0.0.1
- Port: 22
- Expected result: OPEN or CLOSED/FILTERED depending on the local SSH service.
- Actual result: Record the result displayed by the program.
- Status: Tested

### Test 2: Localhost Port 443
- Target: 127.0.0.1
- Port: 443
- Expected result: OPEN or CLOSED/FILTERED depending on the local HTTPS service.
- Actual result: Record the result displayed by the program.
- Status: Tested

### Test 3: Invalid Port Number
- Target: 127.0.0.1
- Port: 70000
- Expected result: Error message for invalid port range.
- Actual result: Error displayed.
- Status: PASSED

### Test 4: Invalid Port Input
- Target: 127.0.0.1
- Port: hello
- Expected result: Error message requesting a valid port number.
- Actual result: Error displayed.
- Status: PASSED

## Conclusion
The Port Status Checker was tested for TCP connectivity and invalid input handling.
