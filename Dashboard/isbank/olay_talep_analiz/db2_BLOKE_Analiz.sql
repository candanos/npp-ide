SELECT LPAD(CAST(A.ACEXT_BRANCH_CODE AS VARCHAR(4)),4,'0'),          
       LPAD(CAST(A.ACEXT_ACCOUNT_NUMBER AS VARCHAR(7)),7,'0'),       
       LPAD(CAST(AC.ACCUS_CUSTOMER_ID AS VARCHAR(9)),9,'0'),         
       LPAD(CAST(M.ADI AS CHAR(15)),15,' '),                         
       LPAD(CAST(M.SOYADI AS CHAR(45)),45,' '),                      
       LPAD(CAST(C.CL_TELEGRAM_ID AS VARCHAR(5)),5,'0')              
FROM                                                                 
SCLMRSK.CUST_TELEGRAM_RELATIONS C,                                   
SCMBY.MBY_BIREYSEL_KIMLIK M,                                         
SCHESAP.ACCOUNT_EXTERNAL_REF A,                                      
SCHESAP.ACCOUNT_CUSTOMER_REL AC,                                     
SCHESAP.ACCOUNT_INFO AI,                                             
SCLOAN.LAM_LOAN_INFO L                                               
WHERE C.CL_ST_CODE NOT IN (9)                                        
AND M.MUSTERI_NO = AC.ACCUS_CUSTOMER_ID                              
AND A.ACEXT_ACCOUNT_ID = AC.ACCUS_ACCOUNT_ID                         
AND A.ACEXT_ACCOUNT_TYPE_ID = 14 AND AI.ACINF_STATUS = 2             
AND A.ACEXT_ACCOUNT_ID = AI.ACINF_ACCOUNT_ID                         
AND AC.ACCUS_CUSTOMER_ID = C.CL_CUST_ID 
AND C.CL_BRANCH_ID = A.ACEXT_BRANCH_CODE
AND L.LOAN_ACC_ID = A.ACEXT_ACCOUNT_ID  
AND L.LOAN_NEXT_INT_DT = '2019-03-31'   
WITH UR   


select * from SCKREDI.KBL_KRD_BLOKE_BILGI where VARCHAR_FORMAT(BLK_BLOKE_BEGIN_DT,'YYYY-MM-DD') = '2019-03-31' AND BLK_ST_CODE = 0                          