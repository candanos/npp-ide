SELECT DISTINCT 
T2.LOI_CUSTOMER_NO,
T2.LOI_SCOPE_CODE,
T2.LOI_STATUS, 
T2.LOI_CURRENCY_CODE,
T1.ACEXT_BRANCH_CODE,
T1.ACEXT_ADDITIONAL_KEY,
T1.ACEXT_ACCOUNT_NUMBER, 		
T2.LOI_CREDIT_BALANCE,
T3.ACBLN_CREDIT_BALANCE,
T4.ACINF_STATUS
FROM 
ODS.HYM_ACCOUNT_EXTERNAL_REF T1,
ODS.LFN_KKB_LOAN_INFO T2, 
ODS.HYM_ACCOUNT_BALANCES T3, 
ODS.HYM_ACCOUNT_INFO T4 
WHERE 
T1.ACEXT_ACCOUNT_ID = T2.LOI_ACCOUNT_ID AND
T1.ACEXT_ACCOUNT_ID = T3.ACBLN_ACCOUNT_ID AND 
T1.ACEXT_ACCOUNT_ID = T4.ACINF_ACCOUNT_ID AND 
(T2.LOI_STATUS = 'S' OR T2.LOI_STATUS = 'A') AND 
T1.ACEXT_EXPIRE_TS IS NULL AND 
T1.ACEXT_ACCOUNT_TYPE_ID = 5 AND 
(ABS(T3.ACBLN_CREDIT_BALANCE) > T2.LOI_CREDIT_BALANCE OR ABS(T3.ACBLN_CREDIT_BALANCE) < T2.LOI_CREDIT_BALANCE) AND 
T1.SNPST_DT = to_date('2019-09-01', 'YYYY-MM-DD') AND
T2.SNPST_DT = to_date('2019-09-01', 'YYYY-MM-DD') AND
T3.SNPST_DT = to_date('2019-09-01', 'YYYY-MM-DD') AND
T4.SNPST_DT = to_date('2019-09-01', 'YYYY-MM-DD')
ORDER BY 1 ASC, 2 ASC;