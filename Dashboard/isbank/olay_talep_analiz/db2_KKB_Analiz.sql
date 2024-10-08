/* trx logs */
SELECT TL.LOG_KEY_ID, TL.LOG_TIME, TL.LOG_TYPE, CAST(TL.LOG_RES_REQ AS VARCHAR(1500)) 
FROM SCLOAN.LFN_KKB_TRX_LOG TL, SCLOAN.LFN_KKB_NOTIFICATION NT, 
SCLOAN.LFN_KKB_LOAN_INFO LI, SCHESAP.ACCOUNT_EXTERNAL_REF EXT
WHERE TL.LOG_KEY_ID = NT.NOT_ID AND NT.NOT_LOI_ID = LI.LOI_ID AND LI.LOI_ACCOUNT_ID = EXT.ACEXT_ACCOUNT_ID AND EXT.ACEXT_BRANCH_CODE = '2218' AND EXT.ACEXT_ACCOUNT_NUMBER = '197618' ORDER BY 1 DESC;
/* loan_info record of the account */ 
SELECT DISTINCT LI.* FROM SCLOAN.LFN_KKB_LOAN_INFO LI, SCHESAP.ACCOUNT_EXTERNAL_REF AE
WHERE AE.ACEXT_ACCOUNT_ID = LI.LOI_ACCOUNT_ID AND 
AE.ACEXT_BRANCH_CODE = '2218' AND AE.ACEXT_ACCOUNT_NUMBER = '197618' WITH UR;
/* all loans of the customer */
SELECT DISTINCT LI.* FROM SCLOAN.LFN_KKB_LOAN_INFO LI, SCHESAP.ACCOUNT_EXTERNAL_REF AE
WHERE AE.ACEXT_ACCOUNT_ID = LI.LOI_ACCOUNT_ID AND LI.LOI_CUSTOMER_NO = 33214259 WITH UR;
/* branch and account_number of an account */ 
SELECT * FROM SCHESAP.ACCOUNT_EXTERNAL_REF EXT WHERE EXT.ACEXT_ACCOUNT_ID = 80752574 


SCLOAN.LFN_KKB_LOAN_INFO
LOI_ID	1	N	Y	BIGINT  	
LOI_CUSTOMER_NO	2	N	N	INTEGER 	
LOI_SCOPE_CODE	3	N	N	SMALLINT	
LOI_ACCOUNT_ID	4	Y	N	BIGINT  	
LOI_ACCOUNT_NUMBER	5	Y	N	CHAR    (15)	
LOI_ACCOUNT_TYPE	6	N	N	CHAR    (1)	
LOI_CURRENCY_CODE	7	Y	N	SMALLINT	
LOI_CREDIT_BALANCE	8	N	N	DECIMAL (18,2)	
LOI_STATUS	9	N	N	CHAR    (1)	
LOI_CREATE_USER	10	N	N	CHAR    (8)	
LOI_CREATE_TIME	11	N	N	TIMESTMP	
LOI_UPDATE_USER	12	Y	N	CHAR    (8)	
LOI_UPDATE_TIME	13	N	N	TIMESTMP	
LOI_NOTIF_STATUS	14	Y	N	CHAR    (1)

SCLOAN.LFN_KKB_NOTIFICATION
NOT_ID	1	N	Y	BIGINT  	
NOT_LOI_ID	2	N	N	BIGINT  	
NOT_TRX_AMOUNT	3	N	N	DECIMAL (18,2)	
NOT_TYPE	4	N	N	CHAR    (1)	
NOT_STATUS	5	N	N	CHAR    (1)	
NOT_DESC	6	Y	N	VARCHAR (250)	
NOT_CREATE_USER	7	N	N	CHAR    (8)	
NOT_CREATE_TIME	8	N	N	TIMESTMP	
NOT_UPDATE_USER	9	Y	N	CHAR    (8)	
NOT_UPDATE_TIME	10	N	N	TIMESTMP

SCHESAP.ACCOUNT_EXTERNAL_REF
ACEXT_ACCOUNT_TYPE_ID	1	N	Y	SMALLINT	
ACEXT_BRANCH_CODE	2	N	Y	SMALLINT	
ACEXT_ACCOUNT_NUMBER	3	N	Y	INTEGER 	
ACEXT_ADDITIONAL_KEY	4	N	Y	VARCHAR (50)	
ACEXT_ACCOUNT_ID	5	N	N	BIGINT  	
ACEXT_EXPIRE_TS	6	Y	N	TIMESTMP	
ACEXT_IBAN	7	N	N	CHAR    (26)	
ACEXT_ACCOUNT_LOCATION	8	N	N	CHAR    (1)	
ACEXT_PARTITION_INDEX	9	N	N	SMALLINT

LOG_KEY_ID	1	N	Y	BIGINT  	
LOG_KEY_TYPE	2	N	Y	CHAR    (1)	
LOG_TYPE	3	N	Y	CHAR    (1)	
LOG_RES_REQ	4	N	N	CLOB    	
LOG_TIME	5	N	N	TIMESTMP	
DB2_GENERATED_ROWID_FOR_LOBS	6	N	N	ROWID   