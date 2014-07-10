

NET USE V: /delete
NET USE V: ..\

FOR %%F in ("..\*.ack") DO python ItemWriter.py %%~fxF

ECHO.

ECHO DONE - Converted files in Reports directory

PAUSE
