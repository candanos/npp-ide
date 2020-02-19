SELECT
concat(rpad(to_char(bc_sbkd),5,' '), lpad(to_char(bc_musno),7,'0')) as bchkey 
from stg.borclure where snpst_dt = to_date('2019-09-21', 'YYYY-MM-DD')  
ORDER BY 1