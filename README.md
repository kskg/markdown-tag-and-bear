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
- ファイルのタイムスタンプは維持されます。 <sup><a name="1">[^1](#notes_1)</a></sup>
- 入力ソースのディレクトリ構造を維持する or 維持しないを選択できます。 <sup><a name="2">[^2](#notes_2)</a></sup>
- ディレクトリ構造を維持しない場合、ファイルは１つのディレクトリに集められます。 <sup><a name="3">[^3](#notes_3)</a></sup>

## 使い方
- Terminalでマークダウンファイルを含むディレクトリを`/tag-and-bear/src`にコピーする（Finderでも可）
```
cp ~/Desktop/develop ~/Desktop/tag-and-bear/src
```

- Terminalで`/tag-and-bear/bin`に移動する
```
cd ~/Desktop/tag-and-bear/bin
```

- Terminalで`main.py`を実行する
```
python main.py
```

- `/tag-and-bear/dest`に出力される

## 開発環境
- MacOS 10.15.5
- Python 3.7.5

現時点ではWindows/Linuxで恐らく動作しませんが、アップデートで対応する予定です。

## 開発背景
Mac Appのマークダウンエディタ[Bear](https://bear.app)に、大量のマークダウンファイルを一括でインポートしようとしました。  
しかし、インポート後に問題がある事に気づきました。

- Bearのインポート機能ではサブディレクトリが認識されない。
- ディレクトリ毎にインポートするか、全てのファイルを１箇所に集める必要がある。
- インポートされたメモが「タグなし」に分類される。
- 元のディレクトリ構造を再現するには手動でタグを付ける必要がある。

4つ目の問題に関してはメモを複数選択して一括でタグを付ける事はできました。  
しかし、先にタグを用意しておく必要があって、ディレクトリの数がそれなりにあるので自動化したいという思いが強かったのです。

これらを解決するために、以前から興味のあったPythonの勉強も兼ねて、はじめてPythonでプログラムを書いてみました。  
一人でも多く同じ問題に悩む人がいなくなる事を願います🐻

## 注意事項
Pythonの勉強をしながら作成したため、意図しない動作や不具合が起こる可能性があります。  
そのため使用は自己責任でお願いします。使用の際はバックアップをとることをオススメします。

## 注釈
<a name="notes_1">[^1](#1)</a>: 正確にはハッシュタグを追記する前に、ファイルの更新日と最後に開いた日を取得して、追記した後に元に戻しています。  
<a name="notes_2">[^2](#2)</a>: デフォルトでは維持する設定になっています。設定は（`settings.ini`）から変更できます。  
<a name="notes_3">[^3](#3)</a>: ファイル名が被る場合はファイル名に番号が振られます。

## 作者
kskg
- [GitHub](https://github.com/kskg)
- [Twitter](https://github.com/kskg)

## ライセンス
MIT