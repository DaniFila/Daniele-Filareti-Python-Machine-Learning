import xml.etree.ElementTree as ET
import pandas as pd

# dataframe = pd.DataFrame(dati,index,columns)

xml = """<data>
<student name="John">
<email>john@mail.com</email>
<grade>A</grade>
<age>16</age>
</student>
<student name="Alice">
<email>alice@mail.com</email>
<grade>B</grade>
<age>17</age>
</student>
<student name="Bob">
<email>bob@mail.com</email>
<grade>C</grade>
<age>16</age>
</student>
<student name="Hannah">
<email>hannah@mail.com</email>
<grade>A</grade>
<age>17</age>
</student>
</data>
"""

root = ET.fromstring(xml)

df_col = ["nome", "email", "grado", "età"]

righe = []

for nodo in root:
    nome = nodo.attrib["name"]
    mail = nodo.find("email").text if nodo is not None else None
    grado = nodo.find("grade").text if nodo is not None else None
    età = nodo.find("age").text if nodo is not None else None

    righe.append({"nome":nome, "email":mail, "grado":grado, "età":età})

#print(righe)

df = pd.DataFrame(righe, columns=df_col)

print(df)