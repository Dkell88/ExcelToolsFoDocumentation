SCP_ER_AO = {

'AOI': f'''\n<AddOnInstructionDefinitions Use="Context">
<AddOnInstructionDefinition Name="SCP_ER_AO" Revision="1.2" Vendor="QCA Systems" ExecutePrescan="false" ExecutePostscan="false" ExecuteEnableInFalse="false" CreatedDate="2007-02-02T20:31:08.937Z" CreatedBy="Not Available" EditedDate="2019-06-17T22:12:12.146Z" EditedBy="CleanVM-PC\CleanVM" SoftwareRevision="v31.00"
>
    <Description>
    <![CDATA[Scale w/Parameters, Divide by 0 protection
    Based on Rockwell's SCP AOI]]>
    </Description>
    <AdditionalHelpText>
    <![CDATA[Use this instruction to scale data from your analog module and bring it into the limits prescribed by the process variable or another analog module. 
    Equations used in calculating a linear relationship: 

    Scaled value = (input value - input min.) x rate + scaled minimum 
    Rate = (scaled max. - scaled min.) / (input max. - input min.) 


    ]]>
    </AdditionalHelpText>
    <Parameters>
    <Parameter Name="EnableIn" TagType="Base" DataType="BOOL" Usage="Input" Radix="Decimal" Required="false" Visible="false" ExternalAccess="Read Only">
    <Description>
    <![CDATA[Enable Input - System Defined Parameter]]>
    </Description>
    </Parameter>
    <Parameter Name="EnableOut" TagType="Base" DataType="BOOL" Usage="Output" Radix="Decimal" Required="false" Visible="false" ExternalAccess="Read Only">
    <Description>
    <![CDATA[Enable Output - System Defined Parameter]]>
    </Description>
    </Parameter>
    <Parameter Name="EU" TagType="Base" DataType="REAL" Usage="Input" Radix="Float" Required="false" Visible="true" ExternalAccess="Read/Write">
    <DefaultData Format="L5K">
    <![CDATA[0.00000000e+000]]>
    </DefaultData>
    <DefaultData Format="Decorated">
    <DataValue DataType="REAL" Radix="Float" Value="0.0"/>
    </DefaultData>
    </Parameter>
    <Parameter Name="P_ScaledMin" TagType="Base" DataType="REAL" Usage="Input" Radix="Float" Required="false" Visible="true" ExternalAccess="Read/Write">
    <DefaultData Format="L5K">
    <![CDATA[0.00000000e+000]]>
    </DefaultData>
    <DefaultData Format="Decorated">
    <DataValue DataType="REAL" Radix="Float" Value="0.0"/>
    </DefaultData>
    </Parameter>
    <Parameter Name="P_ScaledMax" TagType="Base" DataType="REAL" Usage="Input" Radix="Float" Required="false" Visible="true" ExternalAccess="Read/Write">
    <DefaultData Format="L5K">
    <![CDATA[0.00000000e+000]]>
    </DefaultData>
    <DefaultData Format="Decorated">
    <DataValue DataType="REAL" Radix="Float" Value="0.0"/>
    </DefaultData>
    </Parameter>
    <Parameter Name="Raw_Min" TagType="Base" DataType="REAL" Usage="Input" Radix="Float" Required="true" Visible="true" ExternalAccess="Read/Write">
    <DefaultData Format="L5K">
    <![CDATA[0.00000000e+000]]>
    </DefaultData>
    <DefaultData Format="Decorated">
    <DataValue DataType="REAL" Radix="Float" Value="0.0"/>
    </DefaultData>
    </Parameter>
    <Parameter Name="Raw_Max" TagType="Base" DataType="REAL" Usage="Input" Radix="Float" Required="true" Visible="true" ExternalAccess="Read/Write">
    <DefaultData Format="L5K">
    <![CDATA[0.00000000e+000]]>
    </DefaultData>
    <DefaultData Format="Decorated">
    <DataValue DataType="REAL" Radix="Float" Value="0.0"/>
    </DefaultData>
    </Parameter>
    <Parameter Name="Output" TagType="Base" DataType="REAL" Usage="Output" Radix="Float" Required="true" Visible="true" ExternalAccess="Read Only">
    <DefaultData Format="L5K">
    <![CDATA[0.00000000e+000]]>
    </DefaultData>
    <DefaultData Format="Decorated">
    <DataValue DataType="REAL" Radix="Float" Value="0.0"/>
    </DefaultData>
    </Parameter>
    <Parameter Name="ER" TagType="Base" DataType="BOOL" Usage="Output" Radix="Decimal" Required="false" Visible="true" ExternalAccess="Read Only">
    <Description>
    <![CDATA[Error Bit]]>
    </Description>
    <DefaultData Format="L5K">
    <![CDATA[0]]>
    </DefaultData>
    <DefaultData Format="Decorated">
    <DataValue DataType="BOOL" Radix="Decimal" Value="0"/>
    </DefaultData>
    </Parameter>
    </Parameters>


    <LocalTags>
    <LocalTag Name="Rate" DataType="REAL" Radix="Float" ExternalAccess="Read/Write">
    <DefaultData Format="L5K">
    <![CDATA[0.00000000e+000]]>
    </DefaultData>
    <DefaultData Format="Decorated">
    <DataValue DataType="REAL" Radix="Float" Value="0.0"/>
    </DefaultData>
    </LocalTag>
    </LocalTags>

    
    <Routines>
    <Routine Name="Logic" Type="RLL">
    <RLLContent>
    <Labels/>
    <Rung Number="0" Type="N">
    <Text>
    <![CDATA[EQU(P_ScaledMax,P_ScaledMin)OTE(ER);]]>
    </Text>
    </Rung>
    <Rung Number="1" Type="N">
    <Text>
    <![CDATA[XIO(ER)CPT(Rate,(Raw_Max-Raw_Min)/(P_ScaledMax-P_ScaledMin))CPT(Output,(EU-P_ScaledMin)*Rate+Raw_Min);]]>
    </Text>
    </Rung>
    </RLLContent>
    </Routine>
    </Routines>
</AddOnInstructionDefinition>
</AddOnInstructionDefinitions>''',

'data': f''' data'''
}