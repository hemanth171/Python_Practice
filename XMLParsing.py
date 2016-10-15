import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Hemanth</name>
    <phone type="intl">9566064578</phone>
    <email hide="yes" />
</person>'''

tree = ET.fromstring(data)
print tree.find('name').text
print tree.find('email').get('hide')
print tree.find('phone').get('type')
print tree.find('phone').text