* REXX */
THEPDS = "USERID.ABC.XYZ"
X = OUTTRAP('ML.')
"LISTDS 'THEPDS' MEMBERS"
X = OUTTRAP('OFF')
DO N = 7 TO ML.0
    PARSE VAR ML.N MEMBER                           
    MEMBER=STRIP(MEMBER)
    SAY "MEMBER NAME IS ==>" MEMBER
END                                             

EXIT 0                                         