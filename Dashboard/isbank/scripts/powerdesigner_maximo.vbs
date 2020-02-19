Sub %Method%(obj)
   ' Implement your method on <obj> here
   if obj.model.GetExtendedAttribute("Repository") = "1_DEV_TEST" then
      msgbox "This function can only be used for INT-UAT-PROD Environments."
   elseif err_count>0 then
      msgbox "Please fix the errors."
   'elseif not MaximoAllowed then
   '   msgbox "Model is changed after check-out. Send to Maximo is not allowed."
   else
      'surum starts here 
      dim fark1,fark2,ay,ResultBoolean
      ResultBoolean= True
      ay = Month(date) 
      dim fso, filename,f,StrDelimitedLine,Dates,Date1,Date2
      dim aa,gg, yyyy, aa1, gg1, yyyy1
      filename = "\\power.isbank\PD_SHARE\LOVs\ReleaseDate.txt"
      set fso = CreateObject("Scripting.FileSystemObject")
      set f = fso.OpenTextFile(filename, 1)
      ScriptResult=""
      Do until f.AtEndOfStream 
         StrDelimitedLine=f.ReadLine      
         if ay=CInt(Left(StrDelimitedLine,InStrRev(StrDelimitedLine, "-") -1))  then
            Dates= Right(StrDelimitedLine,Len(StrDelimitedLine)-InStrRev(StrDelimitedLine, "-"))
            gg = Mid(Dates,1,2)
            aa = Mid(Dates,4,2)
            yyyy = Mid(Dates,7,4)
            Date1= dateserial(yyyy,aa,gg) + timeserial(23,59,59)
            gg1 = Mid(Dates,21,2)
            aa1 = Mid(Dates,24,2)
            yyyy1 = Mid(Dates,27,4)
            Date2= dateserial(yyyy1,aa1,gg1) + timeserial(09,00,00)
            'Date1= Cdate(Left(Dates,Len(Dates)-InStrRev(Dates, ";")))
            'Date2= Cdate(Right(Dates,Len(Dates)-InStrRev(Dates, ";")))
         End If
      Loop  
      f.Close
      Set fso = Nothing
   
      fark1 = DateDiff("s",now, Date1)
      fark2 = DateDiff("s",now, Date2)
      if fark1 < 0 then
         if fark2 > 0 then
             if obj.model.GetExtendedAttribute("Repository") = "3_PROD" then
                msgbox  "Sürüm nedeniyle " & Date2 &  " tarihine kadar maximo girişleri kapatılmıştır." 
                ResultBoolean = False    
             end if
         end if
      end if
     'surum ends here
      
           
      'grant starts here
      dim sendUser
      if len(UserName) = 5 then
         sendUser = UserName
      elseif len(UserName) = 6 then
         sendUser = UserName
      elseif len(UserName) = 7 then
         sendUser = right(UserName, 5)
      end if 
      dim groups, usr, devGroupName, ownGroupName,grantCount
      grantCount=0
      devGroupName="DEV_"&obj.GetExtendedAttribute("ProjectCode")
      ownGroupName="OWN_"&obj.GetExtendedAttribute("ProjectCode")
      'for each groups in RepositoryConnection.Groups
         'if groups.Name=devGroupName Or groups.Name=ownGroupName then
            'for each usr in groups.GroupUsers
               'if usr.LoginName=sendUser then
                  'grantCount=grantCount+1
               'end if
            'next   
         'end if
      'next
      'if grantCount=0 then 
          'ResultBoolean=False
          'msgbox "Modelde Maximo kaydı açmaya yetkili değilsiniz. Lütfen VYB - Veri Mimarisi ekibi ile iletişime geçiniz."
      'end if
   'grant ends here
   
      if ResultBoolean = True then
            GenerateTicket obj,pathname,scriptname
            MaximoUpdate
      end if
   end if
