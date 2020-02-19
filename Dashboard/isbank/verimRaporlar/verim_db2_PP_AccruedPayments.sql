SELECT DISTINCT 
PA.PPA_SEQ_NO,
PA.PPA_PYMT_ID, 
PA.PPA_TSTP,
PA.PPA_INSTALLMENT_NO,
PA.PPA_AMT, 
to_char(PA.PPA_INT_RATE, 'FM09.90') as int_rate,
PA.PPA_PYMT_DT, 
PA.PPA_PYMT_TYPE, 
PA.PPA_TYPE_ID
FROM 
STG.PP_PYMT_PLAN PP, 
STG.PP_ACCRUED_PAYMENTS PA, 
STG.HYM_ACCOUNT_EXTERNAL_REF ER 
WHERE 
ER.ACEXT_ACCOUNT_TYPE_ID = 14 AND 
ER.ACEXT_ACCOUNT_ID = PP.PPL_ACC_ID AND 
PP.PPL_PLAN_ID = PA.PPA_PYMT_PLAN_ID AND
PA.PPA_ST = 'A' AND PP.PPL_ST = 'A'
AND (
PA.SNPST_DT =  TO_DATE('2019-12-24', 'YYYY-MM-DD') AND
ER.SNPST_DT =  TO_DATE('2019-12-24', 'YYYY-MM-DD') AND 
PP.SNPST_DT = TO_DATE('2019-12-24', 'YYYY-MM-DD')
)
AND (
(ER.ACEXT_BRANCH_CODE = '5000' AND ER.ACEXT_ACCOUNT_NUMBER = '1000671')
)
ORDER BY PA.PPA_PYMT_DT ASC, PA.PPA_PYMT_ID ASC;


keywords:104786300 90322
STG

PP_INSTALLMENTS
SNPST_DT SRC_DT	UPD_DT	INST_AGREEMENT_F INST_CAPITAL_AMT INST_FUND_AMT INST_INCR_DECREASE_F INST_INSTALLMENT_AMT 
INST_INSTALLMENT_DT	INST_INSTALLMENT_NO	INST_INSTALLMENT_RATIO INST_INSTALLMENT_TYPE INST_INT_AMT INST_INTERVAL	INST_PLAN_ID	
INST_POSTPONE_F	INST_PYMT_DT INST_PYMT_ST INST_PYMT_TYPE INST_PYMT_TYPE_ORDR INST_REMAINING_CAPITAL_AMT INST_TAX_AMT INST_VERSION_NO

PP_PYMT_PLAN
SNPST_DT SRC_DT		UPD_DT		PPL_ACC_ID	PPL_APP_ID	PPL_AVG_DURATION PPL_BRANCH_CODE	PPL_CREATE_TSTP	PPL_CRY_CODE	PPL_CUST_NO	PPL_DISBURSMNT_DT PPL_FUND_CODE	PPL_FUND_RATE PPL_INSTALLMENT_AMT PPL_INT_RATE PPL_LOAN_AMT	PPL_MTR_DAY_COUNT PPL_MTR_TIME PPL_PD_ID PPL_PER_SCALE PPL_PLAN_ID PPL_PLAN_TYPE PPL_PREPAID_INT_BY_CUST PPL_PREPAID_INT_BY_FIRM PPL_PREV_VERSION PPL_REASON_CODE PPL_ST PPL_START_DT PPL_TAX_CODE PPL_TAX_FREE_TERMS PPL_TAX_RATE PPL_UPD_TSTP	PPL_VERSION		

