#!/usr/bin/env python
import openpyxl as px

def main():
    wb = px.load_workbook('../DATA/presidents.xlsx')
    ws = wb.active  # <.>
    all_values = ws.values
    headers = next(all_values)   # <.>
    print("Headers:", headers)
    for row in all_values:  # <.>
        print(row[:5])   # <.>


if __name__ == '__main__':
    main()
