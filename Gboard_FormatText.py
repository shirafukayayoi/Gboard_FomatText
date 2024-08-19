import zipfile
import os

file_path = input('ファイルパスを入力してください: ')

if not os.path.exists(file_path):
    print("エラー: 指定されたファイルが存在しません。")
else:
    zip_file_name = os.path.splitext(file_path)[0] + ".zip"

    try:
        with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(file_path, os.path.basename(file_path))
        
        print(f"ZIPファイルの作成が完了しました: {zip_file_name}")
        
    except Exception as e:
        print(f"エラーが発生しました: {e}")
