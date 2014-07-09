@ECHO OFF
NET USE V: /delete
NET USE V: \\btecbpo.local\bpo_Prod\Banctec\BtecImg\BTECPRD2\BI_ImportPath\Done\123

FOR %%F in ("V:\*") DO python ItemWriter.py %%~fxF

ECHO.

ECHO DONE - Converted files in Reports directory

PAUSE
