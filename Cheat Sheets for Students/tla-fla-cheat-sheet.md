# INDUSTRIAL CONTROLS CHEAT SHEET

*A quick and dirty guide for many of the names and acronyms that are commonly encountered.*


|     Acronym         |     Full name                                             |     Quick defenition                                             |
|---------------------|-----------------------------------------------------------|------------------------------------------------------------------|
|     ICS             |     Industrial Control System                             |     General name for control systems                             |
|     SCADA           |     Supervisory Control And Data Acquisition              |     Control systems primarily for power grid systems             |
|     IED             |     Intelligent Electronic Device                         |     Typically referred to as the simplest block of an ICS        |
|     TLA             |     Three Letter Acronym                                  |     Quick notation for three-letter acronyms                     |
|     FLA             |     Four Letter Acronym                                   |     Quick notation for four-letter acronyms                      |
|     PLC             |     Programmable Logic Controller                         |     Standard process control device                              |
|     PAC             |     Programmable Automation Controller                    |     Another name for a Programmable Logic Controller             |
|     RTD             |     Resistive Thermal Device                              |     Device used for sensing and measuring temperature            |
|     TC              |     Thermo-Couple                                         |     Device used for sensing and measuring temperature            |
|     SEL-FM          |     SEL Fast-Message Protocol                             |     SEL proprietary, self-describing, SCADA protocol             |
|     MB              |     Mirrored Bits Protocol                                |     SEL proprietary, high-speed protection protocol              |
|     DNP             |     Distributed Network Protocol                          |     Industrial standard SCADA protocol                           |
|     MOD             |     Modbus                                                |     Antiquated industrial standard SCADA protocol                |
|     IEC             |     International Electrotechnical Commission             |     Industrial/Electrical standards organization                 |
|     ANSI            |     American National Standards Institute                 |     Industrial/Electrical standards organization                 |
|     ASCII           |     American Standard Code for Information Interchange    |                                                                  |
|     TCP/IP          |     Transmission Control Protocol/Internet Protocol       |     Component of the conceptual ethernet model                   |
|     EtherNet I/P    |     Ethernet Industrial Protocol                          |     Not to be confused with TCP/IP (Internet Protocol)           |
|     GOOSE           |     Generic Object-Oriented Substation Events             |     Peer-to-Peer protocol of the IEC-61850 family                |
|     RTU             |     Remote Terminal Unit                                  |     Remote I/O device                                            |
|     VFD             |     Variable Frequency Drive                              |     Speed control for an AC motor                                |
|     VSD             |     Variable Speed Drive                                  |     Another name for speed control for an AC motor               |
|     ASD             |     Adjustable Speed Drive                                |     Another name for speed control for an AC motor               |
|     MMS             |     Manufacturing Message Specification                   |     SCADA protocol of the IEC-61850 family                       |
|     SV              |     Sampled Values                                        |     Analog measurement protocol of the IEC-61850 family          |
|     CFC             |     Continuous Function Chart                             |     A block style of logic implementation in IEC-61131           |
|     LD              |     Ladder Diagram                                        |     A contact style of logic implementation in IEC-61131         |
|     ST              |     Structured Text                                       |     A code style of logic implementation in IEC-61131            |
|     hmi             |     Human Machine Interface                               |     Visual monitoring and control interface                      |
|     db9             |     N/A                                                   |     D-sub 9-pin serial connector (shaped like a D)               |
|     rj45            |     N/A                                                   |     Standard ethernet connector                                  |
|     Com-Proc        |     Communications Processor                              |     An IED that processes and aggregates communication           |
|     RTAC            |     Real Time Automation Controller                       |     SEL proprietary com-proc and logic controller                |
|     TCP             |     Transmission Control Protocol                         |     Reliable, but verbose, method of ethernet comms              |
|     UDP             |     User Datagram Protocol                                |     Simple, but error prone, method of ethernet comms            |
|     OSI             |     Open System Interconnection                           |     International standard model for comms among IEDs            |
|     HTTP(s)         |     Hyper-Text Transfer Protocol (Secured)                |     Common format for web-based data exchange                    |
|     SSH             |     Secure Shell                                          |     Encrypted protocol intended for Unix terminal access         |
|     RX              |     Receive/Receiver                                      |     Channel for accepting data input                             |
|     TX              |     Transmit/Transmitter                                  |     Channel for providing data output                            |
|     Base-t          |     N/A                                                   |     Copper Ethernet Port (RJ45 connector)                        |
|     base-fx         |     N/A                                                   |     Fiber Ethernet Port (commonly LC connector)                  |
|     PTP             |     Precise Time Protocol                                 |     High-accuracy ethernet-based time protocol                   |
|     SNTP            |     Simple Network Time Protocol                          |     Moderate-accuracy ethernet-based time protocol               |
|     SNMP            |     Simple Network Management Protocol                    |     Ethernet control device management protocol                  |
|     STP             |     Spanning Tree Protocol                                |     Ethernet failover management protocol                        |
|     RSTP            |     Rapid Spanning Tree Protocol                          |     Medium speed Ethernet failover management protocol           |
|     IRIG-B          |     Inter-Range Instrument Group version B                |     Serial/Coaxial-Based time distribution protocol              |
|     SMTP            |     Simple Mail Transfer Protocol                         |     Email transfer protocol                                      |
|     PRP             |     Parallel Redundancy Protocol                          |     Ethernet redundancy and failover method                      |
|     FTP             |     File Transfer Protocol                                |     Ethernet-based file transfer protocol                        |
|     SFTP            |     Secure File Transfer Protocol                         |     Secured ethernet-based file transfer protocol                |
|     DFR             |     Digital Fault Recorder                                |     Digital system for recording fault data                      |
|     DDR             |     Digital Disturbance Recorder                          |     Digital system for trending disturbance data                 |
|     SOE/SER         |     Sequence Of Events/Sequential Event Recorder          |     Sequential state change recorder                             |
|     RAS             |     Remedial Action Scheme                                |     Advanced Protection System                                   |
|     POTT            |     Permissive Overreach Transfer Trip                    |     Communication Assisted Tripping Protection Scheme            |
|     DTT             |     Direct Transfer Trip                                  |     Communication Assisted Tripping Protection Scheme            |
|     PT/VT           |     Potential/Voltage Transformer                         |     Transformer to reduce voltage to measurable range            |
|     CT              |     Current Transformer                                   |     Transformer to reduce current to measurable range            |
|     COMTRADE        |     Common Format for Transient Data Exchange             |     IEEE standardized oscillography event recording files        |
|     CEV             |     Compressed Event Record                               |     SEL standardized oscillography event recording file          |
|     RB              |     Remote Bit                                            |     Binary/Digital point used to send controls to an IED         |
|     AI/AO           |     Analog Input/Output (respectively)                    |     IED discrete inputs and outputs used for analog data         |
|     BI/BO/DI/DO     |     Binary/Digital Input/Output (respectively)            |     IED discrete inputs and outputs used for digital data        |
|     DTE             |     Data Terminal Equipment                               |     An end instrument such as a protective relay or RTU          |
|     DCE             |     Data Communications Equipment                         |     Communications equipment and pass-through devices            |
|     PEBKac          |     Problem Exists Between Keyboard And Chair             |     The problem isn’t the computer’s fault…                      |
|     CRC             |     Cyclic Redundancy Check                               |     A simple communications verification algorithm               |
|     UTC             |     Universal Time Code                                   |     World standard time, local times are relative to this        |
|     DST             |     Daylight Savings Time (offset)                        |     Offset applied for daylight savings time (United States)     |
|     MV              |     Measured Value                                        |     IEC standard variable type for analog data points            |
|     CMV             |     Complex Measured Value                                |     IEC standard variable type for complex analog data           |
|     SPS             |     Single Point Status                                   |     IEC standard variable type for binary data points            |
|     DPS             |     Double Point Status                                   |     IEC standard variable type for physical contact states       |
|     EA              |     Engineering Access                                    |     Description for remote configuration communications          |
|     MSB             |     Most Significant Bit/Byte                             |     Most-significant bit/byte leads in protocol transmission     |
|     LSB             |     Least Significant Bit/Byte                            |     Least-significant bit/byte leads in protocol transmission    |
|     ARP             |     Address Resolution Protocol                           |     Used to resolve MAC addresses for Ethernet switching         |
|     FLISR           |     Fault Location, Isolation, and Service Restoration    |     Automated control for distributed fault management           |
|     ADMS            |     Advanced Distribution Management System               |     Automated control for distribution systems                   |
|     DER             |     Distributed Energy Resource                           |     Small (relative) energy generation connected to distribution |
|     DG              |     Distributed Generation                                |     Distributed generation resource(s)                           |
|     BMS             |     Battery Management/Monitoring System                  |     A system for managing or monitoring battery(ies)             |
|     PCS             |     Power Control System                                  |     A system for controlling the power of an industrial site     |
|     PCC             |     Power of Common Coupling                              |     The metered interconnection point for DER/renewable sites    |