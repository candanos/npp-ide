bch_key = "'13800108858'"
my_time = Now 
my_time = Trim(Replace(my_time,":",""))
my_time = Replace(my_time,".","")
my_time = Replace(my_time," ","")
if Len(my_time) = 13 then 
	my_date = Left(my_time,7)
	my_date = Right(my_date,4) & Mid(my_date,2,2) & "0" & Left(my_date,1)
else 
	my_date = Left(my_time,8)
	my_date = Right(my_date,4) & Mid(my_date,3,2) & Left(my_date,2)
end if
my_time = Right(my_time,6)
Dim FolderName
FolderName = "C:\Users\CY59857\Desktop\" 
Dim filename
filename = FolderName & "resultset.txt"
Set objFSO = CreateObject("Scripting.FileSystemObject")
If Not objFSO.FolderExists(FolderName) Then
	Set objResultFile = objFSO.CreateTextFile(filename)
Else
	Set objResultFile = objFSO.CreateTextFile(filename)
End If
Dim excelFile 
excelFile = FolderName & "Resultset_" & my_time & ".xlsx"	
Set objExcel = CreateObject("Excel.Application")	
objExcel.Visible = True
Set objWorkbook = objExcel.Workbooks.Add()
objWorkbook.SaveAs(excelFile)
Set objWorkbook = objExcel.Workbooks.Open(excelFile)
objWorkbook.Activate
Set objWorkSheet = objWorkbook.Worksheets(1)
objWorkSheet.Activate

oracleConnStr = "Provider=OraOLEDB.Oracle;Data Source=VERIMPRD_DDMA;User Id=59857;Password=cD194775;"
Set OCon = CreateObject("ADODB.Connection")
Set ORs = CreateObject("ADODB.Recordset")
OCon.Open oracleConnStr
sqlstr = "SELECT * FROM ODS.TRX_BDEFSDEP T1 WHERE T1.SEGCKEY  = " & bch_key &  " ORDER BY 2 ASC"
Set ORs = OCon.Execute(sqlstr)
set obJRange = objWorksheet.Range("A1")
r = 1
'colNum = oRs.FieldCount()
Do While Not oRs.EOF	
	For i=0 To 8
		name = oRs.Fields(i).Name
		obJRange.Offset(0,i).ColumnWidth = 18
		objRange.Offset(0,i).Value = name
	Next
	For i=0 To 8
		myVal = oRs.Fields(i).Value
		if (myVal) = "" then 
			myval = " "
		end if		
		objRange.Offset(r,i).Value = myVal
	Next
	r = r + 1
	oRs.MoveNext
Loop
oCon.Close
Set oRs = Nothing
Set oCon = Nothing	