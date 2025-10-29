import xml.etree.ElementTree as ET

tree = ET.parse('runners.xml')
root = tree.getroot()

for runner in root.findall('runner'):
    fname = runner.find('firstname').text
    lname = runner.find('lastname').text
    distance = float(runner.find('distance').text)
    time = int(runner.find('time').text)
    print(fname, lname, distance, time)
