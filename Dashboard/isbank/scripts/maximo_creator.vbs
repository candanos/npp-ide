' {"rowstamp":"7692564375","AFFECTEDEMAIL":"Candan.Yuksel@softtech.com.tr","CLASS":"SR","CLASSIFICATIONID":"DONANIM TALEPLERI","CLASSSTRUCTUREID":"18655","CREATEDBY":"59857","CREATIONDATE":"2019-09-05T12:57:12+03:00","CUSTTALEPTIPI":"Softtech Citrix Eri\u015fim Talebi","DESCRIPTION":"Softtech Citrix Eri\u015fim Talebi","REPORTDATE":"2019-09-05T12:57:46+03:00","REPORTEDBY":"59857","STATUS":"HAZIR","STATUSDATE":"2019-09-05T12:57:45+03:00","TICKETID":"H7151489","TICKETUID":13993701}

' {"NEW":1,"ONAY1BEK":11,"ONAY2BEK":12,"NOCONTACT":4902,"TEKRARAMA":3,"CANCELLED":1629,"COMPLETE":50766,"BEKLEMEDE":33,"REDDEDILDI":538,"RESOLVED":307,"UNRESOLVED":1888,"INPROG":299,"HAZIR":1}


   msgbox "here we go."
   ticketUser = "59857"
   dim dlg, result
   dim ticketDefinition, ticketSummary, ticketCategory, ticketUser, ticketAlert, ticketDrop, ticketReorg
   dim ticketSchema, ticketDB, ticketEnvironment
   dim encodeText                       
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
    nodeSR.setAttribute "action", "Change"
	nodeTicket.appendChild nodeSR
	
    dim nodeAttr
    set nodeAttr = requestDoc.createElement("max:AFFECTEDPERSON")
    nodeAttr.text = "59857"
    nodeSR.appendChild nodeAttr
	
    set nodeAttr = requestDoc.createElement("max:CLASSIFICATIONID")
    nodeAttr.text = "DONANIM TALEPLERI"
    nodeSR.appendChild nodeAttr
	
	set nodeAttr = requestDoc.createElement("max:ISREQUESTCAT")
    nodeAttr.text = "Teknik Çaðrý, Arýzalar"
    nodeSR.appendChild nodeAttr
	
    set nodeAttr = requestDoc.createElement("max:CLASSSTRUCTUREID")
    nodeAttr.text = "18655"   
    nodeSR.appendChild nodeAttr
	
    Set nodeAttr = requestDoc.createElement("max:DESCRIPTION")
    nodeAttr.text = "Softtech Citrix Eriþim Talebi"
    nodeSR.appendChild nodeAttr

    Set nodeAttr = requestDoc.createElement("max:CUSTTALEPTIPI")
    nodeAttr.text = "Softtech Citrix Eriþim Talebi"
    nodeSR.appendChild nodeAttr
	
    set nodeAttr = requestDoc.createElement("max:DESCRIPTION_LONGDESCRIPTION")
    nodeAttr.text = "Softtech Citrix Eriþim Talebi"
    nodeSR.appendChild nodeAttr
    
	set nodeAttr = requestDoc.createElement("max:SOURCE")
    nodeAttr.text = "KATALOG"
    nodeSR.appendChild nodeAttr 
	
	set nodeAttr = requestDoc.createElement("max:IMPACT")
    nodeAttr.text = "3"
    nodeSR.appendChild nodeAttr
	
	set nodeAttr = requestDoc.createElement("max:PMSCCRID")
    nodeAttr.text = "3066656"
    nodeSR.appendChild nodeAttr
	
	set nodeAttr = requestDoc.createElement("max:REPORTEDBY")
    nodeAttr.text = ticketUser
    nodeSR.appendChild nodeAttr
	
	set nodeAttr = requestDoc.createElement("max:REPORTEDEMAIL")
    nodeAttr.text = "Candan.Yuksel@softtech.com.tr"
    nodeSR.appendChild nodeAttr
	
	
    dim xmlhttp
    set xmlhttp = CreateObject("MSXML2.ServerXMLHTTP.6.0")
    'xmlhttp.Open "POST", url, false, "maxadmin", "maxuat"
	
	msgbox "we are at the door."
    xmlhttp.Open "POST", url, false, "59857", "Os121212"
    xmlhttp.setRequestHeader "Content-Type", "text/xml;charset=UTF-8"
	
    'set SOAPAction as appropriate for the operation '
    xmlhttp.setRequestHeader "SOAPAction", "urn:processDocument"
    xmlhttp.send requestDoc.xml
    
	msgbox requestDoc.xml
    'output "ilki geliyo"
    'output vbcrlf & "Raw XML response:" & vbcrlf 
    'output xmlhttp.responseXML.xml
    
    responseDoc.LoadXML xmlhttp.responseXML.xml
	
	msgbox responseDoc.text 
    SRNumber =replace(responseDoc.text, "SR", "")
	
    if responseDoc.parseError.errorCode <> 0 Then 'parser error found 
       msgbox "Maximo kaydý açýlamadý."
    else
       msgbox replace(responseDoc.text, "SR", "") + " nolu hizmet talebiniz açýlmýþtýr."
    end if