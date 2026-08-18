import sys
from openpyxl import load_workbook

input_file = sys.argv[1]

workbook = load_workbook(input_file)
sheet = workbook.active
