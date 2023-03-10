@echo off

pyinstaller --onefile --console --name "SefaceParticleSequenceMerge" --icon "../icon.ico" ../main.py

rem Move the executable to the root of scripts folder.
set executable=%cd%\dist\SefaceParticleSequenceMerge.exe
set new_executable=%~dp0\SefaceParticleSequenceMerge.exe
move %executable% %new_executable%

rem Remove extra files from the scripts directory. 
set build_folder=%cd%\build
set dist_folder=%cd%\dist
set spec_file=%cd%\SefaceParticleSequenceMerge.spec

rd /s /q %build_folder%
rd /s /q %dist_folder%
del %spec_file%
