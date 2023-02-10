import sys
import os

# 有効なコマンド
# reverse,copy,duplicate-contents,replace-string

def isValidCommand(command):
    if command == "reverse" or command == "copy" or command == "duplicate-contents" or command == "replace-string":
        return True
    else:
        return False

def isFileOrDirExsits(path):
    if os.path.exists(path):
        return True
    else:
        return False

def printAlert(missPoint):
    print("正しい" + missPoint +"を入力してください。")


print("実行したいコマンドを入力してください。")
command = sys.stdin.readline().strip()

# コマンドのバリデータ
while not isValidCommand(command):
    printAlert("コマンド")
    command = sys.stdin.readline().strip()
    
print("入力するファイルのパスを入力してください。")
inputPath = sys.stdin.readline().strip()

# inputPathのバリデータ
while not isFileOrDirExsits(inputPath):
    printAlert("入力するファイルのパス")
    inputPath = sys.stdin.readline().strip()

fileName = inputPath[inputPath.rfind('\\'):]

# コマンドがreverseだった場合　inputpath にあるファイルを受け取り、outputpath に inputpath の内容を逆にした新しいファイルを作成します。
if command == "reverse":
    print("出力するフォルダのパスを入力してください。")
    outputPath = sys.stdin.readline().strip()

    # outputPathがディレクトリかどうか確認するバリデータ
    while not isFileOrDirExsits(outputPath):
        printAlert("出力するフォルダのパス")
        outputPath = sys.stdin.readline().strip()
    
    with open(inputPath) as f:
        contents = f.read()

    with open(outputPath + fileName,'x') as f:
        f.write(contents[::-1])


# コマンドがcopyだった場合 inputpath にあるファイルのコピーを作成し、outputpath として保存します。
if command == "copy":
    print("出力するフォルダのパスを入力してください。")
    outputPath = sys.stdin.readline().strip()

    # outputPathがディレクトリかどうか確認するバリデータ
    while not isFileOrDirExsits(outputPath):
        printAlert("出力するフォルダのパス")
        outputPath = sys.stdin.readline().strip()
    
    with open(inputPath) as f:
        contents = f.read()

    with open(outputPath + fileName,'x') as f:
        f.write(contents)


# コマンドがduplicate-contentsだった場合 inputpath にあるファイルの内容を読み込み、その内容を複製し、複製された内容を inputpath に n 回複製します



# コマンドがreplace-stringだった場合　 inputpath' にあるファイルの内容から文字列 'needle' を検索し、'needle' の全てを 'newstring' に置き換えます。