End Sub

 sub GenerateTicket(obj,filePath,fileName)
   dim dlg, result
   dim ticketDefinition, ticketSummary, ticketCategory, ticketUser, ticketAlert, ticketDrop, ticketReorg
   dim ticketSchema, ticketDB, ticketEnvironment
   dim encodeText
   set dlg = obj.CreateCustomDialog("%CurrentTargetCode%.GenerateTicket")
   result = false
   
   ticketSchema = obj.Model.GetExtendedAttribute("DefaultOwner")
   ticketDB = "DB" & cstr(obj.Model.GetExtendedAttribute("ProjectCode"))
   ticketEnvironment = obj.Model.GetExtendedAttribute("Repository")

   if inStr(ticketEnvironment, "DEV") > 0 then
      ticketEnvironment = "Development" 
   elseif inStr(ticketEnvironment, "INT") > 0 then
      ticketEnvironment = "Integration" 
   elseif inStr(ticketEnvironment, "UAT") > 0 then
      ticketEnvironment = "UAT" 
   elseif inStr(ticketEnvironment, "PROD") > 0 then
      ticketEnvironment = "Production" 
   else
      msgbox "Modelin ortam bilgisi tespit edilemedi. Lütfen VYB - Veri Mimarisi ekibi ile iletişime geçiniz."
   end if
  
   if len(UserName) = 5 then
      ticketUser = UserName
   elseif len(UserName) = 6 then
      ticketUser = UserName
   elseif len(UserName) = 7 then
      ticketUser = right(UserName, 5)
   else
      msgbox "Maximo kaydı açmaya yetkili değilsiniz. Lütfen VYB - Veri Mimarisi ekibi ile iletişime geçiniz."
   end if   
   
   if not dlg is nothing then
      dlg.EnforceCancelButton = true
      dlg.CloseButtonLabel = "Send"        
      fileText = ReadFile(filePath + fileName)
      encodeText = Encode(fileText)
      dlg.SetValue "ScriptText",fileText
      result = dlg.ShowDialog()
   end if
   
   if result = true then
      ticketCategory = dlg.GetValue("TicketCategory")
      ticketSummary = dlg.GetValue("TicketSummary")
      ticketDefinition = dlg.GetValue("TicketDefinition")
      
      if ticketCategory = "" then
         msgbox "Lüften Kategori seçiniz."
      elseif ticketSummary = "" then
         msgbox "Lüften Özet kısmını doldurunuz."
      elseif ticketDefinition = "" then
         msgbox "Lüften Açıklama kısmını doldurunuz."
      else                
         if inStr(fileText, "drop ") > 0 then
            ticketDrop= "DROP komutu içeren bir script eklenmiştir!!" + vbCrLf
         else
            ticketDrop = ""   
         end if
         
         if inStr(fileText, "drop column ") > 0 then
            ticketReorg= "DROP COLUMN var, REORG edilmelidir !!" + vbCrLf
         else
            ticketReorg = ""   
         end if
         
         ticketAlert = ticketDrop + ticketReorg
                          
         dim url
         'url = "http://kaismwast1:9080/meaweb/services/TicketWithSpec"
         url = "http://ismentegrasyon.isbank/meaweb/services/TICKETWITHSPEC"
          
         dim requestDoc, responseDoc
         set requestDoc = CreateObject("MSXML2.DOMDocument.6.0")
         set responseDoc = CreateObject("MSXML2.DOMDocument.6.0")

         dim root
         set root = requestDoc.createElement("soapenv:Envelope")
         requestDoc.appendChild root
         root.setAttribute "xmlns:soapenv", "http://schemas.xmlsoap.org/soap/envelope/"
         root.setAttribute "xmlns:max", "http://www.ibm.com/maximo"
   
         dim nodeHeader
         set nodeHeader = requestDoc.createElement("soapenv:Header")
         root.appendChild nodeHeader

         dim nodeBody
         set nodeBody = requestDoc.createElement("soapenv:Body")
         root.appendChild nodeBody

         dim nodeOp
         set nodeOp = requestDoc.createElement("max:CreateTICKETWITHSPEC")
         nodeBody.appendChild nodeOp

         dim nodeTicket
         set nodeTicket = requestDoc.createElement("max:TICKETWITHSPECSet")
         nodeOp.appendChild nodeTicket

         dim nodeSR
         set nodeSR = requestDoc.createElement("max:SR")
         nodeTicket.appendChild nodeSR

         dim nodeAttr
         set nodeAttr = requestDoc.createElement("max:AFFECTEDPERSON")
         nodeAttr.text = ticketUser
         nodeSR.appendChild nodeAttr
   
         set nodeAttr = requestDoc.createElement("max:CLASSIFICATIONID")
         nodeAttr.text = "ANA SİSTEM VERİ YÖNETİMİ HİZMETLERİ"
         nodeSR.appendChild nodeAttr
   
         set nodeAttr = requestDoc.createElement("max:CLASSSTRUCTUREID")
         nodeAttr.text = "18832"   
         nodeSR.appendChild nodeAttr
   
         Set nodeAttr = requestDoc.createElement("max:DESCRIPTION")
         nodeAttr.text = ticketCategory + " - " + ticketSummary
         nodeSR.appendChild nodeAttr
   
         set nodeAttr = requestDoc.createElement("max:DESCRIPTION_LONGDESCRIPTION")
         nodeAttr.text = "ENV: " + ticketEnvironment + vbCrLf + "DB: " + ticketDB + vbCrLf + "Schema: " + ticketSchema + vbCrLf + ticketAlert + ticketDefinition
         nodeSR.appendChild nodeAttr
         
         
         msgbox nodeAttr.text
         
         'Yeni alanlar
         set nodeAttr = requestDoc.createElement("max:TICKETSPEC")
         nodeSR.appendChild nodeAttr 
          
                 
         'set nodeAttr = requestDoc.createElement("max:ASSETATTRID")
         'nodeAttr.text = "DB2_MODEL_VERI_MIMARI_KONTROL"
         ''''''''''''''''''nodeAttr.text = "<ALNVALUE>Kontrol et</ALNVALUE><ASSETATTRID>DB2_MODEL_VERI_MIMARI_KONTROL</ASSETATTRID>"
         'nodeSR.appendChild nodeAttr
         
         'set nodeAttr = requestDoc.createElement("max:ALNVALUE")
         'nodeAttr.text = "Kontrol Edilecek."
         'nodeSR.appendChild nodeAttr
         
         'set nodeAttr = requestDoc.createElement("max:SECTION")
         'nodeAttr.text = ""
         'nodeSR.appendChild nodeAttr
         
         
         'Veri Mimarisi Kontrolü
         'dim nodeSpec
         'set nodeSpec = requestDoc.createElement("max:ASSETATTRID")
         'nodeSpec.text = "DB2_MODEL_VERI_MIMARI_KONTROL"
         'nodeAttr.appendChild nodeSpec
         
         'set nodeSpec = requestDoc.createElement("max:SECTION")
         'nodeSpec.text = ""
         'nodeAttr.appendChild nodeSpec        
        
         'set nodeSpec = requestDoc.createElement("max:ALNVALUE")
         'nodeSpec.text = "Kontrol edilecek."
         'nodeAttr.appendChild nodeSpec
         
         
         'DBA Kontrol kontrolü
         'dim nodeSpec2
         'set nodeSpec2 = requestDoc.createElement ("max:ASSETATTRID")
         'nodeSpec2.text = "DB2_MODEL_DBA_KONTROL"
         'nodeAttr.appendChild nodeSpec2
         
         
         
         'set nodeAttr = requestDoc.createElement("max:DB2_MODEL_DBA_KONTROL")
         'nodeAttr.text = ticketAlert
         'nodeSR.appendChild nodeAttr 
         'Yeni alanlar 
        
         
         set nodeAttr = requestDoc.createElement("max:IMPACT")
         nodeAttr.text = "3"
         nodeSR.appendChild nodeAttr
   
         set nodeAttr = requestDoc.createElement("max:ISENVIRONMENT")
         nodeAttr.text = ticketEnvironment
         nodeSR.appendChild nodeAttr
   
         set nodeAttr = requestDoc.createElement("max:ISREQUESTCAT")
         nodeAttr.text = "BT İçi Talepler"
         nodeSR.appendChild nodeAttr
   
         set nodeAttr = requestDoc.createElement("max:PMSCITEMNUM")
         nodeAttr.text = "ISBT0196"
         nodeSR.appendChild nodeAttr
         
         set nodeAttr = requestDoc.createElement("max:PMSCITEMSETID")
         nodeAttr.text = "ISIS1"
         nodeSR.appendChild nodeAttr         

         set nodeAttr = requestDoc.createElement("max:PMSCOFFSUMMARY")                                                      
         nodeAttr.text = "DB2 Model Talebi"
         nodeSR.appendChild nodeAttr
            
         set nodeAttr = requestDoc.createElement("max:REPORTEDBY")
         nodeAttr.text = ticketUser
         nodeSR.appendChild nodeAttr

         set nodeAttr = requestDoc.createElement("max:SOURCE")
         nodeAttr.text = "INTEGRATION"
         nodeSR.appendChild nodeAttr
         
         set nodeAttr = requestDoc.createElement("max:DOCLINKS")
         nodeSR.appendChild nodeAttr
         
         dim nodeFile
         set nodeFile = requestDoc.createElement("max:DESCRIPTION")
         nodeFile.text = "Script.sql"
         nodeAttr.appendChild nodeFile
         
         set nodeFile = requestDoc.createElement("max:DOCTYPE")
         nodeFile.text = "Attachments"
         nodeAttr.appendChild nodeFile
         
         set nodeFile = requestDoc.createElement("max:DOCUMENTDATA")
         nodeFile.text = encodeText
         nodeAttr.appendChild nodeFile
         
         set nodeFile = requestDoc.createElement("max:URLTYPE")
         nodeFile.text = "FILE"
         nodeAttr.appendChild nodeFile      
         
         set nodeFile = nothing
         set nodeAttr = nothing
         set nodeSR = nothing
         set nodeTicket = nothing
         set nodeOp = nothing
         set nodeBody = nothing
         set nodeHeader = nothing
         set root = nothing
         'EMRE-----------------------------------------------------commentle alt satırı
         'output  "sending request " & vbcrlf & requestDoc.xml
         'EMRE
         dim xmlhttp
         set xmlhttp = CreateObject("MSXML2.ServerXMLHTTP.6.0")
         'xmlhttp.Open "POST", url, false, "maxadmin", "maxuat"
         xmlhttp.Open "POST", url, false, "powerdesignerusr", "po88OhhSr"
         xmlhttp.setRequestHeader "Content-Type", "text/xml"
   
         'set SOAPAction as appropriate for the operation '
         xmlhttp.setRequestHeader "SOAPAction", "urn:processDocument"
         xmlhttp.send requestDoc.xml
         
         'output "ilki geliyo"
         'output vbcrlf & "Raw XML response:" & vbcrlf 
         'output xmlhttp.responseXML.xml
         
         responseDoc.LoadXML xmlhttp.responseXML.xml
       
         SRNumber =replace(responseDoc.text, "SR", "")
   
         if responseDoc.parseError.errorCode <> 0 Then 'parser error found 
            msgbox "Maximo kaydı açılamadı. Lütfen VYB - Veri Mimarisi ekibi ile iletişime geçiniz."
         else
            msgbox replace(responseDoc.text, "SR", "") + " nolu hizmet talebiniz açılmıştır."
         end if
      end if   
   end if
