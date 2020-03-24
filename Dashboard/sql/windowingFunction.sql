select T.bchkey as tkey, 'X' as tval 
from ( 
select
(
to_char(b.bc_sbkd) || 
lpad(to_char(b.bc_musno),7,'0') || 
to_char(b.bc_acilkd1) || '-' ||
replace(a.val_valor, '-') || '-' ||
to_char(a.val_bakiye) || '-' || 
to_char(a.val_fark) || '-' ||  
to_char( nvl(a.val_spread,0) + nvl(a.val_baz_oran,0) )
) as bchkey,
to_char(a.val_bakiye) as bakiye, 
to_char( nvl(a.val_spread,0) + nvl(a.val_baz_oran,0) ) as rate,
row_number() over ( partition by to_char(b.bc_sbkd), lpad(to_char(b.bc_musno),7,'0') 
order by to_number(replace(a.val_valor, '-')) )
as rn,
LAG(a.val_bakiye, 1, 0) over ( partition by to_char(b.bc_sbkd), lpad(to_char(b.bc_musno),7,'0') 
order by to_number(replace(a.val_valor, '-')) )
as prev_bakiye,
LAG(a.val_bakiye, 2, 0) over ( partition by to_char(b.bc_sbkd), lpad(to_char(b.bc_musno),7,'0') 
order by to_number(replace(a.val_valor, '-')) )
as prev_prev_bakiye,
LAG(to_char( nvl(a.val_spread,0) + nvl(a.val_baz_oran,0) ), 1, 0) over ( partition by to_char(b.bc_sbkd), lpad(to_char(b.bc_musno),7,'0') 
order by to_number(replace(a.val_valor, '-')) )
as prev_rate,
MAX(ABS(a.val_bakiye)) OVER ( 
partition by to_char(b.bc_sbkd), lpad(to_char(b.bc_musno),7,'0')
order by to_number(replace(a.val_valor, '-'))  
ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING ) as max_before   
from 
stg.unlborclu_db2 a,
stg.borclure b,
stg.hym_account_external_ref ext
where
a.src_dt = to_date('#snp_date#','YYYYMMDD') and 
b.snpst_dt = to_date('#snp_date#','YYYYMMDD') and 
ext.snpst_dt = to_date('#snp_date#','YYYYMMDD') and
to_number(replace(a.val_valor, '-')) <= '#snp_date#' and  
ext.acext_branch_code = '2421' and
a.val_karton_sube = b.bc_sbkd and 
a.val_karton_no = b.bc_musno and
to_char(b.bc_nakit_akis_durum) <> 'N' and 
ext.acext_branch_code = b.bc_sbkd and
lpad(to_char(ext.acext_account_number),7,'0') = lpad(to_char(b.bc_musno),7,'0') and 
ext.acext_account_type_id = 14 and 
ext.acext_expire_ts is null and
to_char(b.bc_acilkd1) <> '1' and
( 
( to_number(replace(a.val_valor, '-')) < to_number(b.bc_kapatar_yyag) and to_char(b.bc_acilkd1) = '3') 
or 
to_char(b.bc_acilkd1) <> '3' 
)
order by 1 asc 
) T 
where 
(
(T.max_before <> '0' or T.bakiye <> '0')
)
and (
T.bakiye <> T.prev_bakiye or T.rate <> T.prev_rate )
ORDER BY 1 ASC 