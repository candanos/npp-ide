SELECT 
ER.ACEXT_BRANCH_CODE,
ER.ACEXT_ACCOUNT_NUMBER,
ACR.ACCUS_CUSTOMER_ID,
ER.ACEXT_ACCOUNT_ID,
ER.ACEXT_ACCOUNT_TYPE_ID,
PP.PPL_CRY_CODE,
PP.PPL_PLAN_ID,
to_char(PP.PPL_INT_RATE,'FM09.90') as int_rate,
to_char(PP.PPL_FUND_RATE,'FM09.90') as fund_rate,
to_char(PP.PPL_TAX_RATE,'FM09.90') as tax_rate,
AAR.ACREL_REL_ACCOUNT_ID
FROM
ODS.HYM_ACCOUNT_EXTERNAL_REF ER,
ODS.HYM_LAM_LOAN_INFO LI,
ODS.HYM_ACCOUNT_CUSTOMER_REL ACR,
ODS.HYM_ACCOUNT_ACCOUNT_REL AAR,
STG.PP_PYMT_PLAN PP
WHERE 
ER.ACEXT_BRANCH_CODE = 1380 AND ER.ACEXT_ACCOUNT_NUMBER = 1000740 AND
ER.ACEXT_ACCOUNT_ID = LI.LOAN_ACC_ID AND LI.LOAN_ACC_ID = ACR.ACCUS_ACCOUNT_ID AND
ER.ACEXT_ACCOUNT_ID = AAR.ACREL_ACCOUNT_ID AND 
(AAR.ACREL_ARR_TYPE = 101 AND AAR.ACREL_REL_ARR_TYPE = 113 AND AAR.ACREL_REL_TYPE = 28 AND AAR.ACREL_STATUS = 'A') AND
PP.PPL_ACC_ID = ER.ACEXT_ACCOUNT_ID AND PP.PPL_ST = 'A' AND
ER.SNPST_DT = TO_DATE('2019-04-01', 'YYYY-MM-DD') AND
LI.SNPST_DT = TO_DATE('2019-04-01', 'YYYY-MM-DD') AND
ACR.SNPST_DT = TO_DATE('2019-04-01', 'YYYY-MM-DD') AND
AAR.SNPST_DT = TO_DATE('2019-04-01', 'YYYY-MM-DD') AND
PP.SNPST_DT = TO_DATE('2019-04-25', 'YYYY-MM-DD');



