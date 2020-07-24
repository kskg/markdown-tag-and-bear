# Tag & Bear
![カバー画像](cover.jpg)
Photo by [Hans-Jurgen Mager](https://unsplash.com/@hansjurgen007?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText) on [Unsplash](https://unsplash.com/t?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText)

## 概要
マークダウンファイルの末尾に、カレントディレクトリからの相対パスをハッシュタグ（#tag/sub_tag）として一括で追記するスクリプトです。
ハッシュタグは以下の仕様で追記されます。

例：
- `./readme.md`は追記されない
- `./develop/readme.md`は`readme.md`の末尾に`#develop`が追記される
- `./develop/python/readme.md`は`readme.md`の末尾に`#develop/python`が追記される

## 特徴
- 追記される対象は、入力ソースに含まれるすべてのマークダウンファイルとテキストファイル（.md/.txt/.text）です。
- ファイルのタイムスタンプは、ハッシュタグが追記されても維持されます。（正確にはハッシュタグを追記する前に、ファイルの更新日と最後に開いた日を取得して追記した後に元に戻しています）
- 設定ファイル（`settings.ini`）を編集して、入力ソースのディレクトリ構造を維持するか維持しないかを選択できます。（デフォルトでは維持する設定になっています）
- ディレクトリの構造を維持しない場合、ファイルは１つのディレクトリに集められます。ファイル名が被る場合はファイル名に番号が振られます。

## 使い方
- マークダウンファイルを含むディレクトリを`/tag-and-bear/src`ディレクトリにコピーする
- Terminalで`/tag-and-bear/bin`に移動し`main.py`を実行する
- `/tag-and-bear/dest`ディレクトリに出力される

例：
```
cd ~/MyDocuments/tag-and-bear/bin
python main.py
```

## 開発環境
- MacOS 10.15.5
- Python 3.7.5
現時点ではWindows/Linuxで恐らく動作しませんが、アップデートで対応する予定です。

## 開発背景
Mac Appのマークダウンエディタ[Bear](https://bear.app)に、大量のマークダウンファイルを一括でインポートしようとしました。
しかし、インポート後に問題が２つある事に気づきました。

- Bearのインポート機能ではサブディレクトリが認識されず、ディレクトリ毎にインポートするか全てのファイルを１箇所に集める必要がある。
- インポートされたメモが「タグなし」に分類されるため、元のディレクトリ構造を再現するには手動でタグを付ける必要がある。

特に２つ目の問題に関しては、メモを複数選択して一括でタグを付ける事はできたものの、先にタグを用意しておく必要がありました。
自分の場合はディレクトリがそれなりにあったので、なんとか自動化したいという思いが強かったのです。

これらを解決するために、以前から興味のあったPythonの勉強も兼ねて、はじめてPythonのプログラムを書いてみました。
一人でも多く同じ問題に悩む人がいなくなる事を願います🐻

## 注意事項
Pythonの勉強をしながら作成したため、意図しない動作や不具合が起こる可能性があります。そのため使用は自己責任でお願いします。使用の際はバックアップをとることをオススメします。

## 作者
kskg
- [GitHub](https://github.com/kskg)
- [twitter](https://github.com/kskg)

## ライセンス
MIT