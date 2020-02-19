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
filename = FolderName & "KKB-DKR Results.txt"
Dim logFile  
logFile = FolderName & "KKB-DKR Log.txt"
Dim excelFile 
excelFile = FolderName & "KKB_Rapor_" & my_date & my_time & ".xlsx"
Dim scriptFileD  
scriptFileD = FolderName & "DbUtilScript_Disb.sql"
Dim scriptFileR
scriptFileR = FolderName & "DbUtilScript_Repay.sql"
Dim DkrResultStr
Dim DekResultStr
Dim objFSO
Dim objLogFSO
Dim objScriptD_FSO
Dim objScriptR_FSO
Dim objResultFile
Dim objLogFile
Dim objScriptFileD
Dim objScriptFileR
Dim objExcel
Dim objWorkbook
Dim objWorksheet

status = CreateFiles()
queryResults = GetQueryResults("DKR")
status = CreateScript(queryResults)	
objScriptFileR.writeline("COMMIT;")
objScriptFileD.writeline("COMMIT;")

objWorkbook.Save
objWorkbook.Close
WScript.Quit
	
Function CreateFiles()
	Set objFSO = CreateObject("Scripting.FileSystemObject")
	If Not objFSO.FolderExists(FolderName) Then
		Set LogFolder = objFSO.CreateFolder(FolderName)
		Set objResultFile = objFSO.CreateTextFile(filename)
	Else
		Set objResultFile = objFSO.CreateTextFile(filename)
	End If
	
	Set objLogFSO = CreateObject("Scripting.FileSystemObject")	
	If objLogFSO.FileExists(FolderName & logFile) then
		objLogFSO.DeleteFile(FolderName & logFile)
	Else	
		Set objLogFile = objLogFSO.CreateTextFile(logFile)
	End If
	
	Set objScriptD_FSO = CreateObject("Scripting.FileSystemObject")	
	If objScriptD_FSO.FileExists(FolderName & scriptFileD) then
		objScriptD_FSO.DeleteFile(FolderName & scriptFileD)
	Else	
		Set objScriptFileD = objScriptD_FSO.CreateTextFile(scriptFileD)
	End If
	
	Set objScriptR_FSO = CreateObject("Scripting.FileSystemObject")	
	If objScriptR_FSO.FileExists(FolderName & scriptFileR) then
		objScriptR_FSO.DeleteFile(FolderName & scriptFileR)
	Else	
		Set objScriptFileR = objScriptR_FSO.CreateTextFile(scriptFileR)
	End If
	
	objLogFile.writeline("logfile created")
	
	Set objExcel = CreateObject("Excel.Application")	
	objExcel.Visible = False
	Set objWorkbook = objExcel.Workbooks.Add()
	objWorkbook.SaveAs(excelFile)
	objLogFile.writeline("ExcelFile saved.")
	Set objWorkbook = objExcel.Workbooks.Open(excelFile)
	objWorkbook.Activate
	Set objWorkSheet = objWorkbook.Worksheets(1)
	objWorkSheet.Activate
	objWorkSheet.Name = "DEK"
	Set objWorkSheet = objWorkbook.Worksheets.Add()
	objWorkSheet.Activate
	objWorkSheet.Name = "DKR"

	objLogFile.writeline("ExcelFile opened.")
	CreateFiles = 0 
End Function

