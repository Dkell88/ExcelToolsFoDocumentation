SCP_ER_AI = {

'AOI': f'''\n<AddOnInstructionDefinitions Use="Context">
<AddOnInstructionDefinition Name="SCP_ER_AI" Revision="1.2" Vendor="QCA Systems" ExecutePrescan="false" ExecutePostscan="false" ExecuteEnableInFalse="false" CreatedDate="2007-02-02T20:31:08.937Z" CreatedBy="Not Available" EditedDate="2020-07-06T20:13:42.275Z" EditedBy="ROCKWELL-PT\CleanVM" SoftwareRevision="v32.02"
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
    <Parameter Name="Input" TagType="Base" DataType="REAL" Usage="Input" Radix="Float" Required="true" Visible="true" ExternalAccess="Read/Write">
    <DefaultData Format="L5K">
    <![CDATA[0.00000000e+000]]>
    </DefaultData>
    <DefaultData Format="Decorated">
    <DataValue DataType="REAL" Radix="Float" Value="0.0"/>
    </DefaultData>
    </Parameter>
    <Parameter Name="InOK" TagType="Base" DataType="BOOL" Usage="Output" Radix="Decimal" Required="false" Visible="true" ExternalAccess="Read Only">
    <Description>
    <![CDATA[Input OK]]>
    </Description>
    <DefaultData Format="L5K">
    <![CDATA[0]]>
    </DefaultData>
    <DefaultData Format="Decorated">
    <DataValue DataType="BOOL" Radix="Decimal" Value="0"/>
    </DefaultData>
    </Parameter>
    <Parameter Name="Input_Min" TagType="Base" DataType="REAL" Usage="Input" Radix="Float" Required="true" Visible="true" ExternalAccess="Read/Write">
    <Description>
    <![CDATA[Input Min]]>
    </Description>
    <DefaultData Format="L5K">
    <![CDATA[0.00000000e+000]]>
    </DefaultData>
    <DefaultData Format="Decorated">
    <DataValue DataType="REAL" Radix="Float" Value="0.0"/>
    </DefaultData>
    </Parameter>
    <Parameter Name="Input_Max" TagType="Base" DataType="REAL" Usage="Input" Radix="Float" Required="true" Visible="true" ExternalAccess="Read/Write">
    <Description>
    <![CDATA[Input Max]]>
    </Description>
    <DefaultData Format="L5K">
    <![CDATA[0.00000000e+000]]>
    </DefaultData>
    <DefaultData Format="Decorated">
    <DataValue DataType="REAL" Radix="Float" Value="0.0"/>
    </DefaultData>
    </Parameter>
    <Parameter Name="LowLow" TagType="Base" DataType="BOOL" Usage="Output" Radix="Decimal" Required="false" Visible="true" ExternalAccess="Read Only">
    <Description>
    <![CDATA[Low Low]]>
    </Description>
    <DefaultData Format="L5K">
    <![CDATA[0]]>
    </DefaultData>
    <DefaultData Format="Decorated">
    <DataValue DataType="BOOL" Radix="Decimal" Value="0"/>
    </DefaultData>
    </Parameter>
    <Parameter Name="Low" TagType="Base" DataType="BOOL" Usage="Output" Radix="Decimal" Required="false" Visible="true" ExternalAccess="Read Only">
    <Description>
    <![CDATA[Low]]>
    </Description>
    <DefaultData Format="L5K">
    <![CDATA[0]]>
    </DefaultData>
    <DefaultData Format="Decorated">
    <DataValue DataType="BOOL" Radix="Decimal" Value="0"/>
    </DefaultData>
    </Parameter>
    <Parameter Name="High" TagType="Base" DataType="BOOL" Usage="Output" Radix="Decimal" Required="false" Visible="true" ExternalAccess="Read Only">
    <Description>
    <![CDATA[High]]>
    </Description>
    <DefaultData Format="L5K">
    <![CDATA[0]]>
    </DefaultData>
    <DefaultData Format="Decorated">
    <DataValue DataType="BOOL" Radix="Decimal" Value="0"/>
    </DefaultData>
    </Parameter>
    <Parameter Name="HighHigh" TagType="Base" DataType="BOOL" Usage="Output" Radix="Decimal" Required="false" Visible="true" ExternalAccess="Read Only">
    <Description>
    <![CDATA[High High]]>
    </Description>
    <DefaultData Format="L5K">
    <![CDATA[0]]>
    </DefaultData>
    <DefaultData Format="Decorated">
    <DataValue DataType="BOOL" Radix="Decimal" Value="0"/>
    </DefaultData>
    </Parameter>
    <Parameter Name="P_ScaledMin" TagType="Base" DataType="REAL" Usage="Input" Radix="Float" Required="false" Visible="true" ExternalAccess="Read/Write">
    <Description>
    <![CDATA[Scaled Min]]>
    </Description>
    <DefaultData Format="L5K">
    <![CDATA[0.00000000e+000]]>
    </DefaultData>
    <DefaultData Format="Decorated">
    <DataValue DataType="REAL" Radix="Float" Value="0.0"/>
    </DefaultData>
    </Parameter>
    <Parameter Name="P_ScaledMax" TagType="Base" DataType="REAL" Usage="Input" Radix="Float" Required="false" Visible="true" ExternalAccess="Read/Write">
    <Description>
    <![CDATA[Scaled Max]]>
    </Description>
    <DefaultData Format="L5K">
    <![CDATA[0.00000000e+000]]>
    </DefaultData>
    <DefaultData Format="Decorated">
    <DataValue DataType="REAL" Radix="Float" Value="0.0"/>
    </DefaultData>
    </Parameter>
    <Parameter Name="P_LowLow" TagType="Base" DataType="REAL" Usage="Input" Radix="Float" Required="false" Visible="false" ExternalAccess="Read/Write">
    <Description>
    <![CDATA[Low Low Limit]]>
    </Description>
    <DefaultData Format="L5K">
    <![CDATA[0.00000000e+000]]>
    </DefaultData>
    <DefaultData Format="Decorated">
    <DataValue DataType="REAL" Radix="Float" Value="0.0"/>
    </DefaultData>
    </Parameter>
    <Parameter Name="P_Low" TagType="Base" DataType="REAL" Usage="Input" Radix="Float" Required="false" Visible="false" ExternalAccess="Read/Write">
    <Description>
    <![CDATA[Low Limit]]>
    </Description>
    <DefaultData Format="L5K">
    <![CDATA[0.00000000e+000]]>
    </DefaultData>
    <DefaultData Format="Decorated">
    <DataValue DataType="REAL" Radix="Float" Value="0.0"/>
    </DefaultData>
    </Parameter>
    <Parameter Name="P_High" TagType="Base" DataType="REAL" Usage="Input" Radix="Float" Required="false" Visible="false" ExternalAccess="Read/Write">
    <Description>
    <![CDATA[High Limit]]>
    </Description>
    <DefaultData Format="L5K">
    <![CDATA[0.00000000e+000]]>
    </DefaultData>
    <DefaultData Format="Decorated">
    <DataValue DataType="REAL" Radix="Float" Value="0.0"/>
    </DefaultData>
    </Parameter>
    <Parameter Name="P_HighHigh" TagType="Base" DataType="REAL" Usage="Input" Radix="Float" Required="false" Visible="false" ExternalAccess="Read/Write">
    <Description>
    <![CDATA[High High Limit]]>
    </Description>
    <DefaultData Format="L5K">
    <![CDATA[0.00000000e+000]]>
    </DefaultData>
    <DefaultData Format="Decorated">
    <DataValue DataType="REAL" Radix="Float" Value="0.0"/>
    </DefaultData>
    </Parameter>
    <Parameter Name="Service_Enable" TagType="Base" DataType="BOOL" Usage="Input" Radix="Decimal" Required="true" Visible="true" ExternalAccess="Read/Write">
    <Description>
    <![CDATA[In/Out of Service
    Enabled]]>
    </Description>
    <DefaultData Format="L5K">
    <![CDATA[0]]>
    </DefaultData>
    <DefaultData Format="Decorated">
    <DataValue DataType="BOOL" Radix="Decimal" Value="0"/>
    </DefaultData>
    </Parameter>
    <Parameter Name="Service_Permission" TagType="Base" DataType="BOOL" Usage="Input" Radix="Decimal" Required="true" Visible="true" ExternalAccess="Read/Write">
    <Description>
    <![CDATA[In/Out of Service Permission]]>
    </Description>
    <DefaultData Format="L5K">
    <![CDATA[0]]>
    </DefaultData>
    <DefaultData Format="Decorated">
    <DataValue DataType="BOOL" Radix="Decimal" Value="0"/>
    </DefaultData>
    </Parameter>
    <Parameter Name="HMI_I_OutOfService" TagType="Base" DataType="BOOL" Usage="Input" Radix="Decimal" Required="false" Visible="false" ExternalAccess="Read/Write">
    <Description>
    <![CDATA[HMI Out Of Service
    Command]]>
    </Description>
    <DefaultData Format="L5K">
    <![CDATA[0]]>
    </DefaultData>
    <DefaultData Format="Decorated">
    <DataValue DataType="BOOL" Radix="Decimal" Value="0"/>
    </DefaultData>
    </Parameter>
    <Parameter Name="HMI_I_InService" TagType="Base" DataType="BOOL" Usage="Input" Radix="Decimal" Required="false" Visible="false" ExternalAccess="Read/Write">
    <Description>
    <![CDATA[HMI In Service
    Command]]>
    </Description>
    <DefaultData Format="L5K">
    <![CDATA[0]]>
    </DefaultData>
    <DefaultData Format="Decorated">
    <DataValue DataType="BOOL" Radix="Decimal" Value="0"/>
    </DefaultData>
    </Parameter>
    <Parameter Name="OutOfService" TagType="Base" DataType="BOOL" Usage="Output" Radix="Decimal" Required="false" Visible="true" ExternalAccess="Read/Write">
    <Description>
    <![CDATA[Out Of Service]]>
    </Description>
    <DefaultData Format="L5K">
    <![CDATA[0]]>
    </DefaultData>
    <DefaultData Format="Decorated">
    <DataValue DataType="BOOL" Radix="Decimal" Value="0"/>
    </DefaultData>
    </Parameter>
    <Parameter Name="InService" TagType="Base" DataType="BOOL" Usage="Output" Radix="Decimal" Required="false" Visible="true" ExternalAccess="Read/Write">
    <Description>
    <![CDATA[In Service]]>
    </Description>
    <DefaultData Format="L5K">
    <![CDATA[0]]>
    </DefaultData>
    <DefaultData Format="Decorated">
    <DataValue DataType="BOOL" Radix="Decimal" Value="0"/>
    </DefaultData>
    </Parameter>
    <Parameter Name="EU" TagType="Base" DataType="REAL" Usage="Output" Radix="Float" Required="false" Visible="true" ExternalAccess="Read Only">
    <DefaultData Format="L5K">
    <![CDATA[0.00000000e+000]]>
    </DefaultData>
    <DefaultData Format="Decorated">
    <DataValue DataType="REAL" Radix="Float" Value="0.0"/>
    </DefaultData>
    </Parameter>
    <Parameter Name="EUMax" TagType="Base" DataType="REAL" Usage="Output" Radix="Float" Required="false" Visible="false" ExternalAccess="Read Only">
    <Description>
    <![CDATA[Logical EU Max]]>
    </Description>
    <DefaultData Format="L5K">
    <![CDATA[0.00000000e+000]]>
    </DefaultData>
    <DefaultData Format="Decorated">
    <DataValue DataType="REAL" Radix="Float" Value="0.0"/>
    </DefaultData>
    </Parameter>
    <Parameter Name="EUMin" TagType="Base" DataType="REAL" Usage="Output" Radix="Float" Required="false" Visible="false" ExternalAccess="Read Only">
    <Description>
    <![CDATA[Logical EU Min]]>
    </Description>
    <DefaultData Format="L5K">
    <![CDATA[0.00000000e+000]]>
    </DefaultData>
    <DefaultData Format="Decorated">
    <DataValue DataType="REAL" Radix="Float" Value="0.0"/>
    </DefaultData>
    </Parameter>
    </Parameters>




    <LocalTags>
    <LocalTag Name="Rate" DataType="REAL" Radix="Float" ExternalAccess="None">
    <DefaultData Format="L5K">
    <![CDATA[0.00000000e+000]]>
    </DefaultData>
    <DefaultData Format="Decorated">
    <DataValue DataType="REAL" Radix="Float" Value="0.0"/>
    </DefaultData>
    </LocalTag>
    <LocalTag Name="ConfigError" DataType="BOOL" Radix="Decimal" ExternalAccess="Read Only">
    <Description>
    <![CDATA[Error Bit]]>
    </Description>
    <DefaultData Format="L5K">
    <![CDATA[0]]>
    </DefaultData>
    <DefaultData Format="Decorated">
    <DataValue DataType="BOOL" Radix="Decimal" Value="0"/>
    </DefaultData>
    </LocalTag>
    <LocalTag Name="OutOfRange" DataType="BOOL" Radix="Decimal" ExternalAccess="Read Only">
    <Description>
    <![CDATA[Out of Range]]>
    </Description>
    <DefaultData Format="L5K">
    <![CDATA[0]]>
    </DefaultData>
    <DefaultData Format="Decorated">
    <DataValue DataType="BOOL" Radix="Decimal" Value="0"/>
    </DefaultData>
    </LocalTag>
    <LocalTag Name="HMI_OutOfService" DataType="BOOL" Radix="Decimal" ExternalAccess="Read/Write">
    <Description>
    <![CDATA[HMI Out Of Service
    Command]]>
    </Description>
    <DefaultData Format="L5K">
    <![CDATA[0]]>
    </DefaultData>
    <DefaultData Format="Decorated">
    <DataValue DataType="BOOL" Radix="Decimal" Value="0"/>
    </DefaultData>
    </LocalTag>
    <LocalTag Name="HMI_InService" DataType="BOOL" Radix="Decimal" ExternalAccess="None">
    <Description>
    <![CDATA[HMI In Service
    Command]]>
    </Description>
    <DefaultData Format="L5K">
    <![CDATA[0]]>
    </DefaultData>
    <DefaultData Format="Decorated">
    <DataValue DataType="BOOL" Radix="Decimal" Value="0"/>
    </DefaultData>
    </LocalTag>
    </LocalTags>





    <Routines>
    <Routine Name="Logic" Type="RLL">
    <RLLContent>
    <Rung Number="0" Type="N">
    <Comment>
    <![CDATA[Divide by 0 protection (if Input Max and Min are equal to each other)
    **********************************]]>
    </Comment>
    <Text>
    <![CDATA[NOP();]]>
    </Text>
    </Rung>
    <Rung Number="1" Type="N">
    <Text>
    <![CDATA[[EQU(Input_Max,Input_Min) ,EQU(P_ScaledMin,P_ScaledMax) ]OTE(ConfigError);]]>
    </Text>
    </Rung>
    <Rung Number="2" Type="N">
    <Comment>
    <![CDATA[EU Calculation
    **********************************]]>
    </Comment>
    <Text>
    <![CDATA[NOP();]]>
    </Text>
    </Rung>
    <Rung Number="3" Type="N">
    <Text>
    <![CDATA[XIO(ConfigError)CPT(Rate,(P_ScaledMax-P_ScaledMin)/(Input_Max-Input_Min))CPT(EU,(Input-Input_Min)*Rate+P_ScaledMin);]]>
    </Text>
    </Rung>
    <Rung Number="4" Type="N">
    <Text>
    <![CDATA[XIO(ConfigError)[GRT(P_ScaledMax,P_ScaledMin) [MOV(P_ScaledMin,EUMin) ,MOV(P_ScaledMax,EUMax) ] ,LES(P_ScaledMax,P_ScaledMin) [MOV(P_ScaledMax,EUMin) ,MOV(P_ScaledMin,EUMax) ] ];]]>
    </Text>
    </Rung>
    <Rung Number="5" Type="N">
    <Comment>
    <![CDATA[Out of Range Calculation
    **********************************

    Calculates 5% of input range to define the out of range alarms

    For example, for a 4-20mA analog input (16 mA range). 5% of 16 is .8. Therefore, 

    Input > 20.8 
    OR
    Input < 3.2 

    triggers an out of range alarm]]>
    </Comment>
    <Text>
    <![CDATA[NOP();]]>
    </Text>
    </Rung>
    <Rung Number="6" Type="N">
    <Text>
    <![CDATA[XIO(ConfigError)[CMP(Input > (((Input_Max - Input_Min)*0.05)+Input_Max)) ,CMP(Input < (Input_Min - ((Input_Max - Input_Min)*0.05))) ]OTE(OutOfRange);]]>
    </Text>
    </Rung>
    <Rung Number="7" Type="N">
    <Text>
    <![CDATA[[XIO(ConfigError) XIO(OutOfRange) ,XIC(OutOfService) ]OTE(InOK);]]>
    </Text>
    </Rung>
    <Rung Number="8" Type="N">
    <Comment>
    <![CDATA[LowLow, Low, High, High High Defintion
    **********************************]]>
    </Comment>
    <Text>
    <![CDATA[NOP();]]>
    </Text>
    </Rung>
    <Rung Number="9" Type="N">
    <Text>
    <![CDATA[XIC(InOK)XIC(InService)[NEQ(P_HighHigh,EUMax) GRT(EU,P_HighHigh) OTE(HighHigh) ,NEQ(P_High,EUMax) GRT(EU,P_High) OTE(High) ,NEQ(P_Low,EUMin) LES(EU,P_Low) OTE(Low) ,NEQ(P_LowLow,EUMin) LES(EU,P_LowLow) OTE(LowLow) ];]]>
    </Text>
    </Rung>
    <Rung Number="10" Type="N">
    <Comment>
    <![CDATA[Bypassed
    **********************************]]>
    </Comment>
    <Text>
    <![CDATA[NOP();]]>
    </Text>
    </Rung>
    <Rung Number="11" Type="N">
    <Text>
    <![CDATA[XIC(HMI_I_OutOfService)[OTE(HMI_OutOfService) ,OTU(HMI_I_OutOfService) ];]]>
    </Text>
    </Rung>
    <Rung Number="12" Type="N">
    <Text>
    <![CDATA[XIC(HMI_I_InService)[OTE(HMI_InService) ,OTU(HMI_I_InService) ];]]>
    </Text>
    </Rung>
    <Rung Number="13" Type="N">
    <Text>
    <![CDATA[XIC(Service_Enable)[XIC(Service_Permission) XIC(HMI_OutOfService) ,XIC(OutOfService) [XIO(HMI_InService) ,XIO(Service_Permission) ] ]OTE(OutOfService);]]>
    </Text>
    </Rung>
    <Rung Number="14" Type="N">
    <Text>
    <![CDATA[XIO(OutOfService)OTE(InService);]]>
    </Text>
    </Rung>
    </RLLContent>
    </Routine>
    </Routines>
</AddOnInstructionDefinition>
</AddOnInstructionDefinitions>''',

'data': f'''<Data Format="L5K">
            <![CDATA[[4231,3.68000000e+002,-2.00000000e+003,6.30000000e+003,-2.00000000e+002,6.30000000e+002
            ,-2.00000000e+002,-2.00000000e+002,6.00000000e+001,9.00000000e+001,3.68000031e+001,6.30000000e+002
            ,-2.00000000e+002,1.00000000e-001]]]>
            </Data>
            <Data Format="Decorated">
            <Structure DataType="SCP_ER_AI">
                <DataValueMember Name="EnableIn" DataType="BOOL" Value="1"/>
                <DataValueMember Name="EnableOut" DataType="BOOL" Value="1"/>
                <DataValueMember Name="Input" DataType="REAL" Radix="Float" Value="368.0"/>
                <DataValueMember Name="InOK" DataType="BOOL" Value="1"/>
                <DataValueMember Name="Input_Min" DataType="REAL" Radix="Float" Value="-2000.0"/>
                <DataValueMember Name="Input_Max" DataType="REAL" Radix="Float" Value="6300.0"/>
                <DataValueMember Name="LowLow" DataType="BOOL" Value="0"/>
                <DataValueMember Name="Low" DataType="BOOL" Value="0"/>
                <DataValueMember Name="High" DataType="BOOL" Value="0"/>
                <DataValueMember Name="HighHigh" DataType="BOOL" Value="0"/>
                <DataValueMember Name="P_ScaledMin" DataType="REAL" Radix="Float" Value="-200.0"/>
                <DataValueMember Name="P_ScaledMax" DataType="REAL" Radix="Float" Value="630.0"/>
                <DataValueMember Name="P_LowLow" DataType="REAL" Radix="Float" Value="-200.0"/>
                <DataValueMember Name="P_Low" DataType="REAL" Radix="Float" Value="-200.0"/>
                <DataValueMember Name="P_High" DataType="REAL" Radix="Float" Value="60.0"/>
                <DataValueMember Name="P_HighHigh" DataType="REAL" Radix="Float" Value="90.0"/>
                <DataValueMember Name="Service_Enable" DataType="BOOL" Value="1"/>
                <DataValueMember Name="Service_Permission" DataType="BOOL" Value="0"/>
                <DataValueMember Name="HMI_I_OutOfService" DataType="BOOL" Value="0"/>
                <DataValueMember Name="HMI_I_InService" DataType="BOOL" Value="0"/>
                <DataValueMember Name="OutOfService" DataType="BOOL" Value="0"/>
                <DataValueMember Name="InService" DataType="BOOL" Value="1"/>
                <DataValueMember Name="EU" DataType="REAL" Radix="Float" Value="36.800003"/>
                <DataValueMember Name="EUMax" DataType="REAL" Radix="Float" Value="630.0"/>
                <DataValueMember Name="EUMin" DataType="REAL" Radix="Float" Value="-200.0"/>
                </Structure>'''

}