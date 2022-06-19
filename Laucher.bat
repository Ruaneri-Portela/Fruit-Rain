@echo off
cls
:menu
cls
color 30

ECHO ===================================
ECHO Obetendo Permissao de Administrador
ECHO ===================================

:init
setlocal DisableDelayedExpansion
set cmdInvoke=1
set winSysFolder=System32
set "batchPath=%~0"
for %%k in (%0) do set batchName=%%~nk
set "vbsGetPrivileges=%temp%\OEgetPriv_%batchName%.vbs"
setlocal EnableDelayedExpansion

:checkPrivileges
NET FILE 1>NUL 2>NUL
if '%errorlevel%' == '0' ( goto gotPrivileges ) else ( goto getPrivileges )

:getPrivileges
if '%1'=='ELEV' (echo ELEV & shift /1 & goto gotPrivileges)
ECHO.
ECHO *****************************************
ECHO Chamando UAC para elevacao de privilegios
ECHO ******************************************

ECHO Set UAC = CreateObject^("Shell.Application"^) > "%vbsGetPrivileges%"
ECHO args = "ELEV " >> "%vbsGetPrivileges%"
ECHO For Each strArg in WScript.Arguments >> "%vbsGetPrivileges%"
ECHO args = args ^& strArg ^& " "  >> "%vbsGetPrivileges%"
ECHO Next >> "%vbsGetPrivileges%"

if '%cmdInvoke%'=='1' goto InvokeCmd 

ECHO UAC.ShellExecute "!batchPath!", args, "", "runas", 1 >> "%vbsGetPrivileges%"
goto ExecElevation

:InvokeCmd
ECHO args = "/c """ + "!batchPath!" + """ " + args >> "%vbsGetPrivileges%"
ECHO UAC.ShellExecute "%SystemRoot%\%winSysFolder%\cmd.exe", args, "", "runas", 1 >> "%vbsGetPrivileges%"

:ExecElevation
"%SystemRoot%\%winSysFolder%\WScript.exe" "%vbsGetPrivileges%" %*
exit /B

:gotPrivileges
setlocal & cd /d %~dp0
if '%1'=='ELEV' (del "%vbsGetPrivileges%" 1>nul 2>nul  &  shift /1)

cls
date /t
echo Computador: %computername% Usuario: %username%                   
echo         Fruit Rain Laucher
echo  ==================================
echo * 1.Iniciar Jogo                  * 
echo * 2.Primero Inicio                *
echo * 3.Ajuda                         * 
echo * 4.Sobre                         *
echo * 5.Sair                          * 
echo  ==================================                      

set /p opcao= Escolha uma opcao: 
echo ------------------------------
if %opcao% equ 1 goto iniciarg
if %opcao% equ 2 goto primeror
if %opcao% equ 3 goto ajudap
if %opcao% equ 4 goto sobrep
if %opcao% equ 5 goto sair
if %opcao% GEQ 6 goto erro

:iniciarg
cls
echo ==================================
echo *      Jogo Iniciado             *
echo ==================================
python .\Main.py
pause
goto menu

:primeror
cls
echo ==============================================
echo * Requisitos para essa funcao:               * 
echo * 1.Elevacao pode ser solicitada             * 
echo * 2.Necessita de internet                    * 
echo * 3.Apenas Windows 11(Para Instalar o Python)* 
echo * 4.Responda positivamente a toda solicitacao* 
echo ==========================================================
echo * Caso rode uma versao antiga do Windows;                *
echo * Baixe o python em 'https://www.python.org/downloads/'  *
echo ==========================================================
pause
winget install 9MSSZTT1N39L --silent
echo ===============================
echo * Python Instalado com Sucesso * 
echo ===============================
pause
pip install simpleaudio
echo ==================================
echo *    Dependencias Instaladas     *
echo ==================================
pause
goto menu

:ajudap
cls
echo ================================================
echo * Ajuda:                                       *
echo * 1. Caso isso apareca                         *
echo * -('python/pip' nao e reconhecido como        *
echo * um comando interno ou externo, um programa   *
echo * operavel ou um arquivo em lotes.)            * 
echo * -O python nao esta instalado                 *
echo * -instale em https://www.python.org/downloads/*
echo * ou rode o primeiro inicio(apenas W11)        *
echo * -------------------------------------------- *
echo * 2.Caso o python retorne um traceback         *
echo * -Rode o primeiro inicio(Precisa do Python)   *
echo * -Precisa de internet (Okay!)                 *
echo * -------------------------------------------- *
echo * 3.Objetivo do jogo                           *
echo * Fruit Rain e um jogo simples onde objetos    *
echo * caem e precisam ser aparados, quando aparados*
echo * se ganham pontos quando nao se perde vida,   *
echo * acelerando com o tempo aumentando a          *
echo * dificuldade, ate que o jogador perca         *
echo * -------------------------------------------- *
echo * 4.Lista de Comandos                          *
echo * a - move-se a direita                        *
echo * d - move-se a esqueda                        *
echo * espaco - pula                                *
echo * c - acelera o jogo                           *
echo * h - ajuda                                    *
echo * p - pausa/despausa                           *
echo * r - reinicia                                 *
echo * t - gerenciador de comando interno           *
echo ================================================
pause
goto menu

:sobrep
cls
echo ==================================
echo *Craido Por Ruaneri Portela para *
echo *a atividade de segundo semestre *
echo *da materia de AED da FURG       *
echo *12/2021 Santarem/Para/Brasil    *
echo ==================================
pause
goto menu

:sair
cls
pause
exit

:erro
echo ==============================================
echo * Opcao Invalida! Escolha outra opcao do menu *
echo ==============================================
pause
goto menu