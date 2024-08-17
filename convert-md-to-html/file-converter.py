import sys
import os
import markdown

def check_args(args):
  # 引数の数
  if len(args) < 4:
    sys.exit("引数の数が不適です")
  
  # markdownか判別
  command = args[1]
  if command != "markdown":
    sys.exit(f"第1引数に{command}は不適です")
  
  # 使用するファイルのチェック
  input_file = args[2]
  input_ext_pair = os.path.splitext(input_file)

  if not os.access(input_file, os.R_OK):
    sys.exit(f"{input_file}は読み込み不可能です")
  elif input_ext_pair[-1] != ".md":
    input_file = input_ext_pair[0] + ".md"
  
  output_file = args[3]
  output_ext_pair = os.path.splitext(output_file)
  
  if output_ext_pair[-1] != ".html":
    output_file = output_ext_pair[0] + ".html"
  
  return input_file, output_file

# 変換関数
def convert_md_to_html(args):

  if check_args(args):
    input,output = check_args(args)

    with open(input, "r") as f1:
      with open(output, "w") as f2:
        content = f1.read()
        html = markdown.markdown(content)
        f2.write(html)
    
    
convert_md_to_html(sys.argv) 