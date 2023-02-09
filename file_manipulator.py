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

while not isValidCommand(command):
    print("正しいコマンドを入力してください。")
    command = sys.stdin.readline().strip()
    
print("入力するファイルのパスを入力してください。")
inputPath = sys.stdin.readline().strip()

while not isFileExist(inputPath):
    print("正しいパスを入力してください。")
    inputPath = sys.stdin.readline().strip()

fileName = inputPath.rfind('/')
print("出力するファイルのパスを入力してください。")
outputPath = sys.stdin.readline().strip()

while not isFileExist(outputPath):
    print("正しいパスを入力してください。")
    outputPath = sys.stdin.readline().strip()