PP_ACCRUED_PAYMENTS 
SNPST_DT	1	Y	N	DATE (7 bytes)	<LONG>	FREQUENCY
SRC_DT	2	Y	N	DATE (7 bytes)	<LONG>	NONE
UPD_DT	3	Y	N	DATE (7 bytes)	<LONG>	NONE
PPA_AMT	4	Y	N	NUMBER (22 bytes)	<LONG>	NONE
PPA_CRY_RATE	5	Y	N	NUMBER (22 bytes)	<LONG>	NONE
PPA_INDEX	6	Y	N	NUMBER (22 bytes)	<LONG>	NONE
PPA_INSTALLMENT_NO	7	Y	N	NUMBER (22 bytes)	<LONG>	NONE
PPA_INT_RATE	8	Y	N	NUMBER (22 bytes)	<LONG>	NONE
PPA_PART_INDEX	9	Y	N	NUMBER (22 bytes)	<LONG>	NONE
PPA_PYMT_DT	10	Y	N	DATE (7 bytes)	<LONG>	NONE
PPA_PYMT_ID	11	Y	N	NUMBER (22 bytes)	<LONG>	NONE
PPA_PYMT_PLAN_ID	12	Y	N	NUMBER (22 bytes)	<LONG>	NONE
PPA_PYMT_TYPE	13	Y	N	VARCHAR2 (1 bytes)	<LONG>	NONE
PPA_REF_CODE	14	Y	N	VARCHAR2 (15 bytes)	<LONG>	NONE
PPA_SEQ_NO	15	Y	N	NUMBER (22 bytes)	<LONG>	NONE
PPA_ST	16	Y	N	VARCHAR2 (1 bytes)	<LONG>	NONE

PP_OVERDUE
SNPST_DT	1	Y	N	DATE (7 bytes)	<LONG>	FREQUENCY
SRC_DT	2	Y	N	DATE (7 bytes)	<LONG>	NONE
UPD_DT	3	Y	N	DATE (7 bytes)	<LONG>	NONE
PPO_ACCRUAL_DT	4	Y	N	DATE (7 bytes)	<LONG>	NONE
PPO_EXCH_RATE	5	Y	N	NUMBER (22 bytes)	<LONG>	NONE
PPO_INSTALLMENT_NO	6	Y	N	NUMBER (22 bytes)	<LONG>	NONE
PPO_PLAN_ID	7	Y	N	NUMBER (22 bytes)	<LONG>	NONE
PPO_REASON_CODE	8	Y	N	VARCHAR2 (1 bytes)	<LONG>	NONE
PPO_VERSION_NO	9	Y	N	NUMBER (22 bytes)	<LONG>	NONE

HYM_ACCOUNT_EXTERNAL_REF 
SNPST_DT	1	Y	N	DATE (7 bytes)	<LONG>	NONE
SRC_DT	2	Y	N	DATE (7 bytes)	<LONG>	NONE
UPD_DT	3	Y	N	DATE (7 bytes)	<LONG>	NONE
ODS_SUBE_KODU	4	Y	N	NUMBER (22 bytes)	<LONG>	NONE
ODS_HESAP_NO	5	Y	N	NUMBER (22 bytes)	<LONG>	NONE
ACEXT_ACCOUNT_TYPE_ID	6	Y	N	NUMBER (22 bytes)	<LONG>	NONE
ACEXT_BRANCH_CODE	7	Y	N	NUMBER (22 bytes)	<LONG>	NONE
ACEXT_ACCOUNT_NUMBER	8	Y	N	NUMBER (22 bytes)	<LONG>	NONE
ACEXT_ADDITIONAL_KEY	9	Y	N	VARCHAR2 (50 bytes)	<LONG>	NONE
ACEXT_ACCOUNT_ID	10	Y	N	NUMBER (22 bytes)	<LONG>	NONE
ACEXT_EXPIRE_TS	11	Y	N	DATE (7 bytes)	<LONG>	NONE
ACEXT_IBAN	12	Y	N	VARCHAR2 (26 bytes)	<LONG>	NONE
ACEXT_ACCOUNT_LOCATION	13	Y	N	VARCHAR2 (1 bytes)	<LONG>	NONE
ACEXT_PARTITION_INDEX	14	Y	N	NUMBER (22 bytes)	<LONG>	NONE
SYS_STS9ZKKRO7JHJB#PAQ2XH...		Y	N	NUMBER (22 bytes)	<LONG>	NONE