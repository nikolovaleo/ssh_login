@echo off 
setlocal enableDelayedExpansion

for /f "tokens=1,2" %%A in (ips.txt) do (
    echo %%A
    echo %%B

    
    for /L %%C in (1,1,%%B) do (
       ping %%A    
    )   
)
pause