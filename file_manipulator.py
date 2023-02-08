import sys
import os

# command = argv[2]
# inputpath = argv[3]
# outputpath = argv[4]

# inputpath = /home/yuki-gakiya/mydir/text-file/test2.txt
# outputpath = /home/yuki-gakiya/mydir/output-file-for-test

if len(sys.argv) < 4:
    print("正確なコマンド, 第1引数，第2引数を入力してください。")
    sys.exit()

command = sys.argv[1]

if command == "reverse":
    inputpath = sys.argv[2]
    outputpath = sys.argv[3]

    # inputpathがファイルじゃなかった場合
    if not os.path.isfile(inputpath):
        print("入力するファイルの正しいパスを入力してください。")
        sys.exit()
    
    fileName = inputpath[inputpath.rfind('/'):]
    # outputpathがフォルダじゃなかった場合
    if not os.path.isdir(outputpath):
        print("出力する正しいフォルダのパスを入力してください。")
        sys.exit()
    
    with open(inputpath) as f:
        contents = f.read()
    
    with open(outputpath + fileName,'x') as f:
        f.write(contents[::-1])

else:
    print("miss")