end sub



sub MaximoUpdate
         
         dim url
         url = "http://kaismwas01:9080/meaweb/services/TICKETWITHSPEC"
         'url = "http://ismentegrasyon.isbank/meaweb/services/TICKETWITHSPEC"
           
         dim requestDoc, responseDoc
         set requestDoc = CreateObject("MSXML2.DOMDocument.6.0")
         set responseDoc = CreateObject("MSXML2.DOMDocument.6.0")

         dim root
         set root = requestDoc.createElement("soapenv:Envelope")
         requestDoc.appendChild root
         root.setAttribute "xmlns:soapenv", "http://schemas.xmlsoap.org/soap/envelope/"
         root.setAttribute "xmlns:max", "http://www.ibm.com/maximo"

         dim nodeHeader
         set nodeHeader = requestDoc.createElement("soapenv:Header")
         root.appendChild nodeHeader
         
         dim nodeBody
         set nodeBody = requestDoc.createElement("soapenv:Body")
         root.appendChild nodeBody

         dim nodeOp
         set nodeOp = requestDoc.createElement("max:SyncTICKETWITHSPEC")
         nodeBody.appendChild nodeOp

         dim nodeTicket
         set nodeTicket = requestDoc.createElement("max:TICKETWITHSPECSet")
         nodeOp.appendChild nodeTicket
         
         dim nodeSR
         set nodeSR = requestDoc.createElement("max:SR")
         nodeSR.setAttribute "action", "Change"
		   nodeTicket.appendChild nodeSR
           
         
         'Veri Mimarisi Kontrolü
         VMCheck = ""  
    
         if CheckWord("create table ","maxpartitions 200") then
          'output "hasan birinci kontrol"
            VMCheck = "kontrol edilecek"      
         elseif CheckWord("create index","defer no") then
          'output "hasan ikinci kontrol"
           VMCheck = "kontrol edilecek" 
         else
           VMCheck = ""  
         end if
                     
         dim nodeFile
         set nodeFile = requestDoc.createElement("max:TICKETID")
         nodeFile.setAttribute "changed", "true"
         nodeSR.appendChild nodeFile
         nodeFile.text = SRNumber
		 
         dim nodeClass         
         set nodeClass = requestDoc.createElement("max:CLASS")
         nodeClass.setAttribute "changed", "true"
         nodeSR.appendChild nodeClass
         nodeClass.text = "SR"   
         
         dim nodeSpec         
         set nodeSpec = requestDoc.createElement("max:TICKETSPEC")
         nodeSpec.setAttribute "action", "Change"
         nodeSR.appendChild nodeSpec
         
         dim nodeALN
         set nodeALN = requestDoc.createElement("max:ALNVALUE")
         nodeALN.setAttribute "changed", "true"
         nodeSpec.appendChild nodeALN
         nodeALN.text = VMCheck
         
         dim nodeAsset           
         set nodeAsset = requestDoc.createElement("max:ASSETATTRID")
         nodeAsset.setAttribute "changed", "false"
         nodeSpec.appendChild nodeAsset
         nodeAsset.text = "DB2_MODEL_VERI_MIMARI_KONTROL"
         
         dim nodeSection
         set nodeSection = requestDoc.createElement("max:SECTION")
         nodeSpec.appendChild nodeSection
         nodeSection.setAttribute "changed", "false"
         
         'set nodeSpec = requestDoc.createElement("max:SECTION")
         'nodeSpec.text = ""
         'nodeAttr.appendChild nodeSpec        


         'DBA Kontrolü
         DBACheck = ""  
                 
         set nodeSpec = requestDoc.createElement("max:TICKETSPEC")
         nodeSpec.setAttribute "action", "Change"
         nodeSR.appendChild nodeSpec
         
         set nodeALN = requestDoc.createElement("max:ALNVALUE")
         nodeALN.setAttribute "changed", "true"
         nodeSpec.appendChild nodeALN
         nodeALN.text = DBACheck   
                  
         set nodeAsset = requestDoc.createElement("max:ASSETATTRID")
         nodeAsset.setAttribute "changed", "false"
         nodeSpec.appendChild nodeAsset
         nodeAsset.text = "DB2_MODEL_DBA_KONTROL"
         
         set nodeSection = requestDoc.createElement("max:SECTION")
         nodeSpec.appendChild nodeSection
         nodeSection.setAttribute "changed", "false"
         

         dim xmlhttp
         set xmlhttp = CreateObject("MSXML2.ServerXMLHTTP.6.0")
         'xmlhttp.Open "POST", url, false, "maxadmin", "maxuat"
         xmlhttp.Open "POST", url, false, "powerdesignerusr", "po88OhhSr"
         xmlhttp.setRequestHeader "Content-Type", "text/xml"

   
         'set SOAPAction as appropriate for the operation '
         xmlhttp.setRequestHeader "SOAPAction", "urn:processDocument"
         xmlhttp.send requestDoc.xml
         'output requestDoc.xml & xmlhttp.send 
         
         'output vbcrlf & "Raw XML response:" & vbcrlf 
         'output xmlhttp.responseXML.xml

         responseDoc.LoadXML xmlhttp.responseXML.xml  
         
         'output "update geliyo"
         'output  "update request " & vbcrlf & requestDoc.xml
         
         SRNumber = ""
           
