📖 English / [Japanese](./README_JP.md)  
  
# Tag & Bear
![Cover image](cover.jpg)
Photo by [Hans-Jurgen Mager](https://unsplash.com/@hansjurgen007?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText) on [Unsplash](https://unsplash.com/t?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText)

## Overview
This is a script to add the relative path from the current directory to the end of the markdown file as a hashtag (#tag/sub_tag).
The hashtags are added with the following specifications.

e.g.
- `. /readme.md` will not be added.
- `. /develop/readme.md` is appended to `readme.md` with `#develop` at the end.
- `. /develop/python/readme.md` is appended to `readme.md` with `#develop/python` at the end.

## Features
- If the hashtag contains a space ` `, it will be replaced with an underbar `_`.
- The file's timestamp is preserved. <sup><a name="1">[^1](#notes_1)</a></sup>
- You can choose to "keep" or "not keep" the input source directory structure. <sup><a name="2">[^2](#notes_2)</a></sup>
- If you choose "Don't keep" directory structure, the files are collected in one directory. <sup><a name="3">[^3](#notes_3)</a></sup>

## Usage.
- Switch to Python 3.7.5 or higher
- Copy the directory containing the markdown file to `/tag-and-bear/src`.
- Go to `/tag-and-bear/bin` on the terminal and run `main.py`.
- Output to `/tag-and-bear/dest`.

e.g.
```
$ pyenv global 3.7.5
$ cp ~/MyDocuments/MyNote ~/Desktop/tag-and-bear/src
$ cd ~/Desktop/tag-and-bear/bin
$ python main.py
🐻 < Done!
```

## Development Environment
- MacOS 10.15.5
- Python 3.7.5

It probably won't work on Windows/Linux at this time, but it will be supported in an update.

## Development Background
I tried to import a large number of markdown files into the Mac App markdown editor [Bear] (https://bear.app) in bulk.  
However, I noticed that there was a problem after importing.

- Bear's import feature does not recognize subdirectories.
- You have to import each directory or collect all the files in one place.
- Imported notes are classified as "untagged".
- You need to tag them manually to recreate the original directory structure.

For the fourth problem, I was able to select multiple memos and tag them in batches.  
However, I had to prepare the tags ahead of time & I had a large number of directories, so I was keen to automate the process.

To solve these problems, I wrote a program in Python for the first time, as well as studying Python, which I had been interested in for some time.  
I hope that not even one more person suffers from the same problem 🐻

## Notes
Since I created it while studying Python, there is a possibility of unintended behavior and problems.  
Therefore, please use it at your own risk. We recommend you to back up the code when you use it.

## Footnotes
<a name="notes_1">[^1](#1)</a>: To be precise, we get the date the file was last modified and the date it was last opened before adding the hashtag, and then revert it back to its original state after we add it.
<a name="notes_2">[^2](#2)</a>: The default setting is to keep the file structure. You can change it from `settings.ini`.
<a name="notes_3">[^3](#3)</a>: The file name is numbered if the same file name exists in the output destination.

## Author
- [GitHub](https://github.com/kskg)
- [Twitter](https://twitter.com/kskg)

Please feel free to give me your comments and suggestions. We'll use it as a reference for development🤓

## License
MIT