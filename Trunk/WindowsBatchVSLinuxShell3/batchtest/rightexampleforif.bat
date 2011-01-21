@echo off
setlocal enabledelayedexpansion


set VAR=before
    if "%VAR%" == "before" (
        set VAR=after
        if "!VAR!" == "after" @echo If you see this, it worked
    )

endlocal

pause