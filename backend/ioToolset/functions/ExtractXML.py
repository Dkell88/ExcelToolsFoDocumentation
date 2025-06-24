import copy
import datetime
def SetCommentRungXML(obj,idx):

    return f'''
            <Rung Number="{idx}" Type="N">
                <Comment>
                <![CDATA[********************************
                Rack: {obj['Rack number']} Slot:{obj['Slot']} Card: {obj['Card name']}
                Located: {obj['Panel Name']}
                ********************************]]>
                </Comment>
                <Text>
                <![CDATA[ nop();]]>
                </Text>
            </Rung>\n'''

def ExtractRungXML(obj):
    xml_obj = {
        'Rung XML': "",
        'Controller Tag XML': "",
        'Program Tag XML': ""
    }

    xml_out = {
        'Digital I': copy.deepcopy(xml_obj), 
        'Digital O': copy.deepcopy(xml_obj),
        'Analog I': copy.deepcopy(xml_obj),
        'Analog O': copy.deepcopy(xml_obj),
        'RTD': copy.deepcopy(xml_obj)
    }

    obj['IO point'].sort(key=lambda x: x['Card type'], reverse=True)

    previous_slot = None
    previous_rack = None
    di_idx = 0
    do_idx = 0

    # Create a mapping of tag keys to their corresponding IO point types
    tag_key_mapping = {}
    for io_point in obj['IO point']:
        io_point_tag = f"{io_point['Rack number']}{io_point['Slot']}"
        tag_key = f"I_{io_point_tag}" if io_point['Card type'] in {'RTD', 'DI', 'AI'} else f"O_{io_point_tag}"
        tag_key_mapping[tag_key] = io_point['Card type']

    # Generate Controller Tag XML for the entire object
    if 'Controller Tag XML' in obj:
        for tag_key, tag_xml in obj['Controller Tag XML'].items():
            if tag_key in tag_key_mapping:
                io_type = tag_key_mapping[tag_key]
                if io_type == 'DI':
                    xml_out['Digital I']['Controller Tag XML'] += tag_xml
                elif io_type == 'DO':
                    xml_out['Digital O']['Controller Tag XML'] += tag_xml
                elif io_type == 'AI':
                    xml_out['Analog I']['Controller Tag XML'] += tag_xml
                elif io_type == 'AO':
                    xml_out['Analog O']['Controller Tag XML'] += tag_xml
                elif io_type == 'RTD':
                    xml_out['RTD']['Controller Tag XML'] += tag_xml

    for io_point in obj['IO point']:
        match io_point['Card type']:
            case "DI":
                if previous_slot is None or (previous_slot is not None and (io_point['Slot'] != previous_slot or io_point['Rack number'] != previous_rack)):
                    xml_out['Digital I']['Rung XML'] += SetCommentRungXML(io_point,di_idx)
                    di_idx += 1
                xml_out['Digital I']['Rung XML'] += f'''\t\t\t<Rung Number="{di_idx}" Type="N">{io_point['Rung XML']}</Rung>\n'''
                if 'Program Tag XML' in io_point and io_point['Program Tag XML']:
                    xml_out['Digital I']['Program Tag XML'] += io_point['Program Tag XML']  
                di_idx += 1
            
            case "DO":
                if previous_slot is None or (previous_slot is not None and (io_point['Slot'] != previous_slot or io_point['Rack number'] != previous_rack)):
                    xml_out['Digital O']['Rung XML'] += SetCommentRungXML(io_point,do_idx)
                    do_idx += 1
                xml_out['Digital O']['Rung XML'] += f'''\t\t\t<Rung Number="{do_idx}" Type="N">{io_point['Rung XML']}</Rung>\n'''
                if 'Program Tag XML' in io_point and io_point['Program Tag XML']:
                    xml_out['Digital O']['Program Tag XML'] += io_point['Program Tag XML']
                do_idx += 1
            
            case "AI":
                if previous_slot is None or (previous_slot is not None and (io_point['Slot'] != previous_slot or io_point['Rack number'] != previous_rack)):
                    xml_out['Analog I']['Rung XML'] += SetCommentRungXML(io_point,di_idx)
                    di_idx += 1
                xml_out['Analog I']['Rung XML'] += f'''\t\t\t<Rung Number="{di_idx}" Type="N">{io_point['Rung XML']}</Rung>\n'''
                if 'Program Tag XML' in io_point and io_point['Program Tag XML']:
                    xml_out['Analog I']['Program Tag XML'] += io_point['Program Tag XML']
                di_idx += 1
            
            case "AO":
                if previous_slot is None or (previous_slot is not None and (io_point['Slot'] != previous_slot or io_point['Rack number'] != previous_rack)):
                    xml_out['Analog O']['Rung XML'] += SetCommentRungXML(io_point,do_idx)
                    do_idx += 1
                xml_out['Analog O']['Rung XML'] += f'''\t\t\t<Rung Number="{do_idx}" Type="N">{io_point['Rung XML']}</Rung>\n'''
                if 'Program Tag XML' in io_point and io_point['Program Tag XML']:
                    xml_out['Analog O']['Program Tag XML'] += io_point['Program Tag XML']
                do_idx += 1

            case "RTD":
                if previous_slot is None or (previous_slot is not None and (io_point['Slot'] != previous_slot or io_point['Rack number'] != previous_rack)):
                    xml_out['RTD']['Rung XML'] += SetCommentRungXML(io_point, di_idx)
                    di_idx += 1
                xml_out['RTD']['Rung XML'] += f'''\t\t\t<Rung Number="{di_idx}" Type="N">{io_point['Rung XML']}</Rung>\n'''
                if 'Program Tag XML' in io_point and io_point['Program Tag XML']:
                    xml_out['RTD']['Program Tag XML'] += io_point['Program Tag XML']
                di_idx += 1

        previous_slot = io_point['Slot']
        previous_rack = io_point['Rack number']

    return xml_out

