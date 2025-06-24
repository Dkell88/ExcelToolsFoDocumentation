import pandas as pd
import pprint
from Functions.GetRungXML import getRungXML

def SortByEquipment(objects_array):
    """
    Function to reorganize the array of objects into a new structure based on 'Equipment',
    ignoring any elements where the 'Equipment' variable is blank or NaN.
    
    Parameters:
    objects_array (list): The original array of objects.
    
    Returns:
    List[dict]: A new array of objects reorganized by 'Equipment'.
    """
    equipment_dict = {}
    stored_controller_tags = []

    # Loop through each object in the original array
    for obj in objects_array:
        rack_num = obj['Rack Number']
        card_name = obj['Card Name']
        card_type = obj['Cardtype']
        slot = obj['Slot']
        panel_name = obj['Panel Name']
        # pprint.pprint(obj)
        # Loop through each IO point in the current object's 'IO Points' array
        for io_point in obj['IO Points']:
            equipment = io_point['Equipment']
            number_value = int(io_point['Number Value'])
            tag_description_temp = io_point['Tag Description']
            tag_description = tag_description_temp.replace('-', '_')
            comment = str(io_point['Comment'])
            comment += f''' - {str(io_point['Tag Description'])}'''

            # Ignore if equipment is blank or NaN
            if pd.isna(equipment) or equipment == "":
                continue

            # If the equipment is not yet in the dictionary, add it
            if equipment not in equipment_dict:
                equipment_dict[equipment] = {
                    'Equipment': equipment,
                    'IO point': []
                }

            point_card_tag = f"{rack_num}{slot}"   #I_1808.0
            point_tag = f"{point_card_tag}.{number_value}"   #I_1808.0

            rung_xml = getRungXML(card_type, point_card_tag, number_value, tag_description,io_point['Limits'])

            program_tag_xml = f'''        
        <Tag Name="{tag_description}" TagType="Base" DataType="BOOL" Radix="Decimal" Constant="false" ExternalAccess="Read/Write">
            <Description>
            <![CDATA[{comment}]]>
            </Description>
            <Data Format="L5K">
            <![CDATA[0]]>
            </Data>
            <Data Format="Decorated">
            <DataValue DataType="BOOL" Radix="Decimal" Value="0"/>
            </Data>
        </Tag>
            '''

            if point_card_tag not in stored_controller_tags: 
                match card_type:
                    case 'RTD': point_card_tag = f'''RTD_{point_card_tag}'''
                    case 'DI': point_card_tag = f'''I_{point_card_tag}'''
                    case 'DO': point_card_tag = f'''O_{point_card_tag}'''
                    case 'AI': point_card_tag = f'''I_{point_card_tag}'''
                    case 'AO': point_card_tag = f'''O_{point_card_tag}'''

                controller_tag_xml = f'''
    <Tag Name="{point_card_tag}" Class="Standard" TagType="Base" DataType="DINT" Radix="Decimal" Constant="false" ExternalAccess="Read/Write">
        <Data Format="L5K">
        <![CDATA[0]]>
        </Data>
        <Data Format="Decorated">
        <DataValue DataType="DINT" Radix="Decimal" Value="0"/>
        </Data>
    </Tag>
'''   
                stored_controller_tags.append(point_card_tag)
            else:
                controller_tag_xml = ""
            
            # Create the new IO point object
            io_point_obj = {
                'Number value': number_value,
                'Tag description': tag_description,
                'Rack number': rack_num,
                'Card name': card_name,
                'Card type': card_type,
                'Rung XML': rung_xml,
                'Controller Tag XML': controller_tag_xml,
                'Program Tag XML': program_tag_xml,
                'Comment': comment,
                'Slot': slot,
                'Panel Name': panel_name,
                'Limits': io_point['Limits']
            }
            
            # Append the IO point object to the correct equipment entry
            equipment_dict[equipment]['IO point'].append(io_point_obj)

    # Convert the dictionary to a list of objects
    new_objects_array = list(equipment_dict.values())

    return new_objects_array

