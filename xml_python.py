import xml.etree.ElementTree as ET

xml_data = """
<user>
    <id>1</id>
    <last_name>A</last_name>
    <first_name>B</first_name>
    <email>sacha-ek@gmail.com</email>
    <age>30</age>
</user>
"""

root = ET.fromstring(xml_data)
print("User ID: ", root.find('id').text)
print("User last name: ", root.find('last_name').text)
print("User first_name: ", root.find('first_name').text)
