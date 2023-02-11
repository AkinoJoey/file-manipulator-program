import sys
import os

def isFileOrDirExsits(path):
    if os.path.exists(path):
        return True
    else:
        print("ファイルまたはフォルダが存在しません。")
        print("正しいパスを入力してください。")
        return False

def printDone(command):
    print(command + "が完了しました。")

print("実行したいコマンドを入力してください。")
flag = False

# コマンドのバリデータ
while not flag:
    command = sys.stdin.readline().strip()

    if command == "reverse" or command == "copy" or command == "duplicate-contents" or command == "replace-string":
        flag = True
    else:
        print("正しいコマンドを入力してください。")

    
print("入力するファイルのパスを入力してください。")
inputPath = sys.stdin.readline().strip()

# inputPathのバリデータ
while not isFileOrDirExsits(inputPath):
    inputPath = sys.stdin.readline().strip()

# コマンドがreverseだった場合　inputpath にあるファイルを受け取り、outputpath に inputpath の内容を逆にした新しいファイルを作成します。
if command == "reverse":
    
    print("出力したいフォルダのパスを入力してください。")
    outputPathDir = sys.stdin.readline().strip()

    # outputPathがディレクトリかどうか確認するバリデータ
    while not isFileOrDirExsits(outputPathDir):
        outputPathDir = sys.stdin.readline().strip()

    fileName = inputPath[inputPath.rfind('\\'):] if os.name == "nt" else inputPath[inputPath.rfind('/'):]
    outputPath = outputPathDir + fileName
    
    if not os.path.exists(outputPath):
        with open(inputPath) as f:
            contents = f.read()

        with open(outputPath,'w') as f:
            f.write(contents[::-1])
            print(command)
    else:
        print("既に同じ名前のファイルが存在します。")

# コマンドがcopyだった場合 inputpath にあるファイルのコピーを作成し、outputpath として保存します。
if command == "copy":
    print("出力するファイルのパスを入力してください。")
    outputPath = sys.stdin.readline().strip()
    outputPathDir = outputPath[0:outputPath.rfind('\\')] if os.name == "nt" else outputPath[0:outputPath.rfind('/'):]

    # outputPathDirが存在するディレクトリかどうか確認するバリデータ
    while not isFileOrDirExsits(outputPathDir):
        outputPath = sys.stdin.readline().strip()
        outputPathDir = outputPath[0:outputPath.rfind('\\'):] if os.name == "nt" else outputPath[0:outputPath.rfind('/'):]
    
    if not os.path.exists(outputPath):
        with open(inputPath) as f:
            contents = f.read()

        with open(outputPath,'w') as f:
            f.write(contents)
            printDone(command)
    else:
        print("既に同じ名前のファイルが存在します。")

# コマンドがduplicate-contentsだった場合 inputpath にあるファイルの内容を読み込み、その内容を複製し、複製された内容を inputpath に n 回複製します
if command == "duplicate-contents":
    print("複製する回数を入力してください。")
    flag = False

    while not flag:
        copyTimes = sys.stdin.readline().strip()

        if copyTimes.isnumeric() and isinstance(int(copyTimes),int):
            flag = True
        else:
            print("整数を入力してください。")
            
    with open(inputPath) as f:
        contents = f.read()

    for i in range(int(copyTimes)):
        with open(inputPath,'a') as f:
            f.write(contents)

    printDone(command)
        

# コマンドがreplace-stringだった場合　 inputpath' にあるファイルの内容から文字列 'needle' を検索し、'needle' の全てを 'newstring' に置き換えます。
if command == "replace-string":
    print("置換後の文字列を入力してください。")
    newString = sys.stdin.readline().strip()

    with open(inputPath) as f:
        contents = f.read()

    with open(inputPath,'w') as f:
        f.write(contents.replace("needle",newString))

    printDone(command)
