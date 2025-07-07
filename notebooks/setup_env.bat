@echo off
echo Setting up environment variables for Smart Research Assistant...

set HF_HUB_DISABLE_SYMLINKS_WARNING=1
set TOKENIZERS_PARALLELISM=false
set HF_HOME=%USERPROFILE%\.cache\huggingface
set TRANSFORMERS_CACHE=%USERPROFILE%\.cache\huggingface\transformers
set HF_DATASETS_CACHE=%USERPROFILE%\.cache\huggingface\datasets

echo Environment variables set successfully!
echo.
echo To make these permanent, run:
echo setx HF_HUB_DISABLE_SYMLINKS_WARNING 1
echo setx TOKENIZERS_PARALLELISM false
echo.
pause
