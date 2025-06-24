from AOIs.SCP_ER_AI import SCP_ER_AI
from AOIs.SCP_ER_AO import SCP_ER_AO
from AOIs.RTD import RTD
def GetXMLSnippets(meta_data, type):

    routine_name = ""
    match type:
        case "Digital I": routine_name = "R001_InputBuffer"
        case "Digital O": routine_name = "R099_OutputBuffer"
        case "Analog I": routine_name = "R001_InputBuffer"
        case "Analog O": routine_name = "R099_OutputBuffer"

    XML_snippets = {
        'Main Header': f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <RSLogix5000Content SchemaRevision="1.0" SoftwareRevision="{meta_data['Revision']}" TargetName="{routine_name}" TargetType="Routine" TargetSubType="RLL" TargetClass="Standard" ContainsContext="true" Owner="User'" ExportDate="Thu Aug 08 13:24:36 2024" ExportOptions="References NoRawData L5KData DecoratedData Context Dependencies ForceProtectedEncoding AllProjDocTrans">
        <Controller Use="Context" Name="{meta_data['Program Name']}">
        <DataTypes Use="Context">
        </DataTypes>\n""",

        'Tags Element': f'''
        <Tags Use="Context">''',

        'Tags Closing':f'''</Tags>
        ''',

        'Program Element': f'''
        <Programs Use="Context">
            <Program Use="Context" Name="New Program" Class="Standard">
            <Tags Use="Context">''',

        'Routine Element':f'''
            <Routines Use="Context">
                <Routine Use="Target" Name="{routine_name}" Type="RLL">
                <RLLContent>''',

        'Routine Closing': f'''
                </RLLContent>
                </Routine>
            </Routines>
            </Program>
        </Programs>
        </Controller>
        </RSLogix5000Content>''',

        'AOIs': {
            'SCP_ER_AI': SCP_ER_AI['AOI'],
            'SCP_ER_AO': SCP_ER_AO['AOI'],
            'RTD': RTD['AOI']
        }
    }
    return XML_snippets