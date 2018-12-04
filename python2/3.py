from xml.dom.minidom import getDOMImplementation

with open('example.xml', 'r') as PlikXml:
    with open('powrocik.xml', 'w') as doZapisu:
        for line in PlikXml:
            impl = getDOMImplementation()

            new = impl.createDocument(None, "tag", None)
            top_element = new.documentElement
            text = new.createTextNode('Cos.')
            top_element.appendChild(text)