import pandas as pd
import pprint
import os
from pathlib import Path
from functions.ParseExecel import FindCard
from functions.DefineCard import DefineCard
from functions.SortEquipment import SortEquipment
from functions.ExtractXML import ExtractRungXML
from functions.ExtractXML import CompileXML
from functions.XMLStrings import GetXMLSnippets
from functions.ParseExecel import GetMetaData


def extract_io_to_xml_imports(
    input_file: Path
) -> None:
    print('Converting to XML please wait...')
    # Determine the root directory of the project
    project_root = os.path.dirname(os.path.abspath(__file__))
    # Define the path to the folder where the XML Exports will be stored           ***This needs to be changed after development to /PLC/XML Export folder****
    folder_path = os.path.join(project_root, 'data/XML_to_Import')
    # Check if the folder already exists
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    # Load the CSV file
    file_path = os.path.join(project_root, 'IOSheet', input_file)
    IO_list = pd.read_excel(file_path, sheet_name='IO LIST')

    print('Reading excel sheet please wait...')
    meta_data = GetMetaData(IO_list) 
    pprint.pprint(meta_data)
    print('Extracting card data please wait...')
    IOcard_rows = FindCard(IO_list)
    print('Organizing equipment please wait (this will take a hot minute)...')
    IOCards = []
    for index in IOcard_rows:
        obj = DefineCard(IO_list, index)
        IOCards.append(obj)
    IO_Sorted_Equipment = SortEquipment(IOCards, meta_data)
    print('Creating independant XML just wait!')
    for obj in IO_Sorted_Equipment:

        xml_obj = ExtractRungXML(obj)

        if xml_obj['Digital I']['Rung XML'] or xml_obj['Analog I']['Rung XML'] or xml_obj['RTD']['Rung XML']:
            rung_xml = xml_obj['Digital I']['Rung XML']
            rung_xml += xml_obj['Analog I']['Rung XML']      
            rung_xml += xml_obj['RTD']['Rung XML']
            
            # pprint.pprint(rung_xml)
            program_tag_xml =xml_obj['Digital I']['Program Tag XML']
            program_tag_xml +=xml_obj['Analog I']['Program Tag XML']
            if xml_obj['Analog I']['Rung XML']:
                program_tag_xml += f'''<Tag Name="Service_Permission" TagType="Base" DataType="BOOL" Radix="Decimal" Constant="false" ExternalAccess="Read/Write">
                    <Description>
                    <![CDATA[In Service /
                    Out Of Service
                    Permission]]>
                    </Description>
                    <Data Format="L5K">
                    <![CDATA[0]]>
                    </Data>
                    <Data Format="Decorated">
                    <DataValue DataType="BOOL" Radix="Decimal" Value="0"/>
                    </Data>
                    </Tag> '''
            program_tag_xml +=xml_obj['RTD']['Program Tag XML']

            controller_tag_xml = xml_obj['Digital I']['Controller Tag XML']
            controller_tag_xml += xml_obj['Analog I']['Controller Tag XML']
            controller_tag_xml += xml_obj['RTD']['Controller Tag XML']

            XML_snippets = GetXMLSnippets(meta_data, "Digital I")
            file_name = obj['Equipment'] + " Input Mapping"+'.L5x'
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "w") as file:
                file.write(CompileXML(controller_tag_xml, program_tag_xml, rung_xml, XML_snippets))

        if xml_obj['Digital O']['Rung XML'] or xml_obj['Analog O']['Rung XML']:
            rung_xml = xml_obj['Digital O']['Rung XML']
            rung_xml += xml_obj['Analog O']['Rung XML']
            program_tag_xml =xml_obj['Digital O']['Program Tag XML']
            program_tag_xml +=xml_obj['Analog O']['Program Tag XML']
            controller_tag_xml = xml_obj['Digital O']['Controller Tag XML']
            controller_tag_xml += xml_obj['Analog O']['Controller Tag XML']
            XML_snippets = GetXMLSnippets(meta_data, "Digital O")
            file_name = obj['Equipment'] + " Output Mapping"+'.L5x'
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "w") as file:
                file.write(CompileXML(controller_tag_xml, program_tag_xml, rung_xml, XML_snippets))





    # if xml_obj['RTD']['Rung XML']:
    #     rung_xml = xml_obj['RTD']['Rung XML']
    #     program_tag_xml = xml_obj['RTD']['Program Tag XML']
    #     controller_tag_xml = xml_obj['RTD']['Controller Tag XML']
    #     XML_snippets = GetXMLSnippets(meta_data, "RTD")
    #     file_name = obj['Equipment'] + " RTD Mapping" + '.L5x'
    #     file_path = os.path.join(folder_path, file_name)
    #     with open(file_path, "w") as file:
    #         file.write(CompileXML(controller_tag_xml, program_tag_xml, rung_xml, XML_snippets))

    # for key, value in xml_obj.items():
    #     rung_xml = value['Rung XML']
    #     program_tag_xml = value['Program Tag XML']
    #     controller_tag_xml = value['Controller Tag XML']
    #     XML_snippets = GetXMLSnippets(meta_data, key)

    #     if rung_xml:
    #         file_name = obj['Equipment'] + " " + key + '.L5x'
    #         file_path = os.path.join(folder_path, file_name)
    #         with open(file_path, "w") as file:
    #             file.write(CompileXML(controller_tag_xml, program_tag_xml, rung_xml, XML_snippets))


# #**********************************************************************
# # Just for troubleshooting
# #**********************************************************************
# folder_path = os.path.join(project_root, 'VariableOutput')
# if not os.path.exists(folder_path):
#     os.makedirs(folder_path)
# file_name = 'SortedCard.txt'
# file_path = os.path.join(folder_path, file_name)
# with open(file_path, "w") as file:
#     pprint.pprint(IOCards, stream=file)
# file_name = 'SortedEquipment.txt'
# file_path = os.path.join(folder_path, file_name)
# with open(file_path, "w") as file:
#     pprint.pprint(IO_Sorted_Equipment, stream=file)   
