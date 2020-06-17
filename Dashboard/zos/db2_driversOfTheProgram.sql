select pgmname, prjname, mdltype from scdegisk.moduls where pgmname in 
(SELECT DISTINCT PROGRAM1 FROM SCDEGISK.PGMDRIVE where PROGRAM2 = 'SBPVTRAN' AND PROGRAM1 LIKE 'PS%');