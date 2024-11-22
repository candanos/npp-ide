DCN: D-19659-94
Items: 24645743, 24704157

get 'T660T.T659BS.G2262V00' C:\temp\T659BS_241105.txt

INC107308014 D1955969 DM:24634975 10.03
grep -rl D1955969 /app/mqft/dcnevent_files_done --include=DCNEVENT_241003*
/app/mqft/dcnevent_files_done/DCNEVENT_241003.063130.xml
/app/mqft/dcnevent_files_done/DCNEVENT_241003.070559.xml
/app/mqft/dcnevent_files_done/DCNEVENT_241003.070620.xml

grep -rl D1955969 /app/mqft/dcnevent_files_done --include=DCNEVENT_241003* | xargs grep -rl 24634975

<?xml version="1.0"?>
<ns2:SyncEventElementFreeze xmlns:ns3="http://www.volvo.com/group/common/1_0" xmlns:ns2="http://www.volvo.com/kola/sync_dcn_event/1_0">
  <ns3:ApplicationArea>
    <ns3:Sender>
      <ns3:LogicalID>KOLA</ns3:LogicalID>
    </ns3:Sender>
    <ns3:CreationDateTime>2024-10-03T06:31:21.040</ns3:CreationDateTime>
    <ns3:BODID>0e15e214-3bce-4f2c-a70f-05fdd3ee7b21</ns3:BODID>
  </ns3:ApplicationArea>
  <ns2:DataArea>
    <ns2:Sync/>
    <ns2:DcnEventFreeze>
      <ns2:MessageType>FREEZE</ns2:MessageType>
      <ns2:DesignChangeNote>
        <ns2:DCNNumber>D1955969</ns2:DCNNumber>
        <ns2:DCNType>3</ns2:DCNType>
      </ns2:DesignChangeNote>
      <ns2:UserId>A483322</ns2:UserId>
      <ns2:Reviewers>
        <ns2:Reviewer>
          <ns2:UserID>A443258</ns2:UserID>
          <ns2:MailOrderType>DCNCAD</ns2:MailOrderType>
        </ns2:Reviewer>
        <ns2:Reviewer>
          <ns2:UserID>A443258</ns2:UserID>
          <ns2:MailOrderType>DCNCHECK</ns2:MailOrderType>
        </ns2:Reviewer>
        <ns2:Reviewer>
          <ns2:UserID>T0C0865</ns2:UserID>
          <ns2:MailOrderType>DCNDEPT</ns2:MailOrderType>
        </ns2:Reviewer>
        <ns2:Reviewer>
          <ns2:UserID>A359074</ns2:UserID>
          <ns2:MailOrderType>DCNFUNC</ns2:MailOrderType>
        </ns2:Reviewer>
        <ns2:Reviewer>
          <ns2:UserID>A333367</ns2:UserID>
          <ns2:MailOrderType>DCNGROUP</ns2:MailOrderType>
        </ns2:Reviewer>
        <ns2:Reviewer>
          <ns2:UserID>T0C0865</ns2:UserID>
          <ns2:MailOrderType>DCNLEGAL</ns2:MailOrderType>
        </ns2:Reviewer>
        <ns2:Reviewer>
          <ns2:UserID>A333367</ns2:UserID>
          <ns2:MailOrderType>DCNRESPE</ns2:MailOrderType>
        </ns2:Reviewer>
        <ns2:Reviewer>
          <ns2:UserID>A398924</ns2:UserID>
          <ns2:MailOrderType>DCNRESPE</ns2:MailOrderType>
        </ns2:Reviewer>
        <ns2:Reviewer>
          <ns2:UserID>A483322</ns2:UserID>
          <ns2:MailOrderType>FREEZE</ns2:MailOrderType>
        </ns2:Reviewer>
      </ns2:Reviewers>
      <ns2:Company>7</ns2:Company>
      <ns2:TimeStamp>2024100306312140</ns2:TimeStamp>
      <ns2:ToC>
        <ns2:item>
          <ns2:ItemCategory>Part</ns2:ItemCategory>
          <ns2:ItemNumber>24621885</ns2:ItemNumber>
          <ns2:ItemType id="D"/>
          <ns2:Version>02</ns2:Version>
          <ns2:Rejected>false</ns2:Rejected>
          <ns2:DesignStage>C</ns2:DesignStage>
          <ns2:MasterSystem>KOLA</ns2:MasterSystem>
          <ns2:Bridges>
            <ns2:Bridge>
              <ns2:ExternalName>24621885-WTPart</ns2:ExternalName>
              <ns2:ExternalVersion>3</ns2:ExternalVersion>
              <ns2:ExternalVault>01</ns2:ExternalVault>
              <ns2:BridgeStatus>2</ns2:BridgeStatus>
              <ns2:ExternalObject>wt.part.WTPartMaster:79981176814|981783618-1249579887230-31922233-43-20-97-131|pdmlink.got.volvo.net</ns2:ExternalObject>
            </ns2:Bridge>
          </ns2:Bridges>
        </ns2:item>
        <ns2:item>
          <ns2:ItemCategory>Part</ns2:ItemCategory>
          <ns2:ItemNumber>24634959</ns2:ItemNumber>
          <ns2:ItemType id="D"/>
          <ns2:Version>02</ns2:Version>
          <ns2:Rejected>false</ns2:Rejected>
          <ns2:DesignStage>C</ns2:DesignStage>
          <ns2:MasterSystem>KOLA</ns2:MasterSystem>
          <ns2:Bridges>
            <ns2:Bridge>
              <ns2:ExternalName>24634959-WTPart</ns2:ExternalName>
              <ns2:ExternalVersion>2</ns2:ExternalVersion>
              <ns2:ExternalVault>01</ns2:ExternalVault>
              <ns2:BridgeStatus>2</ns2:BridgeStatus>
              <ns2:ExternalObject>wt.part.WTPartMaster:80362316442|981783618-1249579887230-31922233-43-20-97-131|pdmlink.got.volvo.net</ns2:ExternalObject>
            </ns2:Bridge>
          </ns2:Bridges>
        </ns2:item>
        <ns2:item>
          <ns2:ItemCategory>Part</ns2:ItemCategory>
          <ns2:ItemNumber>24634967</ns2:ItemNumber>
          <ns2:ItemType id="K"/>
          <ns2:Version>02</ns2:Version>
          <ns2:Rejected>false</ns2:Rejected>
          <ns2:DesignStage>C</ns2:DesignStage>
          <ns2:MasterSystem>KOLA</ns2:MasterSystem>
          <ns2:Bridges>
            <ns2:Bridge>
              <ns2:ExternalName>24634967-WTPart</ns2:ExternalName>
              <ns2:ExternalVersion>4</ns2:ExternalVersion>
              <ns2:ExternalVault>01</ns2:ExternalVault>
              <ns2:BridgeStatus>2</ns2:BridgeStatus>
              <ns2:ExternalObject>wt.part.WTPartMaster:80518344096|981783618-1249579887230-31922233-43-20-97-131|pdmlink.got.volvo.net</ns2:ExternalObject>
            </ns2:Bridge>
          </ns2:Bridges>
        </ns2:item>
        <ns2:item>
          <ns2:ItemCategory>Part</ns2:ItemCategory>
          <ns2:ItemNumber>24634975</ns2:ItemNumber>
          <ns2:ItemType id="K"/>
          <ns2:Version>02</ns2:Version>
          <ns2:Rejected>false</ns2:Rejected>
          <ns2:DesignStage>C</ns2:DesignStage>
          <ns2:MasterSystem>KOLA</ns2:MasterSystem>
          <ns2:Bridges>
            <ns2:Bridge>
              <ns2:ExternalName>24634975-WTPart</ns2:ExternalName>
              <ns2:ExternalVersion>3</ns2:ExternalVersion>
              <ns2:ExternalVault>01</ns2:ExternalVault>
              <ns2:BridgeStatus>2</ns2:BridgeStatus>
              <ns2:ExternalObject>wt.part.WTPartMaster:80415865722|981783618-1249579887230-31922233-43-20-97-131|pdmlink.got.volvo.net</ns2:ExternalObject>
            </ns2:Bridge>
          </ns2:Bridges>
        </ns2:item>
        <ns2:item>
          <ns2:ItemCategory>Part</ns2:ItemCategory>
          <ns2:ItemNumber>24636704</ns2:ItemNumber>
          <ns2:ItemType id="D"/>
          <ns2:Version>02</ns2:Version>
          <ns2:Rejected>false</ns2:Rejected>
          <ns2:DesignStage>C</ns2:DesignStage>
          <ns2:MasterSystem>KOLA</ns2:MasterSystem>
          <ns2:Bridges>
            <ns2:Bridge>
              <ns2:ExternalName>24636704-WTPart</ns2:ExternalName>
              <ns2:ExternalVersion>2</ns2:ExternalVersion>
              <ns2:ExternalVault>01</ns2:ExternalVault>
              <ns2:BridgeStatus>2</ns2:BridgeStatus>
              <ns2:ExternalObject>wt.part.WTPartMaster:80979413387|981783618-1249579887230-31922233-43-20-97-131|pdmlink.got.volvo.net</ns2:ExternalObject>
            </ns2:Bridge>
          </ns2:Bridges>
        </ns2:item>
        <ns2:item>
          <ns2:ItemCategory>Part</ns2:ItemCategory>
          <ns2:ItemNumber>24636734</ns2:ItemNumber>
          <ns2:ItemType id="D"/>
          <ns2:Version>02</ns2:Version>
          <ns2:Rejected>false</ns2:Rejected>
          <ns2:DesignStage>C</ns2:DesignStage>
          <ns2:MasterSystem>KOLA</ns2:MasterSystem>
          <ns2:Bridges>
            <ns2:Bridge>
              <ns2:ExternalName>24636734-WTPart</ns2:ExternalName>
              <ns2:ExternalVersion>3</ns2:ExternalVersion>
              <ns2:ExternalVault>01</ns2:ExternalVault>
              <ns2:BridgeStatus>2</ns2:BridgeStatus>
              <ns2:ExternalObject>wt.part.WTPartMaster:80518297695|981783618-1249579887230-31922233-43-20-97-131|pdmlink.got.volvo.net</ns2:ExternalObject>
            </ns2:Bridge>
          </ns2:Bridges>
        </ns2:item>
        <ns2:item>
          <ns2:ItemCategory>Part</ns2:ItemCategory>
          <ns2:ItemNumber>24637103</ns2:ItemNumber>
          <ns2:ItemType id="D"/>
          <ns2:Version>02</ns2:Version>
          <ns2:Rejected>false</ns2:Rejected>
          <ns2:DesignStage>C</ns2:DesignStage>
          <ns2:MasterSystem>KOLA</ns2:MasterSystem>
          <ns2:Bridges>
            <ns2:Bridge>
              <ns2:ExternalName>24637103-WTPart</ns2:ExternalName>
              <ns2:ExternalVersion>3</ns2:ExternalVersion>
              <ns2:ExternalVault>01</ns2:ExternalVault>
              <ns2:BridgeStatus>2</ns2:BridgeStatus>
              <ns2:ExternalObject>wt.part.WTPartMaster:80390326469|981783618-1249579887230-31922233-43-20-97-131|pdmlink.got.volvo.net</ns2:ExternalObject>
            </ns2:Bridge>
          </ns2:Bridges>
        </ns2:item>
        <ns2:item>
          <ns2:ItemCategory>Part</ns2:ItemCategory>
          <ns2:ItemNumber>24637106</ns2:ItemNumber>
          <ns2:ItemType id="D"/>
          <ns2:Version>02</ns2:Version>
          <ns2:Rejected>false</ns2:Rejected>
          <ns2:DesignStage>C</ns2:DesignStage>
          <ns2:MasterSystem>KOLA</ns2:MasterSystem>
          <ns2:Bridges>
            <ns2:Bridge>
              <ns2:ExternalName>24637106-WTPart</ns2:ExternalName>
              <ns2:ExternalVersion>3</ns2:ExternalVersion>
              <ns2:ExternalVault>01</ns2:ExternalVault>
              <ns2:BridgeStatus>2</ns2:BridgeStatus>
              <ns2:ExternalObject>wt.part.WTPartMaster:80965003390|981783618-1249579887230-31922233-43-20-97-131|pdmlink.got.volvo.net</ns2:ExternalObject>
            </ns2:Bridge>
          </ns2:Bridges>
        </ns2:item>
        <ns2:item>
          <ns2:ItemCategory>Part</ns2:ItemCategory>
          <ns2:ItemNumber>24637109</ns2:ItemNumber>
          <ns2:ItemType id="D"/>
          <ns2:Version>02</ns2:Version>
          <ns2:Rejected>false</ns2:Rejected>
          <ns2:DesignStage>C</ns2:DesignStage>
          <ns2:MasterSystem>KOLA</ns2:MasterSystem>
          <ns2:Bridges>
            <ns2:Bridge>
              <ns2:ExternalName>24637109-WTPart</ns2:ExternalName>
              <ns2:ExternalVersion>2</ns2:ExternalVersion>
              <ns2:ExternalVault>01</ns2:ExternalVault>
              <ns2:BridgeStatus>2</ns2:BridgeStatus>
              <ns2:ExternalObject>wt.part.WTPartMaster:80390333259|981783618-1249579887230-31922233-43-20-97-131|pdmlink.got.volvo.net</ns2:ExternalObject>
            </ns2:Bridge>
          </ns2:Bridges>
        </ns2:item>
        <ns2:item>
          <ns2:ItemCategory>Part</ns2:ItemCategory>
          <ns2:ItemNumber>24637117</ns2:ItemNumber>
          <ns2:ItemType id="E"/>
          <ns2:Version>02</ns2:Version>
          <ns2:Rejected>false</ns2:Rejected>
          <ns2:DesignStage>C</ns2:DesignStage>
          <ns2:MasterSystem>KOLA</ns2:MasterSystem>
          <ns2:Bridges>
            <ns2:Bridge>
              <ns2:ExternalName>24637117.asm</ns2:ExternalName>
              <ns2:ExternalVersion>2</ns2:ExternalVersion>
              <ns2:ExternalVault>01</ns2:ExternalVault>
              <ns2:BridgeStatus>2</ns2:BridgeStatus>
              <ns2:ExternalObject>wt.epm.EPMDocumentMaster:80390683006|981783618-1249579887230-31922233-43-20-97-131|pdmlink.got.volvo.net</ns2:ExternalObject>
            </ns2:Bridge>
          </ns2:Bridges>
        </ns2:item>
        <ns2:item>
          <ns2:ItemCategory>Part</ns2:ItemCategory>
          <ns2:ItemNumber>24637257</ns2:ItemNumber>
          <ns2:ItemType id="D"/>
          <ns2:Version>02</ns2:Version>
          <ns2:Rejected>false</ns2:Rejected>
          <ns2:DesignStage>C</ns2:DesignStage>
          <ns2:MasterSystem>KOLA</ns2:MasterSystem>
          <ns2:Bridges>
            <ns2:Bridge>
              <ns2:ExternalName>24637257-WTPart</ns2:ExternalName>
              <ns2:ExternalVersion>3</ns2:ExternalVersion>
              <ns2:ExternalVault>01</ns2:ExternalVault>
              <ns2:BridgeStatus>2</ns2:BridgeStatus>
              <ns2:ExternalObject>wt.part.WTPartMaster:80389577549|981783618-1249579887230-31922233-43-20-97-131|pdmlink.got.volvo.net</ns2:ExternalObject>
            </ns2:Bridge>
          </ns2:Bridges>
        </ns2:item>
        <ns2:item>
          <ns2:ItemCategory>Part</ns2:ItemCategory>
          <ns2:ItemNumber>24643646</ns2:ItemNumber>
          <ns2:ItemType id="E"/>
          <ns2:Version>02</ns2:Version>
          <ns2:Rejected>false</ns2:Rejected>
          <ns2:DesignStage>C</ns2:DesignStage>
          <ns2:MasterSystem>KOLA</ns2:MasterSystem>
          <ns2:Bridges>
            <ns2:Bridge>
              <ns2:ExternalName>24643646.asm</ns2:ExternalName>
              <ns2:ExternalVersion>2</ns2:ExternalVersion>
              <ns2:ExternalVault>01</ns2:ExternalVault>
              <ns2:BridgeStatus>2</ns2:BridgeStatus>
              <ns2:ExternalObject>wt.epm.EPMDocumentMaster:80754135215|981783618-1249579887230-31922233-43-20-97-131|pdmlink.got.volvo.net</ns2:ExternalObject>
            </ns2:Bridge>
          </ns2:Bridges>
        </ns2:item>
        <ns2:item>
          <ns2:ItemCategory>Document</ns2:ItemCategory>
          <ns2:ItemNumber>24621884</ns2:ItemNumber>
          <ns2:ItemType id="R"/>
          <ns2:Version>02</ns2:Version>
          <ns2:Rejected>false</ns2:Rejected>
          <ns2:MasterSystem>KOLA</ns2:MasterSystem>
          <ns2:Bridges>
            <ns2:Bridge>
              <ns2:ExternalName>24621884.drw</ns2:ExternalName>
              <ns2:ExternalVersion>2</ns2:ExternalVersion>
              <ns2:ExternalVault>01</ns2:ExternalVault>
              <ns2:BridgeStatus>2</ns2:BridgeStatus>
              <ns2:ExternalObject>wt.epm.EPMDocumentMaster:79823846278|981783618-1249579887230-31922233-43-20-97-131|pdmlink.got.volvo.net</ns2:ExternalObject>
            </ns2:Bridge>
          </ns2:Bridges>
        </ns2:item>
        <ns2:item>
          <ns2:ItemCategory>Document</ns2:ItemCategory>
          <ns2:ItemNumber>24634958</ns2:ItemNumber>
          <ns2:ItemType id="R"/>
          <ns2:Version>02</ns2:Version>
          <ns2:Rejected>false</ns2:Rejected>
          <ns2:MasterSystem>KOLA</ns2:MasterSystem>
          <ns2:Bridges>
            <ns2:Bridge>
              <ns2:ExternalName>24634958.drw</ns2:ExternalName>
              <ns2:ExternalVersion>2</ns2:ExternalVersion>
              <ns2:ExternalVault>01</ns2:ExternalVault>
              <ns2:BridgeStatus>2</ns2:BridgeStatus>
              <ns2:ExternalObject>wt.epm.EPMDocumentMaster:80631685561|981783618-1249579887230-31922233-43-20-97-131|pdmlink.got.volvo.net</ns2:ExternalObject>
            </ns2:Bridge>
          </ns2:Bridges>
        </ns2:item>
        <ns2:item>
          <ns2:ItemCategory>Document</ns2:ItemCategory>
          <ns2:ItemNumber>24634966</ns2:ItemNumber>
          <ns2:ItemType id="R"/>
          <ns2:Version>02</ns2:Version>
          <ns2:Rejected>false</ns2:Rejected>
          <ns2:MasterSystem>KOLA</ns2:MasterSystem>
          <ns2:Bridges>
            <ns2:Bridge>
              <ns2:ExternalName>24634966.drw</ns2:ExternalName>
              <ns2:ExternalVersion>2</ns2:ExternalVersion>
              <ns2:ExternalVault>01</ns2:ExternalVault>
              <ns2:BridgeStatus>2</ns2:BridgeStatus>
              <ns2:ExternalObject>wt.epm.EPMDocumentMaster:80612896203|981783618-1249579887230-31922233-43-20-97-131|pdmlink.got.volvo.net</ns2:ExternalObject>
            </ns2:Bridge>
          </ns2:Bridges>
        </ns2:item>
        <ns2:item>
          <ns2:ItemCategory>Document</ns2:ItemCategory>
          <ns2:ItemNumber>24634974</ns2:ItemNumber>
          <ns2:ItemType id="R"/>
          <ns2:Version>02</ns2:Version>
          <ns2:Rejected>false</ns2:Rejected>
          <ns2:MasterSystem>KOLA</ns2:MasterSystem>
          <ns2:Bridges>
            <ns2:Bridge>
              <ns2:ExternalName>24634974.drw</ns2:ExternalName>
              <ns2:ExternalVersion>2</ns2:ExternalVersion>
              <ns2:ExternalVault>01</ns2:ExternalVault>
              <ns2:BridgeStatus>2</ns2:BridgeStatus>
              <ns2:ExternalObject>wt.epm.EPMDocumentMaster:80484968432|981783618-1249579887230-31922233-43-20-97-131|pdmlink.got.volvo.net</ns2:ExternalObject>
            </ns2:Bridge>
          </ns2:Bridges>
        </ns2:item>
        <ns2:item>
          <ns2:ItemCategory>DigitalModel</ns2:ItemCategory>
          <ns2:ItemNumber>24621885</ns2:ItemNumber>
          <ns2:ItemType id="2"/>
          <ns2:Version>02</ns2:Version>
          <ns2:Rejected>false</ns2:Rejected>
          <ns2:MasterSystem>KOLA</ns2:MasterSystem>
          <ns2:Bridges>
            <ns2:Bridge>
              <ns2:ExternalName>24621885.prt</ns2:ExternalName>
              <ns2:ExternalVersion>2</ns2:ExternalVersion>
              <ns2:ExternalVault>01</ns2:ExternalVault>
              <ns2:BridgeStatus>2</ns2:BridgeStatus>
              <ns2:ExternalObject>wt.epm.EPMDocumentMaster:79749870858|981783618-1249579887230-31922233-43-20-97-131|pdmlink.got.volvo.net</ns2:ExternalObject>
            </ns2:Bridge>
          </ns2:Bridges>
        </ns2:item>
        <ns2:item>
          <ns2:ItemCategory>DigitalModel</ns2:ItemCategory>
          <ns2:ItemNumber>24634959</ns2:ItemNumber>
          <ns2:ItemType id="2"/>
          <ns2:Version>02</ns2:Version>
          <ns2:Rejected>false</ns2:Rejected>
          <ns2:MasterSystem>KOLA</ns2:MasterSystem>
          <ns2:Bridges>
            <ns2:Bridge>
              <ns2:ExternalName>24634959.prt</ns2:ExternalName>
              <ns2:ExternalVersion>2</ns2:ExternalVersion>
              <ns2:ExternalVault>01</ns2:ExternalVault>
              <ns2:BridgeStatus>2</ns2:BridgeStatus>
              <ns2:ExternalObject>wt.epm.EPMDocumentMaster:80362275364|981783618-1249579887230-31922233-43-20-97-131|pdmlink.got.volvo.net</ns2:ExternalObject>
            </ns2:Bridge>
          </ns2:Bridges>
        </ns2:item>
        <ns2:item>
          <ns2:ItemCategory>DigitalModel</ns2:ItemCategory>
          <ns2:ItemNumber>24634967</ns2:ItemNumber>
          <ns2:ItemType id="2"/>
          <ns2:Version>02</ns2:Version>
          <ns2:Rejected>false</ns2:Rejected>
          <ns2:MasterSystem>KOLA</ns2:MasterSystem>
          <ns2:Bridges>
            <ns2:Bridge>
              <ns2:ExternalName>24634967.asm</ns2:ExternalName>
              <ns2:ExternalVersion>3</ns2:ExternalVersion>
              <ns2:ExternalVault>01</ns2:ExternalVault>
              <ns2:BridgeStatus>2</ns2:BridgeStatus>
              <ns2:ExternalObject>wt.epm.EPMDocumentMaster:80383968203|981783618-1249579887230-31922233-43-20-97-131|pdmlink.got.volvo.net</ns2:ExternalObject>
            </ns2:Bridge>
          </ns2:Bridges>
        </ns2:item>
        <ns2:item>
          <ns2:ItemCategory>DigitalModel</ns2:ItemCategory>
          <ns2:ItemNumber>24634975</ns2:ItemNumber>
          <ns2:ItemType id="2"/>
          <ns2:Version>02</ns2:Version>
          <ns2:Rejected>false</ns2:Rejected>
          <ns2:MasterSystem>KOLA</ns2:MasterSystem>
          <ns2:Bridges>
            <ns2:Bridge>
              <ns2:ExternalName>24634975.asm</ns2:ExternalName>
              <ns2:ExternalVersion>3</ns2:ExternalVersion>
              <ns2:ExternalVault>01</ns2:ExternalVault>
              <ns2:BridgeStatus>2</ns2:BridgeStatus>
              <ns2:ExternalObject>wt.epm.EPMDocumentMaster:80384169986|981783618-1249579887230-31922233-43-20-97-131|pdmlink.got.volvo.net</ns2:ExternalObject>
            </ns2:Bridge>
          </ns2:Bridges>
        </ns2:item>
        <ns2:item>
          <ns2:ItemCategory>DigitalModel</ns2:ItemCategory>
          <ns2:ItemNumber>24636704</ns2:ItemNumber>
          <ns2:ItemType id="2"/>
          <ns2:Version>02</ns2:Version>
          <ns2:Rejected>false</ns2:Rejected>
          <ns2:MasterSystem>KOLA</ns2:MasterSystem>
          <ns2:Bridges>
            <ns2:Bridge>
              <ns2:ExternalName>24636704.prt</ns2:ExternalName>
              <ns2:ExternalVersion>2</ns2:ExternalVersion>
              <ns2:ExternalVault>01</ns2:ExternalVault>
              <ns2:BridgeStatus>2</ns2:BridgeStatus>
              <ns2:ExternalObject>wt.epm.EPMDocumentMaster:80372299960|981783618-1249579887230-31922233-43-20-97-131|pdmlink.got.volvo.net</ns2:ExternalObject>
            </ns2:Bridge>
          </ns2:Bridges>
        </ns2:item>
        <ns2:item>
          <ns2:ItemCategory>DigitalModel</ns2:ItemCategory>
          <ns2:ItemNumber>24636734</ns2:ItemNumber>
          <ns2:ItemType id="2"/>
          <ns2:Version>02</ns2:Version>
          <ns2:Rejected>false</ns2:Rejected>
          <ns2:MasterSystem>KOLA</ns2:MasterSystem>
          <ns2:Bridges>
            <ns2:Bridge>
              <ns2:ExternalName>24636734.prt</ns2:ExternalName>
              <ns2:ExternalVersion>2</ns2:ExternalVersion>
              <ns2:ExternalVault>01</ns2:ExternalVault>
              <ns2:BridgeStatus>2</ns2:BridgeStatus>
              <ns2:ExternalObject>wt.epm.EPMDocumentMaster:80383857835|981783618-1249579887230-31922233-43-20-97-131|pdmlink.got.volvo.net</ns2:ExternalObject>
            </ns2:Bridge>
          </ns2:Bridges>
        </ns2:item>
        <ns2:item>
          <ns2:ItemCategory>DigitalModel</ns2:ItemCategory>
          <ns2:ItemNumber>24637103</ns2:ItemNumber>
          <ns2:ItemType id="2"/>
          <ns2:Version>02</ns2:Version>
          <ns2:Rejected>false</ns2:Rejected>
          <ns2:MasterSystem>KOLA</ns2:MasterSystem>
          <ns2:Bridges>
            <ns2:Bridge>
              <ns2:ExternalName>24637103.prt</ns2:ExternalName>
              <ns2:ExternalVersion>2</ns2:ExternalVersion>
              <ns2:ExternalVault>01</ns2:ExternalVault>
              <ns2:BridgeStatus>2</ns2:BridgeStatus>
              <ns2:ExternalObject>wt.epm.EPMDocumentMaster:80383935942|981783618-1249579887230-31922233-43-20-97-131|pdmlink.got.volvo.net</ns2:ExternalObject>
            </ns2:Bridge>
          </ns2:Bridges>
        </ns2:item>
        <ns2:item>
          <ns2:ItemCategory>DigitalModel</ns2:ItemCategory>
          <ns2:ItemNumber>24637106</ns2:ItemNumber>
          <ns2:ItemType id="2"/>
          <ns2:Version>02</ns2:Version>
          <ns2:Rejected>false</ns2:Rejected>
          <ns2:MasterSystem>KOLA</ns2:MasterSystem>
          <ns2:Bridges>
            <ns2:Bridge>
              <ns2:ExternalName>24637106.prt</ns2:ExternalName>
              <ns2:ExternalVersion>2</ns2:ExternalVersion>
              <ns2:ExternalVault>01</ns2:ExternalVault>
              <ns2:BridgeStatus>2</ns2:BridgeStatus>
              <ns2:ExternalObject>wt.epm.EPMDocumentMaster:80384027979|981783618-1249579887230-31922233-43-20-97-131|pdmlink.got.volvo.net</ns2:ExternalObject>
            </ns2:Bridge>
          </ns2:Bridges>
        </ns2:item>
        <ns2:item>
          <ns2:ItemCategory>DigitalModel</ns2:ItemCategory>
          <ns2:ItemNumber>24637109</ns2:ItemNumber>
          <ns2:ItemType id="2"/>
          <ns2:Version>02</ns2:Version>
          <ns2:Rejected>false</ns2:Rejected>
          <ns2:MasterSystem>KOLA</ns2:MasterSystem>
          <ns2:Bridges>
            <ns2:Bridge>
              <ns2:ExternalName>24637109.prt</ns2:ExternalName>
              <ns2:ExternalVersion>2</ns2:ExternalVersion>
              <ns2:ExternalVault>01</ns2:ExternalVault>
              <ns2:BridgeStatus>2</ns2:BridgeStatus>
              <ns2:ExternalObject>wt.epm.EPMDocumentMaster:80384028023|981783618-1249579887230-31922233-43-20-97-131|pdmlink.got.volvo.net</ns2:ExternalObject>
            </ns2:Bridge>
          </ns2:Bridges>
        </ns2:item>
        <ns2:item>
          <ns2:ItemCategory>DigitalModel</ns2:ItemCategory>
          <ns2:ItemNumber>24637257</ns2:ItemNumber>
          <ns2:ItemType id="2"/>
          <ns2:Version>02</ns2:Version>
          <ns2:Rejected>false</ns2:Rejected>
          <ns2:MasterSystem>KOLA</ns2:MasterSystem>
          <ns2:Bridges>
            <ns2:Bridge>
              <ns2:ExternalName>24637257.prt</ns2:ExternalName>
              <ns2:ExternalVersion>2</ns2:ExternalVersion>
              <ns2:ExternalVault>01</ns2:ExternalVault>
              <ns2:BridgeStatus>2</ns2:BridgeStatus>
              <ns2:ExternalObject>wt.epm.EPMDocumentMaster:80389443125|981783618-1249579887230-31922233-43-20-97-131|pdmlink.got.volvo.net</ns2:ExternalObject>
            </ns2:Bridge>
          </ns2:Bridges>
        </ns2:item>
      </ns2:ToC>
    </ns2:DcnEventFreeze>
  </ns2:DataArea>
