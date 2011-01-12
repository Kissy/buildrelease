
def TestMiniDom():
  from xml.dom import minidom
  doc = minidom.parse("employees.xml")
  root = doc.getElementsByTagName("employees")[0]
  employees = root.getElementsByTagName("employee")
  for employee in employees:
    print (employee.toprettyxml())
    for node in employee.childNodes:
      if (node.nodeType == node.TEXT_NODE):
        print (node.nodeValue)

TestMiniDom()