def CompileXML(controller_tag_xml, program_tag_xml, rung_xml,XML_snippets):

    xml_content = XML_snippets['Main Header']
    if  'SCP_ER_AI' in rung_xml:
        xml_content += XML_snippets['AOIs']['SCP_ER_AI']
    if  'SCP_ER_AO' in rung_xml:
        xml_content += XML_snippets['AOIs']['SCP_ER_AO']
    if  'RTD' in rung_xml:
        xml_content += XML_snippets['AOIs']['RTD']
    xml_content += XML_snippets['Tags Element']
    xml_content += controller_tag_xml
    xml_content += XML_snippets['Tags Closing']
    xml_content += XML_snippets['Program Element']
    xml_content += program_tag_xml
    xml_content += XML_snippets['Tags Closing']
    xml_content += XML_snippets['Routine Element']
    xml_content += rung_xml
    xml_content += XML_snippets['Routine Closing']

    return xml_content



# def ExtractRungXML(obj):
#     xml_obj = {
#         'Rung XML': "",
#         'Controller Tag XML': "",
#         'Program Tag XML': ""
#     }

#     xml_out = {
#         'Digital I': copy.deepcopy(xml_obj), 
#         'Digital O': copy.deepcopy( xml_obj),
#         'Analog I': copy.deepcopy(xml_obj),
#         'Analog O': copy.deepcopy(xml_obj)
#     }

    # obj['IO point'].sort(key=lambda x: x['Card type'], reverse=True)

    # # xml_out['Digital I']['Rung XML'] = f'''
    # # Input Buffering for {obj['Equipment']}
    # # -----------------------------------------------------------------------
    # # Mapping ot Digital and Analog Inputs
    # # Output from Logix Tools
    # # -----------------------------------------------------------------------
    # # Ver: 0.0
    # # Date: {datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}'''

    # previous_slot = None
    # previous_rack = None
    # di_idx = 0
    # do_idx = 0

    # for io_point in obj['IO point']:
    
    #     match io_point['Card type']:
    #         case "DI":
    #             if previous_slot is None or (previous_slot is not None and (io_point['Slot'] != previous_slot or io_point['Rack number'] != previous_rack)):
    #                 xml_out['Digital I']['Rung XML'] += SetCommentRungXML(io_point,di_idx)
    #                 di_idx += 1
    #             xml_out['Digital I']['Rung XML'] += f'''\t\t\t<Rung Number="{di_idx}" Type="N">{io_point['Rung XML']}</Rung>\n'''
    #             xml_out['Digital I']['Controller Tag XML'] += io_point['Controller Tag XML']
    #             if 'Program Tag XML' in io_point and io_point['Program Tag XML']:
    #                 xml_out['Digital I']['Program Tag XML'] += io_point['Program Tag XML']  
    #             di_idx += 1
                 
    #         case "DO":
    #             if previous_slot is None or (previous_slot is not None and (io_point['Slot'] != previous_slot or io_point['Rack number'] != previous_rack)):
    #                 xml_out['Digital O']['Rung XML'] += SetCommentRungXML(io_point,do_idx)
    #                 do_idx += 1
    #             xml_out['Digital O']['Rung XML'] += f'''\t\t\t<Rung Number="{do_idx}" Type="N">{io_point['Rung XML']}</Rung>\n'''
    #             xml_out['Digital O']['Controller Tag XML'] += io_point['Controller Tag XML']
    #             if 'Program Tag XML' in io_point and io_point['Program Tag XML']:
    #                 xml_out['Digital O']['Program Tag XML'] += io_point['Program Tag XML']
    #             do_idx += 1
                
    #         case "AI":
    #             if previous_slot is None or (previous_slot is not None and (io_point['Slot'] != previous_slot or io_point['Rack number'] != previous_rack)):
    #                 xml_out['Analog I']['Rung XML'] += SetCommentRungXML(io_point,di_idx)
    #                 di_idx += 1
    #             xml_out['Analog I']['Rung XML'] += f'''\t\t\t<Rung Number="{di_idx}" Type="N">{io_point['Rung XML']}</Rung>\n'''
    #             xml_out['Analog I']['Controller Tag XML'] += io_point['Controller Tag XML']
    #             if 'Program Tag XML' in io_point and io_point['Program Tag XML']:
    #                 xml_out['Analog I']['Program Tag XML'] += io_point['Program Tag XML']
    #             di_idx += 1
                
    #         case "AO":
    #             if previous_slot is None or (previous_slot is not None and (io_point['Slot'] != previous_slot or io_point['Rack number'] != previous_rack)):
    #                 xml_out['Analog O']['Rung XML'] += SetCommentRungXML(io_point,do_idx)
    #                 do_idx += 1
    #             xml_out['Analog O']['Rung XML'] += f'''\t\t\t<Rung Number="{do_idx}" Type="N">{io_point['Rung XML']}</Rung>\n'''
    #             xml_out['Analog O']['Controller Tag XML'] += io_point['Controller Tag XML']
    #             if 'Program Tag XML' in io_point and io_point['Program Tag XML']:
    #                 xml_out['Analog O']['Program Tag XML'] += io_point['Program Tag XML']
    #             do_idx += 1

    #     previous_slot = io_point['Slot']
    #     previous_rack = io_point['Rack number']

    # return xml_out
