SELECT SNPST_DT, 
UPD_DT,
BC_SONISTAR_YYAG_DT,
BC_ACILKD1,
BC_FAIZLIBAK,
BC_VALORBAK,
BC_NEXT_FAIZTAR_YYAG_DT,
BC_SON_FAIZTAR_YYAG_DT,
to_char(BC_BFORANI, 'FM99.90') as bf_oran,
to_char(BC_MALIYET_ORANI,'FM99.90') as mly_oran,
BC_TAHAKKUK_SAYISI
FROM
ODS.BORCLURE_GUNLUK
WHERE
BC_SBKD = '1380' AND BC_MUSNO = '1000741' AND
SNPST_DT >= to_date('2018-01-31', 'YYYY-MM-DD');