Function GetQueryResults(typ)
	Dim i 
	i = 0
	Dim sqlstart
	Dim sqlend
	Dim sqlstr
	Dim ResultLine
	Dim ResultStr
		
	Set file = objFSO.OpenTextFile("C:\Users\CY59857\Desktop\kkb_bozuk.csv", 1)
	ResultStr = file.ReadAll
	
	TmpArr = Split(ResultStr, vbLF)
	k = 0 
	x = UBound(TmpArr) 
	For i = 1 To (UBound(TmpArr))
		objLogFile.writeline("i:" & i & ">" & TmpArr(i))
		If i = (UBound(TmpArr)) Then
			Redim Preserve ResultArr(k+1)
			ResultArr(k) =  TmpArr(i)
		Else
			j = i + 1
			ColArr = Split(TmpArr(i),";")
			NextColArr = Split(TmpArr(j),";")
			kkb_balance = 0 
			kkb_balance_0 = ColArr(3)
			kkb_balance_1 = NextColArr(3)
			credit_balance = ColArr(2)
			
			objLogFile.writeline("************read from file******") 
			objLogFile.writeline("kkb_balance_0: " & kkb_balance_0)
			objLogFile.writeline("kkb_balance_1: " & kkb_balance_1)
			objLogFile.writeline("credit_balance: " & credit_balance)
			objLogFile.writeline("************read from file******")
			objLogFile.writeline("                                ")
			
			kkb_balance_0 = Replace(kkb_balance_0, ".", ",")
			kkb_balance_1 = Replace(kkb_balance_1, ".",",")
			credit_balance = Replace(credit_balance, ".",",")
			
			objLogFile.writeline("************read after replace******") 
			objLogFile.writeline("kkb_balance_0: " & kkb_balance_0)
			objLogFile.writeline("kkb_balance_1: " & kkb_balance_1)
			objLogFile.writeline("credit_balance: " & credit_balance)
			objLogFile.writeline("************read after replace******")
			objLogFile.writeline("                                ")
			
			kkb_balance_0 = FormatNumber(kkb_balance_0,2,0,0,0)
			kkb_balance_1 = FormatNumber(kkb_balance_1,2,0,0,0)
			credit_balance = FormatNumber(credit_balance,2,0,0,0)

			objLogFile.writeline("************after formatNumber******") 
			objLogFile.writeline("kkb_balance_0: " & kkb_balance_0)
			objLogFile.writeline("kkb_balance_1: " & kkb_balance_1)
			objLogFile.writeline("credit_balance: " & credit_balance)
			objLogFile.writeline("************after formatNumber******")
			objLogFile.writeline("                                ")
			kkb_balance_0 = Int((100 * kkb_balance_0))
			kkb_balance_1 = Int((100 * kkb_balance_1))
			credit_balance = Int((-100 * credit_balance))

			objLogFile.writeline("************after X100 ******") 
			objLogFile.writeline("kkb_balance_0: " & kkb_balance_0)
			objLogFile.writeline("kkb_balance_1: " & kkb_balance_1)
			objLogFile.writeline("credit_balance: " & credit_balance)
			objLogFile.writeline("************after X100******")
			objLogFile.writeline("                                ")
			
			kkb_balance = (kkb_balance_0 + kkb_balance_1)
			kkb_balance = Int(kkb_balance)
			credit_balance = Int(credit_balance)
			acc_id_0 = ColArr(0)
			acc_id_1 = NextColArr(0)	
			If acc_id_0 = acc_id_1 Then	
				objLogFile.writeline("kkb_balance_0: " & kkb_balance_0)
				objLogFile.writeline("kkb_balance_1: " & kkb_balance_1)
				objLogFile.writeline("credit_balance: " & credit_balance)				
				fark = Int((kkb_balance - credit_balance))
				objLogFile.writeline("fark: " & fark)	
				If ((fark = 0) OR (fark = 1) OR (fark = -1) OR (kkb_balance = credit_balance)) Then 
					i = i + 1
				Else
					objLogFile.writeline("Sorunlu hesap: " & acc_id_0)
					Redim Preserve ResultArr(k+1)
					ResultArr(k) =  TmpArr(i)
					k = k + 1
					objLogFile.writeline("Sorunlu hesap: " & acc_id_1)
					Redim Preserve ResultArr(k+1)
					ResultArr(k) =  TmpArr(j)
					k = k + 1
					i = i + 1
				End If
			Else
				fark = Int((credit_balance - kkb_balance_0))
				If ((fark <> 0)) Then
					objLogFile.writeline("Sorunlu hesap: " & acc_id_0)
					Redim Preserve ResultArr(k+1)
					ResultArr(k) =  TmpArr(i)
					k = k + 1
				End If	
			End If 
		End If
	Next
	ResultStr = ""
	For i = 0 To (UBound(ResultArr) - 1)
		If ResultStr = "" Then
			ResultStr = Replace(ResultArr(i),".",",")
		Else
			ResultStr = ResultStr & vbLF & Replace(ResultArr(i),".",",")
		End If	
	Next
	GetQueryResults = ResultStr
	objLogFile.writeline("Sorun tespit edilen kayitlar:") 
	objLogFile.writeline(ResultStr) 
