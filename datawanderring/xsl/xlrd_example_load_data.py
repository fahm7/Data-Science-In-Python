import xlrd

datafile = "2013_ERCOT_Hourly_Load_Data.xls"

def parse_file(datafile):

    # open and read the xsl file
    workbook = xlrd.open_workbook(datafile)


    print ("number of sheets:")
    print (workbook.nsheets)

    # print sheet names
    print (workbook.sheet_names())

    first_sheet = workbook.sheet_by_index(0)

    # read a row
    print (first_sheet.row_values(0))


    # read a cell
    cell = first_sheet.cell(0, 0)
    print (cell)
    print (cell.value)

    print (first_sheet.row_slice(rowx=0,
                                start_colx=0,
                                end_colx=2))



    data = [[first_sheet.cell_value(r, col)
                for col in range(first_sheet.ncols)]
                    for r in range(first_sheet.nrows)]


    print ("\n************List Comprehension************")
    print("data[3][0]:")
    print(data[3][0])
    print("data[3][1]:")
    print(data[3][1])
    print ("data[3][2]:")
    print (data[3][2])

    print ("\n***************Cells in a nested loop:********************")
    for row in range(first_sheet.nrows):
        for col in range(first_sheet.ncols):
            if row == 50:
                print (first_sheet.cell_value(row, col))



    ### other useful methods:
    print ("***********\nROWS, COLUMNS, and CELLS:**************")
    print( "Number of rows in the sheet:")
    print (first_sheet.nrows)
    print ("Type of data in cell (row 3, col 2):")
    print (first_sheet.cell_type(3, 2))
    print ("Value in cell (row 3, col 2):")
    print (first_sheet.cell_value(3, 2))
    print("Get a slice of values in column 3, from rows 1-3:")
    print(first_sheet.col_values(3, start_rowx=1, end_rowx=4))


    print ("\n********DATES:********")
    print ("Type of data in cell (row 1, col 0):")
    print (first_sheet.cell_type(1, 0))
    exceltime = first_sheet.cell_value(1, 0)
    print ("Time in Excel format:")
    print (exceltime)

    print ("Convert time to a Python datetime tuple, from the Excel float:")
    print (xlrd.xldate_as_tuple(exceltime, 0))


    return data

data = parse_file(datafile)