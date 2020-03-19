select pgmname, prjname, mdltype from scdegisk.moduls where pgmname in 
(SELECT DISTINCT PROGNAME FROM SCDEGISK.CPYFIELD WHERE COPYNAME = 'TXNINPC6');