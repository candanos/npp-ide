SELECT
ae.acext_branch_code,
ae.acext_account_number,
ab.acbln_currency_code,
ai.acinf_status,
le.lex_commsn_code,
le.lex_interest_rate_type,
le.lex_notice_per,
ae.acext_expire_ts,
ab.acbln_credit_limit,
ab.acbln_credit_limit,
ab.acbln_credit_balance,
ab.acbln_credit_balance,
air.acint_base_rate,
air.acint_base_rate,
air.acint_banks_share,
air.acint_comm_rate,
le.lex_cheque_margin,
le.lex_note_margin,
ai.acinf_opening_date,
ai.acinf_opening_date,
ai.acinf_close_date,
ai.acinf_close_date,
ai.acinf_last_trx_date,
ai.acinf_last_trx_date,
air.acint_default_rate,
ae.acext_iban,
ae.acext_iban,
ae.acext_iban,
le.lex_tmo_code,
le.lex_commit_code,
ai.acinf_product_id,
ai.acinf_product_id,
le.lex_related_insr_branch_code,
le.lex_related_insr_type,
le.lex_related_insr_passbook_no,
le.lex_transit_trade_f
FROM
ods.hym_account_external_ref ae,
ods.hym_account_balances ab,
ods.hym_account_info_g ai,
stg.hym_loan_extsn le,
ods.hym_account_interest air
WHERE ae.acext_branch_code = '1380' AND ae.acext_account_number = '1000740' AND
ae.acext_account_id = ai.acinf_account_id AND
ae.acext_account_id = ab.acbln_account_id and
ae.acext_account_id = air.acint_account_id and
ae.acext_account_id = le.lex_acc_id and
ae.snpst_dt = to_date('2019-06-01', 'YYYY-MM-DD') and
ab.snpst_dt = to_date('2019-06-01', 'YYYY-MM-DD') and
ai.snpst_dt = to_date('2019-06-01', 'YYYY-MM-DD') and
le.snpst_dt = to_date('2019-06-23', 'YYYY-MM-DD') and
air.snpst_dt = to_date('2019-06-01', 'YYYY-MM-DD');

ae.acext_account_id = lc.lcq_acc_id 
hiç kayýt olmamasý durumunda sorgunun boþ dönmesine sebep olur.

SELECT
ae.acext_branch_code,
ae.acext_account_number,
ab.acbln_currency_code,
ai.acinf_status,
le.lex_commsn_code,
li.loan_tax_code,
li.loan_fund_code,
li.loan_cry_fx_f,
li.loan_blockage_code,
li.loan_int_term,
le.lex_interest_rate_type,
le.lex_notice_per,
ae.acext_expire_ts,
ab.acbln_credit_limit,
ab.acbln_credit_limit,
ab.acbln_credit_balance,
ab.acbln_credit_balance,
air.acint_base_rate,
air.acint_base_rate,
air.acint_banks_share,
air.acint_comm_rate,
le.lex_cheque_margin,
le.lex_note_margin,
ai.acinf_opening_date,
ai.acinf_opening_date,
ai.acinf_close_date,
ai.acinf_close_date,
li.loan_next_int_dt,
ai.acinf_last_trx_date,
ai.acinf_last_trx_date,
pi.inst_int_amt,
pi.inst_commsn_amt,
pi.inst_tax_amt,
air.acint_default_rate,
ae.acext_iban,
ae.acext_iban,
ae.acext_iban,
li.loan_opening_cry,
lc.lcq_discount_code,
lc.lcq_discount_ref_no,
li.loan_trx_auth_code,
le.lex_tmo_code,
le.lex_commit_code,
lc.lcq_discount_temp_dur,
lc.lcq_discount_avg_dur_dt,
lc.lcq_discount_exclude_f,
li.loan_auto_proceeding_f,
ai.acinf_product_id,
ai.acinf_product_id,
le.lex_related_insr_branch_code,
le.lex_related_insr_type,
le.lex_related_insr_passbook_no,
li.loan_export_code,
li.loan_src_code,
le.lex_transit_trade_f
FROM
ods.hym_account_external_ref ae,
ods.hym_account_balances ab,
ods.hym_account_info_g ai,
stg.hym_loan_extsn le,
ods.hym_loan_info li,
ods.hym_account_interest air,
stg.hym_loan_cheque_integration lc,
stg.pp_pymt_plan pp,
stg.pp_installment pi
WHERE ae.acext_branch_code = '1380' AND ae.acext_account_number = 1000740 AND
ae.acext_account_id = ai.acinf_account_id AND
ae.acext_account_id = ab.acbln_account_id and
ae.acext_account_id = air.acint_account_id and
ae.acext_account_id = li.loan_acc_id and
ae.acext_account_id = le.lex_acc_id and
ae.acext_account_id = lc.lcq_acc_id and
pp.ppl_acc_id = ae.acext_account_id and pp.ppl_st = 'A' and pi.inst_plan_id = pp.ppl_plan_id AND
ae.snpst_dt = to_date('2019-06-01', 'yyyy-mm-dd') and
ab.snpst_dt = to_date('2019-06-01', 'yyyy-mm-dd') and
ai.snpst_dt = to_date('2019-06-01', 'yyyy-mm-dd') and
le.snpst_dt = to_date('2019-06-01', 'yyyy-mm-dd') and
li.snpst_dt = to_date('2019-06-01', 'yyyy-mm-dd') and
air.snpst_dt= to_date('2019-06-01', 'yyyy-mm-dd') and
lc.snpst_dt = to_date('2019-06-01', 'yyyy-mm-dd') and
pp.snpst_dt = to_date('2019-06-01', 'yyyy-mm-dd') and
pi.snpst_dt = to_date('2019-06-25', 'yyyy-mm-dd');