</ns2:SyncEventElementFreeze>

grep -rl 24634975.asm /app/mqft/xml_files_done --include=PDMLink_PROD_2024100* | xargs grep statusEventType
# no-file for that
-bash-4.4$ cat /app/mqft/xml_files_done/PDMLink_PROD_20241003063214_001_.xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<SyncManagedDocument xmlns="http://plm.volvo.com/VolvoPLMS/SyncManagedDocumentPLMS/Message/1_0" xmlns:ns6="http://plm.volvo.com/VolvoPLMS/SyncDocumentPLMS/Message/1_0" xmlns:ns5="http://plm.volvo.com/VolvoPLMS/SyncDigitalModelPLMS/Message/1_0" xmlns:ns7="http://plm.volvo.com/VolvoPLMS/SyncPartPLMS/Message/1_0" xmlns:ns2="http://plm.volvo.com/VolvoPLMS/PLMS/Payload/1_0" xmlns:ns4="http://plm.volvo.com/VolvoPLMS/Base/1_0" xmlns:ns3="urn:omg.org/plm20/informational/model">
    <Id>idd1041aaf-3aac-431c-8c96-4f7b841f24f9</Id>
    <SyncManagedDocumentHeaderSection>
        <MainTriggeringEvent>
            <statusEventType>freeze</statusEventType>
            <businessObjectType>ManagedDocument</businessObjectType>
            <businessObject>idf0e9a69a-27b6-4c8b-b415-a231324df591</businessObject>
        </MainTriggeringEvent>
        <Session>
            <SenderId>PDMLink</SenderId>
            <SendTime>2024-10-03T06:31:41.322+02:00</SendTime>
            <UserId>Windchill</UserId>
        </Session>
    </SyncManagedDocumentHeaderSection>
    <ns2:PLMS2_0>
        <ns2:PLM_container uid="id38d71e6b-b1ad-46f2-888f-2929f5076152">
            <ns3:Document uid="idf0e9a69a-27b6-4c8b-b415-a231324df591">
                <ns3:Name>COOLANT PIPE</ns3:Name>
                <ns3:Document_id>wt.part.WTPartMaster:80415865722|981783618-1249579887230-31922233-43-20-97-131|pdmlink.got.volvo.net</ns3:Document_id>
                <ns3:Document_version uid="id12510db7-d820-42dc-82a0-310db4dd54a6">
                    <ns3:Id>3.2</ns3:Id>
                    <ns3:Document_representation xsi:type="ns3:Digital_document" uid="ideedae17c-e1aa-4b30-b680-67d98ad8df9e" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
                        <ns3:Id></ns3:Id>
                        <ns3:File>id2edd4ced-9072-4223-a511-c438a54325d1</ns3:File>
                    </ns3:Document_representation>
                </ns3:Document_version>
            </ns3:Document>
            <ns3:Document_file xsi:type="ns3:Digital_file" uid="id2edd4ced-9072-4223-a511-c438a54325d1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
                <ns3:File_id>24634975-WTPart</ns3:File_id>
                <ns3:Simple_property_association uid="id42">
                    <ns3:Specified_value>id43</ns3:Specified_value>
                    <ns3:Value_type>lifecycleInfo/lifecycleState</ns3:Value_type>
                </ns3:Simple_property_association>
                <ns3:Simple_property_association uid="id134">
                    <ns3:Specified_value>id137</ns3:Specified_value>
                    <ns3:Value_type>iba</ns3:Value_type>
                </ns3:Simple_property_association>
            </ns3:Document_file>
            <ns3:Property xsi:type="ns3:General_property" uid="id122" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
                <ns3:Id>iba</ns3:Id>
                <ns3:Property_type>java.lang.String</ns3:Property_type>
            </ns3:Property>
            <ns3:Property_value xsi:type="ns3:String_value" uid="id43" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
                <ns3:Value_name>lifecycleInfo/lifecycleState</ns3:Value_name>
                <ns3:Value_specification>VOLVO_INREVIEW</ns3:Value_specification>
            </ns3:Property_value>
            <ns3:Property_value xsi:type="ns3:String_value" uid="id137" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
                <ns3:Value_name>POT</ns3:Value_name>
                <ns3:Property_value_representation uid="id138">
                    <ns3:Definition>id122</ns3:Definition>
                </ns3:Property_value_representation>
                <ns3:Value_specification></ns3:Value_specification>
            </ns3:Property_value>
        </ns2:PLM_container>
    </ns2:PLMS2_0>
</SyncManagedDocument>


 # PDMLink_PROD_20241017203647_001_.xml
 grep -rl 24634975.asm /app/mqft/xml_files_done --include=PDMLink_PROD_2024100* | xargs grep statusEventType