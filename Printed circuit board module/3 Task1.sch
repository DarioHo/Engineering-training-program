EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "Simple LED circuit"
Date "2021-07-03"
Rev "1"
Comp "The University of Hong Kong"
Comment1 "Drawn by: Ho Man Tik"
Comment2 "Student ID: 3035745477"
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Device:Battery BT1
U 1 1 60E072E0
P 6300 3900
F 0 "BT1" H 6408 3946 50  0000 L CNN
F 1 "103(CR2032)" H 6408 3855 50  0000 L CNN
F 2 "SimpleLED:BatteryHolder_Keystone_103_1x20mm" V 6300 3960 50  0001 C CNN
F 3 "~" V 6300 3960 50  0001 C CNN
	1    6300 3900
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_Push SW1
U 1 1 60E0EF37
P 5300 3900
F 0 "SW1" V 5350 4250 50  0000 R CNN
F 1 "SW_Push" V 5200 4300 50  0000 R CNN
F 2 "Button_Switch_SMD:SW_SPST_CK_RS282G05A3" H 5300 4100 50  0001 C CNN
F 3 "~" H 5300 4100 50  0001 C CNN
	1    5300 3900
	0    -1   -1   0   
$EndComp
$Comp
L Device:R R1
U 1 1 60E10281
P 5800 3400
F 0 "R1" V 5700 3300 50  0000 C CNN
F 1 "300R" V 5700 3500 50  0000 C CNN
F 2 "Resistor_SMD:R_1206_3216Metric" V 5730 3400 50  0001 C CNN
F 3 "~" H 5800 3400 50  0001 C CNN
	1    5800 3400
	0    1    1    0   
$EndComp
$Comp
L Device:LED D1
U 1 1 60E10E4E
P 5850 4400
F 0 "D1" H 6000 4500 50  0000 C CNN
F 1 "RED" H 5800 4500 50  0000 C CNN
F 2 "LED_SMD:LED_1210_3225Metric" H 5850 4400 50  0001 C CNN
F 3 "~" H 5850 4400 50  0001 C CNN
	1    5850 4400
	-1   0    0    1   
$EndComp
Wire Wire Line
	5950 3400 6300 3400
Wire Wire Line
	6300 3400 6300 3700
Wire Wire Line
	6300 4100 6300 4400
Wire Wire Line
	6300 4400 6000 4400
Wire Wire Line
	5700 4400 5300 4400
Wire Wire Line
	5300 4400 5300 4100
Wire Wire Line
	5300 3700 5300 3400
Wire Wire Line
	5300 3400 5650 3400
$Comp
L Mechanical:MountingHole H1
U 1 1 60E07DCA
P 5850 5050
F 0 "H1" H 5950 5096 50  0000 L CNN
F 1 "MountingHole" H 5950 5005 50  0000 L CNN
F 2 "MountingHole:MountingHole_4mm" H 5850 5050 50  0001 C CNN
F 3 "~" H 5850 5050 50  0001 C CNN
	1    5850 5050
	1    0    0    -1  
$EndComp
$EndSCHEMATC
