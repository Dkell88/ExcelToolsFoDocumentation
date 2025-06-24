import pandas as pd

def FindCard(df):
    """
    Function to find row numbers where:
    - Column G has a non-empty value
    - Column E has a value of 0

    Parameters:
    df (pd.DataFrame): The DataFrame representing the spreadsheet.

    Returns:
    List[int]: A list of row indices that satisfy the conditions.
    """
    # Create a list to store the row numbers that match the condition
    matching_rows = []

    # Loop through each row in the DataFrame
    for index, row in df.iterrows():
        # print(row[4])
        if pd.notna(row.iloc[6]) and row.iloc[4] == '00':
            matching_rows.append(index)

    return matching_rows

def GetMetaData(df):
    """
    Function to extract metadata from the Excel file.

    Parameters:
    df (pd.DataFrame): The DataFrame representing the spreadsheet.

    Returns:
    dict: A dictionary containing metadata such as Revision, Program Name, Project Ref, and Date.
    """
    # Create a dictionary to store the metadata
    metadata = {}

    # Extract Revision from the Excel file. Currently, it is hard-coded.
    # TODO: Update this to extract Revision from the Excel file.
    metadata['Revision'] = "32.04"

    # Extract Program Name from row 5, column 7 in the Excel file.
    metadata['Program Name'] = df.iloc[4, 7]

    # Extract Project Ref from row 4, column 7 in the Excel file.
    metadata['Project Ref'] = df.iloc[3, 7]

    # Extract Date from row 1, column 7 in the Excel file.
    metadata['Date'] = df.iloc[0, 7]

    # Extract is we are using a UDT standard
    udt = df.iloc[2, 7]
    print(f'UDT: {udt}')
    if udt == 'YES':
        metadata['UDT'] = 1
    else:
        metadata['UDT'] = 0

    return metadata
