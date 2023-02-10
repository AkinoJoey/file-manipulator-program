import sys
import os

# 有効なコマンド
# reverse,copy,duplicate-contents,replace-string

print("実行したいコマンドを入力してください。")
command = sys.stdin.readline().strip()

def isValidCommand(command):
    if command == "reverse" or command == "copy" or command == "duplicate-contents" or command == "replace-string":
        return True
    else:
        return False

def isFileExist(path):
    if os.path.isfile(path):
        return True
    else:
        return False

def isDirExist(path):
    if os.path.isdir(path):
        return True
    else:
        return False

def printAlert(missPoint):
    print("正しい" + missPoint +"を入力してください。")

while not isValidCommand(command):
    printAlert("コマンド")
    command = sys.stdin.readline().strip()
    
print("入力するファイルのパスを入力してください。")
inputPath = sys.stdin.readline().strip()

while not isFileExist(inputPath):
    printAlert("入力するファイルのパス")
    inputPath = sys.stdin.readline().strip()

fileName = inputPath[inputPath.rfind('\\'):]
print(fileName)
print("出力するファイルのパスを入力してください。")

outputPath = sys.stdin.readline().strip()
print(outputPath + fileName)
if command == "reverse":
    while not isDirExist(outputPath):
        printAlert("出力するフォルダのパス")
        outputPath = sys.stdin.readline().strip()
    
    with open(inputPath) as f:
        contents = f.read()

    with open(outputPath + fileName,'x') as f:
        f.write(contents[::-1])


