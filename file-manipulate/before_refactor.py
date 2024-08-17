
# reverse inputpath outputpath: inputpath にあるファイルを受け取り、outputpath に inputpath の内容を逆にした新しいファイルを作成します。
# copy inputpath outputpath: inputpath にあるファイルのコピーを作成し、outputpath として保存します。
# duplicate-contents inputpath n: inputpath にあるファイルの内容を読み込み、その内容を複製し、複製された内容を inputpath に n 回複製します。
# replace-string inputpath needle newstring: inputpath にあるファイルの内容から文字列 'needle' を検索し、'needle' の全てを 'newstring' に置き換えます。

import sys,os

def isReadbleInputFile(filepath):
  if os.access(filepath, os.R_OK):
     return True
  else:
     return False

def isWritableInputFile(filepath):
  if os.access(filepath, os.W_OK):
     return True
  else:
     return False
    
def isPositiveNumber(input):
  if type(input) == int and input > 0:
    return True
  else:
     return False
     

def validateFirstArgument(str):
  if str in ["reverse", "copy", "duplicate-contents", "replace-string"]:
     return True
  else:
     return False
  
def reverseCommandChecker(argvList):
  if len(argvList) != 3:
      sys.exit("引数の数が不適です")
  elif not isReadbleInputFile(argvList[2]):
     sys.exit("ファイルが読み込み不可能です")
  elif not isWritableInputFile(argvList[3]):
     sys.exit("ファイルが書き込み不可能です")
  else:
     return True

def copyCommandChecker(argvList):
  if len(argvList) != 3:
      sys.exit("引数の数が不適です")
  elif not isReadbleInputFile(argvList[2]):
     sys.exit("ファイルが読み込み不可能です")
  elif not isWritableInputFile(argvList[3]):
     sys.exit("ファイルが書き込み不可能です")
  else:
     return True

def duplicateCommandChecker(argvList):
  if len(argvList) != 3:
      sys.exit("引数の数が不適です")
  elif not isReadbleInputFile(argvList[2]):
     sys.exit("ファイルが読み込み不可能です")
  elif not isPositiveNumber(int(argvList[2])):
     sys.exit("1以上の整数を指定してください")
  else:
     return True

def replaceCommandChecker(argvList):
  if len(argvList) != 4:
      sys.exit("引数の数が不適です")
  elif not isReadbleInputFile(argvList[2]):
     sys.exit("ファイルが読み込み不可能です")
  else:
     return True

def commandChecker(argvList):
  if len(argvList) < 3:
    sys.exit("スクリプトに与える引数の数が不適です")
  elif not validateFirstArgument(argvList[1]):
    sys.exit("スクリプトに与える第1引数が不正です")
  elif argvList[1] == "reverse":
    if not reverseCommandChecker(sys.argv):
      sys.exit("reverseコマンドを実行できません。")
    else:
      print("reverse")
  elif argvList[1] == "copy":
    if not copyCommandChecker(sys.argv):
      sys.exit("copyコマンドを実行できません。")
    else:
      print("copy")
  elif argvList[1] == "duplicate-contents":
    if not duplicateCommandChecker(sys.argv):
      sys.exit("duplicate-contentsコマンドを実行できません。")
    else:
      print("duplicate-contents")
  elif argvList[1] == "replace-string":
    if not reverseCommandChecker(sys.argv):
      sys.exit("replace-stringコマンドを実行できません。")
    else:
      print("replace-string")
  
      
commandChecker(sys.argv)