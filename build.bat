del /s /q "./dist"
pyinstaller main.py --add-data "./assets/salty-papers-logo.png;./assets" --add-data "./salty_papers.config;./" --name SaltyPapers --onefile --noconsole -i "./assets/salty-papers-logo.ico"
xcopy /s /i /e /y ".\assets\*.*" ".\dist\assets"
xcopy /s /i /e /y ".\tools\*.*" ".\dist\tools"
xcopy /i /y ".\salty_papers.config" ".\dist"
xcopy /i /y ".\README.md" ".\dist"
xcopy /i /y ".\install.bat" ".\dist"