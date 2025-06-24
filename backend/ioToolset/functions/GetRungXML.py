def getRungXML(card_type, rack_slot, channel_num, tag_description, limits, UDT):

    match card_type:
        case "DI":
            if UDT:
                tag_description = tag_description.replace('_', '.I.')
            return f'''
                 <Text>
                <![CDATA[XIC(I_{rack_slot}.{channel_num})OTE({tag_description});]]>
                </Text>
            '''

        case "DO":
           if UDT:
                tag_description = tag_description.replace('_', '.O.')
           return f'''
                <Text>
                <![CDATA[XIC({tag_description})OTE(O_{rack_slot}.{channel_num});]]>
                </Text>
            '''
            
        case "AI":
            return  f'''
                <Text>
                <![CDATA[SCP_ER_AI({tag_description},AI_{rack_slot}CH[{channel_num}],{limits['EU Min']},{limits['EU Max']},1,Service_Permission);]]>
                </Text>'''
            
        case "AO":
           return  f'''
                <Text>
                <![CDATA[SCP_ER_AO({tag_description},4,20,{limits['EU Min']},{limits['EU Max']},O_{rack_slot}.{channel_num});]]>
                </Text> '''
            
        case "RTD":
            return  f'''<Text>
                <![CDATA[RTD({tag_description},I_{rack_slot}.{channel_num},0,3654,{limits['EU Min']},{limits['EU Max']});]]>
                </Text>'''
            
        case _:
            return" Error No Card Type Found "
            