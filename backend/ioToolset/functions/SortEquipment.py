import pandas as pd
from Functions.GetRungXML import getRungXML
import pprint
import os
from AOIs.SCP_ER_AI import SCP_ER_AI
from AOIs.SCP_ER_AO import SCP_ER_AO
from AOIs.RTD import RTD

def SortEquipment(objects_array, meta_data):
    """
    Reorganizes an array of objects into a new structure based on 'Equipment', grouping comments 
    for each tag under the same Tag Name.

    Parameters:
    objects_array (list): The original array of objects. Each object must contain 'Rack Number', 
    'Card Name', 'Cardtype', 'Slot', 'Panel Name', and 'IO Points' where 'IO Points' is a list of 
    dictionaries with keys: 'Equipment', 'Number Value', 'Tag Description', 'Comment', and 'Limits'.

    Returns:
    List[dict]: A new array of objects reorganized by 'Equipment' with associated IO points.
    """
    equipment_dict = {}
    tag_data_dict = {}

    # Process each object
    for obj in objects_array:
        try:
            rack_num = obj['Rack Number']
            card_name = obj['Card Name']
            card_type = obj['Cardtype']
            slot = obj['Slot']
            panel_name = obj['Panel Name']
            num_channels = obj['Number of channels']
            
            for io_point in obj.get('IO Points', []):
                equipment = io_point.get('Equipment', '')
                number_value = int(io_point.get('Number Value', 0))
                tag_description_temp = io_point.get('Tag Description', '')
                tag_description = tag_description_temp.replace('-', '_')
                tag_description = tag_description.replace(f"{meta_data['Program Name']}_", '')
                comment = str(io_point.get('Comment', ''))
                comment += f' - {tag_description_temp}'

                if pd.isna(equipment) or equipment == "":
                    continue

                point_card_tag = f"{rack_num}{slot}"

                rung_xml = getRungXML(card_type, point_card_tag, number_value, tag_description, io_point.get('Limits', ''), meta_data['UDT'])
                point_card_tag = f"I_{point_card_tag}" if card_type in {'RTD', 'DI', 'AI'} else f"O_{point_card_tag}"

                if point_card_tag not in tag_data_dict:
                    tag_data_dict[point_card_tag] = {
                        'Tag Name': point_card_tag,
                        'Comments': [],
                        'DataType': 'DINT',
                        'DataValue': 0
                    } if card_type in {'DI', 'DO'} else {
                        'Tag Name': f'''A{point_card_tag}CH''',
                        'Comments': [],
                        'DataType': 'REAL',
                        'DataValue': ', '.join(['0'] * num_channels)  #This needs to be changed to be dymanic based on the number of channels
                    }

                # Check if the comment already exists
                if not any(c['Comment'] == comment for c in tag_data_dict[point_card_tag]['Comments']):
                    tag_data_dict[point_card_tag]['Comments'].append({
                        'Operand': f".{number_value}" if card_type in {'DI', 'DO'} else f"[{number_value}]",
                        'Comment': comment
                    })
                #pprint.pprint(tag_data_dict)
                dataType = f"SCP_ER_AI" if card_type in {'RTD', 'AI'} else f'''BOOL" Radix="Decimal'''

                dataFormat = f'''{SCP_ER_AI['data']}''' if card_type in {'RTD', 'AI'} else f'''
                <Data Format="L5K">
                <![CDATA[0]]>
                </Data>
                <Data Format="Decorated"> 
                <DataValue DataType="{dataType}" Value="0"/>'''

                program_tag_xml = f'''        
                <Tag Name="{tag_description}" TagType="Base" DataType="{dataType}" Constant="false" ExternalAccess="Read/Write">
                <Description>
                <![CDATA[{comment}]]>
                </Description>
                {dataFormat}
                </Data>
                </Tag>
                '''

                io_point_obj = {
                    'Number value': number_value,
                    'Tag description': tag_description,
                    'Rack number': rack_num,
                    'Card name': card_name,
                    'Card type': card_type,
                    'Program Tag XML': program_tag_xml,
                    'Comment': comment,
                    'Slot': slot,
                    'Panel Name': panel_name,
                    'Rung XML': rung_xml,
                    'Limits': io_point.get('Limits', '')
                }
                
                if equipment not in equipment_dict:
                    equipment_dict[equipment] = {
                        'Equipment': equipment,
                        'IO point': []
                    }
                
                # Check if the IO point already exists
                if not any(p['Number value'] == number_value and p['Tag description'] == tag_description for p in equipment_dict[equipment]['IO point']):
                    equipment_dict[equipment]['IO point'].append(io_point_obj)

                output_folder = 'VariableOutput'
                os.makedirs(output_folder, exist_ok=True)
                output_file_path = os.path.join(output_folder, 'EquipemntDic_bf_controllerTag_output.txt')
                with open(output_file_path, 'w') as file:
                    pprint.pprint(equipment_dict, stream=file)

        except KeyError as e:
            print(f"Key error: {e} in object {obj}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    # Generate the XML for each unique tag (Controller Tag XML)
    tag_xml_dict = {}
    for tag, tag_data in tag_data_dict.items():
        comments_xml = "".join(f'''
        <Comment Operand="{comment['Operand']}">
        <![CDATA[{comment['Comment']}]]>
        </Comment>''' for comment in tag_data['Comments'])
        # pprint.pprint(tag_data)
        if tag_data['DataType'] == 'DINT': 
            controller_tag_xml = f'''
            <Tag Name="{tag_data['Tag Name']}" Class="Standard" TagType="Base" DataType="{tag_data['DataType']}" Radix="Decimal" Constant="false" ExternalAccess="Read/Write">
                <Comments>
                    {comments_xml}
                </Comments>
                <Data Format="L5K">
                <![CDATA[{tag_data['DataValue']}]]>
                </Data>
                <Data Format="Decorated">
                <DataValue DataType="{tag_data['DataType']}" Radix="Decimal" Value="{tag_data['DataValue']}"/>
                </Data>
            </Tag>
        ''' 
        else: 
            elements_str = "\n    ".join(f'<Element Index="[{i}]" Value="0"/>' for i in range(num_channels))
            controller_tag_xml =f'''<Tag Name="{tag_data['Tag Name']}" TagType="Base" DataType="{tag_data['DataType']}" Dimensions="{num_channels}" Radix="Float" Constant="false" ExternalAccess="Read/Write">
                <Comments>
                    {comments_xml}
                </Comments>
                <Data Format="L5K">
                <![CDATA[[{tag_data['DataValue']}]]]>
                </Data>
                <Data Format="Decorated">
                    <Array DataType="REAL" Dimensions="{num_channels}" Radix="Float">
                    {elements_str}
                    </Array>
                </Data>
            </Tag>
            '''

        tag_xml_dict[tag] = controller_tag_xml
        # equipment_name = tag_data['Equipment']

        # if equipment_name in equipment_dict:
        #     equipment_dict[equipment_name]['ControllerTags'][tag] = controller_tag_xml
        # else:
        # # If the equipment is not found, you may want to handle this case, e.g., create a new equipment entry
        #     equipment_dict[equipment_name] = {'ControllerTags': {tag: controller_tag_xml}, 'IOPoints': {}}
    # Assign Controller Tag XML to each IO point based on its tag, only if it hasn't been assigned yet
    # for equipment_obj in equipment_dict.values():
    #     for io_point in equipment_obj['IO point']:
    #         if 'Controller Tag XML' not in io_point:
    #             io_point_tag = f"{io_point['Rack number']}{io_point['Slot']}"
    #             tag_key = f"I_{io_point_tag}" if io_point['Card type'] in {'RTD', 'DI', 'AI'} else f"O_{io_point_tag}"
    #             if tag_key in tag_xml_dict:
    #                 io_point['Controller Tag XML'] = tag_xml_dict[tag_key]

    for equipment_obj in equipment_dict.values():
        io_point_tag = ""
        for io_point in equipment_obj['IO point']:
            io_point_tag = f"{io_point['Rack number']}{io_point['Slot']}"
            tag_key = f"I_{io_point_tag}" if io_point['Card type'] in {'RTD', 'DI', 'AI'} else f"O_{io_point_tag}"
            if tag_key in tag_data_dict:
                if 'Controller Tag XML' not in equipment_obj:
                    equipment_obj['Controller Tag XML'] = {}
                equipment_obj['Controller Tag XML'][tag_key] = tag_xml_dict[tag_key]

    output_folder = 'VariableOutput'
    os.makedirs(output_folder, exist_ok=True)
    output_file_path = os.path.join(output_folder, 'EquipemntDic_af_controllerTag_output.txt')
    with open(output_file_path, 'w') as file:
        pprint.pprint(equipment_dict, stream=file)

    return list(equipment_dict.values())