import sys, os

# ファイルが読み込み可能か
def is_readable_file(filepath):
    return os.access(filepath, os.R_OK)

# 正の数か
def is_positive_number(input_str):
    try:
        num = int(input_str)
        return num > 0
    except ValueError:
        return False

# 第一引数が指定の文字列か
def validate_first_argument(command):
    return command in ["reverse", "copy", "duplicate-contents", "replace-string"]

# reverseだった時のバリデータ
def reverse_command_checker(args):
    if len(args) != 4:
        sys.exit("reverseコマンドの引数の数が不適です")
    elif not is_readable_file(args[2]):
      return sys.exit(f"{args[2]}は読み込み不可能です")
    else:
      return True

# 正常時の実行コマンド内容
def reverse_command(args):
  if reverse_command_checker(args):
    input_file = args[2]
    output_file = args[3]

    with open(input_file, 'r') as f1:
      with open(output_file, 'w') as f2:
        f2.write(f1.read()[::-1])

    print(f"文字列の反転が完了しました。{input_file} が反転されました。")

# copyだった時のバリデータ
def copy_command_checker(args):
    if len(args) != 4:
        sys.exit("copyコマンドの引数の数が不適です")
    elif not is_readable_file(args[2]):
      return sys.exit(f"{args[2]}は読み込み不可能です")
    else:
      return True

# 正常時の実行コマンド内容
def copy_command(args):
  if copy_command_checker(args):
    input_file = args[2]
    output_file = args[3]

    with open(input_file, 'r') as f1:
      with open(output_file, 'w') as f2:
        f2.write(f1.read())
    
    print(f"コピーが完了しました。{input_file} がコピーされました。")

# duplicateだった時のバリデータ
def duplicate_command_checker(args):
    if len(args) != 4:
        sys.exit("duplicate-contentsコマンドの引数の数が不適です")
    elif not is_readable_file(args[2]):
        sys.exit(f"入力ファイル '{args[2]}' が読み込み不可能です")
    elif not is_positive_number(args[3]):
        sys.exit("複製回数は1以上の整数を指定してください")
    else:
      return True

# 正常時の実行コマンド内容
def duplicate_command(args):
  if duplicate_command_checker(args):
    input_file = args[2]
    duplicate_num = int(args[3])

    with open(input_file, 'r+') as f1:
      f1.write(str(f1.read()) * duplicate_num)
      
    print(f"複製が完了しました。{input_file} が上書きされました。")

# replaceだった時のバリデータ
def replace_command_checker(args):
    if len(args) != 5:
        sys.exit("replace-stringコマンドの引数の数が不適です")
    elif not is_readable_file(args[2]):
        sys.exit(f"入力ファイル '{args[2]}' が読み込み不可能です")
    else:
      return True

# 正常時の実行コマンド内容
def replace_command(args):
    if replace_command_checker(args):
        input_file = args[2]
        target_string = args[3]
        replacement_string = args[4]
        
        # ファイルの内容を読み込む
        with open(input_file, "r") as f:
            content = f.read()
        
        if target_string not in content:
            sys.exit(f"{target_string}がファイル内に見つかりません")
        
        # 文字列置換を行う
        replaced_content = content.replace(target_string, replacement_string)
        
        # 元のファイルに上書きする
        with open(input_file, "w") as f:
            f.write(replaced_content)
        
        print(f"置換が完了しました。{input_file} が上書きされました。")

# 与えられたsys.argvを元に処理の振り分けを行い、確認、実行する関数      
def command_check_and_execute(args):
    if len(args) < 2:
        sys.exit("スクリプトに与える引数の数が不適です")
    
    command = args[1]
    if not validate_first_argument(command):
        sys.exit(f"スクリプトに与える第1引数 '{command}' が不正です")

    command_functions = {
        "reverse": reverse_command,
        "copy": copy_command,
        "duplicate-contents": duplicate_command,
        "replace-string": replace_command
    }

    command_functions[command](args)


# 処理の実行
command_check_and_execute(sys.argv)
