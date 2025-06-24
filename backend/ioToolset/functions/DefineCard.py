import pandas as pd

def DefineCard(df, start_index):
    """
    Function to create an object containing Card type, Number of channels, and a 2D array.
    
    Parameters:
    df (pd.DataFrame): The DataFrame representing the spreadsheet.
    start_index (int): The starting row index to begin the loop.
    
    Returns:
    dict: An object containing the specified keys and values.
    """
    card_type = df.iloc[start_index, 7]
    module = df.iloc[start_index, 6]
    rack_num = df.iloc[start_index, 2]
    panel_name = df.iloc[start_index, 1]
    slot = df.iloc[start_index, 3]
    channels = []
    
    for index in range(start_index, len(df)):
        number_value = df.iloc[index, 4]
        tag_description = df.iloc[index, 10]
        equipment = df.iloc[index, 17]
        comment = df.iloc[index, 16]
        eu_min = df.iloc[index, 21]
        eu_max = df.iloc[index, 22]
        lmt_lo_lo = df.iloc[index, 23]
        lmt_low = df.iloc[index, 24]
        lmt_hi = df.iloc[index, 25]
        lmt_hi_hi = df.iloc[index, 26]

        
        if pd.notna(number_value) and pd.notna(tag_description):
            channel = {
                "Equipment": equipment,
                "Number Value": number_value,
                "Tag Description": tag_description,
                "Comment": comment,
                "Limits": {
                    "EU Min": eu_min,
                    "EU Max": eu_max,
                    "Lo Lo": lmt_lo_lo,
                    "Low": lmt_low,
                    "Hi": lmt_hi,
                    "Hi Hi": lmt_hi_hi
                }
            }
            channels.append(channel)
        else:
            break
    
    result_object = {
        'Cardtype': card_type,
        'Number of channels': len(channels),
        'Panel Name': panel_name,
        'Card Name': module,
        'Rack Number': rack_num,
        'Slot': slot,
        'IO Points': channels
    }
    
    return result_object

# Example usage:
# df = pd.read_excel('your_spreadsheet.xlsx')  # Replace with your actual DataFrame loading method
# start_index = find_row(df)[0]  # Assuming find_row returns a list of indices and we're taking the first one
# result = create_object(df, start_index)
# print(result)
