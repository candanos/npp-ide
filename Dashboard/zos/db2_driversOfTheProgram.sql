select pgmname, prjname, mdltype from scdegisk.moduls where pgmname in 
(SELECT DISTINCT PROGRAM1 FROM SCDEGISK.PGMDRIVE where PROGRAM2 = 'ADRSAKLA' AND PROGRAM1 LIKE 'PS%');