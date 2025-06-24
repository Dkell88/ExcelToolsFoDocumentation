from pathlib import Path
import pandas as pd
from datetime import datetime
from typing import List
from ExtractIOandConvert import convert_excel_to_csv


def extract_io_sheets_case_insensitive(
    keywords: List[str],
    excel_path: Path,
    output_xlsx: Path
) -> Path:
    """
    Reads the "IO LIST" sheet from `excel_path` and for each keyword:
      • Filters rows where column Q (index 16) contains the keyword, case-insensitive.
      • Extracts columns C,D,E,H,K,Q (positions 2,3,4,7,10,16).
      • Writes each filtered set to its own worksheet in a timestamped Excel file.
    Returns the Path to that timestamped file.
    """
    # 1) Load the source sheet
    df = pd.read_excel(excel_path, sheet_name="IO LIST", dtype=str)

    # 2) Build a timestamp string
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")

    # 3) Insert it before the extension
    stem, suffix = output_xlsx.stem, output_xlsx.suffix
    timestamped = output_xlsx.with_name(f"{stem}_{ts}{suffix}")

    # 4) Write out each keyword as its own sheet    
    with pd.ExcelWriter(timestamped, engine="openpyxl") as writer:
        for kw in keywords:
            col_q = df.iloc[:, 16].fillna("")
            mask = col_q.str.contains(kw, case=False, na=False)
            cols_idx = [2, 3, 4, 7, 10, 16]
            filtered = df.loc[mask, :].iloc[:, cols_idx]
            filtered.columns = ["C", "D", "E", "H", "K", "Q"]

            # Sanitize sheet name
            safe = "".join(ch for ch in kw if ch.isalnum())[:31] or "Sheet"
            filtered.to_excel(writer, sheet_name=safe, index=False)

    print(f"Wrote {len(keywords)} sheets to {timestamped!r}")
    return timestamped
    

script_folder = Path(__file__).parent
backend_folder = script_folder.parent
excel_folder = backend_folder / "data" / "excel"
filename = "8083-041000-L-SL3-001-F Instrument List.xlsx"
excel_path = excel_folder / filename
print("Loading Excel from:", excel_path)
if not excel_path.exists():
    raise FileNotFoundError(f"Couldn’t find the file at {excel_path!r}")

keywords = ["HVAC", "Take-Up", "HPU"]           # your list of keywords
input_file = excel_path
filename = "filtered_io_by_keyword.xlsx"
excel_folder = backend_folder / "data" / "excel" / "KeywordXlsx"
excel_path = excel_folder / filename
output_file = excel_path

output_file = extract_io_sheets_case_insensitive(keywords, input_file, output_file)
print(f"Wrote {len(keywords)} sheets to {output_file!r}")
print(f" {len(keywords)} sheets to {output_file!r}")
convert_excel_to_csv(output_file)







    #{   # def extract_io_rows(keywords: List[str], excel_path: Path, output_csv: Path) -> None:
        #     """
        #     1. Load the "IO LIST" sheet.
        #     2. For each cell in column Q (zero-based index 16), check if any keyword appears.
        #     3. When matched, pull columns at positions [2,3,4,7,10,16] (i.e. C,D,E,H,K,Q).
        #     4. Write all matches to CSV.
        #     """
        #     # 1) Read the sheet
        #     df = pd.read_excel(excel_path, sheet_name="IO LIST", dtype=str)

        #     # 2) Build a boolean mask over column Q (index 16)
        #     col_q = df.iloc[:, 16].fillna("")  # ensure no NaNs
        #     mask = col_q.apply(lambda cell: any(kw in cell for kw in keywords))

        #     # 3) Slice out the matching rows + the six columns you want
        #     cols_idx = [2, 3, 4, 7, 10, 16]
        #     filtered = df.loc[mask, :].iloc[:, cols_idx]

        #     # 4) (Optionally) rename the output columns to something meaningful:
        #     filtered.columns = ["Rack", "Slot", "Channel", "Type", "Tag", "Description"]

        #     # 5) Write it out
        #     filtered.to_csv(output_csv, index=False)


        #     return None
    #}