End Function	

Function CreateScript(ResultStr)
	ResultArr = Split(ResultStr, vbLF)	
	For i = 0 To (UBound(ResultArr) -1)
		scr = 1
		ColArr = Split(ResultArr(i),";")
		x = i - 1 
		z = i + 1 
		prevLoiId = ""
		nextLoiId = ""
		loi_id = ColArr(1)
			
		if (i > 0) then 
			prevLoiArr = Split(ResultArr(x),";")
			prevLoiId = prevLoiArr(1)
		end if
		if (i < (UBound(ResultArr) - 1)) then
			nextLoiArr = Split(ResultArr(z),";")
			nextLoiId = nextLoiArr(1)
		end if
		if ( (loi_id = nextLoiId) or (loi_id = prevLoiId) ) then
			scr = 0
		end if
		If scr = 1 Then	
			Amt_0 = (ColArr(2) + 0)						
			Amt_1 = (ColArr(3) + 0)
			Amt_0 = FormatNumber(Amt_0,2,0,0,0)
			Amt_1 = FormatNumber(Amt_1,2,0,0,0)
			Amt_0 = Int((-100 * Amt_0))
			Amt_1 = Int((100 * Amt_1))
			if ( (Amt_0 > Amt_1) or (Amt_0 < Amt_1) ) then
				if (Amt_0 > Amt_1) then
					not_typ = "D"
					not_amt = ((Amt_0 / 100) - (Amt_1 / 100))	
				else
					not_typ = "R"
					not_amt = ((Amt_1 / 100) - (Amt_0 / 100))					
				end if						
				not_amt = FormatNumber(not_amt,2,0,0,0)
				not_amt = Replace(CStr((not_amt)),",",".")
				pnt = "."
				parleft = "(" 
				parright = ")" 
				comma = ","				
				scriptText = "insert into " & Chr(34) & "SCLOAN" & Chr(34) & pnt & Chr(34) & "LFN_KKB_NOTIFICATION" & Chr(34) &_
					parleft & Chr(34) & "NOT_LOI_ID" & Chr(34) & comma & Chr(34) & "NOT_TRX_AMOUNT" & Chr(34) & comma & Chr(34) & "NOT_TYPE" & Chr(34) & comma &_
					Chr(34) & "NOT_STATUS" & Chr(34) & comma & Chr(34) & "NOT_DESC" & Chr(34) & comma & Chr(34) & "NOT_CREATE_USER" & Chr(34) & comma &_
					Chr(34) & "NOT_CREATE_TIME" & Chr(34) & comma & Chr(34) & "NOT_UPDATE_USER" & Chr(34) & comma & Chr(34) & "NOT_UPDATE_TIME" & Chr(34) & parright &_
					" values (" & loi_id & "," & not_amt & "," & "'" & not_typ & "'" & ",'P','','DBUTILS',CURRENT TIMESTAMP,'',CURRENT TIMESTAMP);"
				if not_typ = "D" then 		
					objScriptFileD.writeline(scriptText)
				else
					objScriptFileR.writeline(scriptText)
				end if 	
			end if
		End If
	Next	
End Function