end sub

function CheckWord(word1, word2)
         'ilk kelimeyi scriptte sayar ve counter1 olarak sayiyi belirler
         dim pose1
         pose1=1
         dim counter1
         counter1=0
         while pose1 <> 0
         pose1= pose1 +1
         pose1 = inStr(pose1,fileText,word1)
         'pose1 = inStr(pose1,"hasan test1 test2 basri test1 test2 tokgoz test1 test2",word1)
         'output "hasan pose 1: "&pose1
         if pose1 <> 0 Then
            counter1 = counter1 +1
         end if
         wend
        
         'ikinci kelimeyi scriptte sayar ve counter2 olarak sayiyi belirler  
         dim pose2
         pose2=1
         dim counter2
         counter2=0
         while pose2 <> 0
         pose2= pose2 +1
         pose2 = inStr(pose2,fileText,word2)
         'pose2 = inStr(pose2,"hasan test1 test2 basri test1 test2 tokgoz test1 test",word2)
         'output "hasan pose 2: "&pose2
         if pose2 <> 0 Then
            counter2 = counter2 +1
         end if
         wend
         'output "hasan: "& counter1
         'output "hasan: "& counter2
         'kelimelerin tekrar sayılarının eşit olup olmamasına göre boolean değer döner, eğer eşit değilse true döner
         if counter1 = counter2 then
            CheckWord=False
         else 
            CheckWord=True
         end if                
         
end function

function Encode(sText)
   Dim oXML, oNode

   Set oXML = CreateObject("MSXML2.DOMDocument.6.0")
   Set oNode = oXML.CreateElement("base64")

   oNode.dataType = "bin.base64"
   oNode.nodeTypedValue = StringToBinary(sText)    
   Encode = oNode.text

   Set oNode = Nothing
   Set oXML = Nothing
end function

function StringToBinary(Text)
   const adTypeText = 2
   const adTypeBinary = 1

   'Create Stream object
   dim BinaryStream 'As New Stream
   set BinaryStream = CreateObject("ADODB.Stream")

   'Specify stream type - we want To save text/string data.
   BinaryStream.Type = adTypeText

   'Specify charset For the source text (unicode) data.
   BinaryStream.CharSet = "us-ascii"

   'Open the stream And write text/string data To the object
   BinaryStream.Open
   BinaryStream.WriteText Text

   'Change stream type To binary
   BinaryStream.Position = 0
   BinaryStream.Type = adTypeBinary

   'Ignore first two bytes - sign of
   BinaryStream.Position = 0

   'Open the stream And get binary data from the object
   StringToBinary = BinaryStream.Read

   set BinaryStream = nothing
end function
