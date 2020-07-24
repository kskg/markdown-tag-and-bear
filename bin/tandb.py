import re
import os
import logging
import random
import pathlib
import string
import glob
import shutil


# logging.basicConfig(level=logging.DEBUG, format='%(message)s')


class Tag:
    """マークダウンファイルを操作する

    Args:
        source (str): 入力元のファイル名
        destination (str): 出力先のファイル名
        extensions (list): 対象の拡張子
    """
    source = ''
    destination = ''
    extensions = []


    def __init__(self, source, destination, extensions):
        self.source = '../' + source
        self.destination = '../' + destination
        self.extensions = ['.' + extension for extension in extensions]

        # 必要なディレクトリを作成し、入力ソースを複製する
        if not os.path.isdir(self.source):
            os.mkdir(self.source)
        if os.path.isdir(self.destination):
            shutil.rmtree(self.destination)
        shutil.copytree(self.source, self.destination)


    def add_tag(self):
        """テキストファイルの末尾に、カレントディレクトリからの相対パスをハッシュタグとして追加する
        """
        paths = glob.glob(self.destination + '/**', recursive=True)
        for path in paths:

            # ファイル以外、対象外の拡張子、第一階層に属する場合は次のループに移る
            if not os.path.isfile(path):
                continue
            if not os.path.splitext(path)[1] in self.extensions:
                continue
            if os.path.dirname(path) == self.destination:
                continue

            # ファイルの更新日、最後に開いた日を取得
            update_time = pathlib.Path(path).stat().st_mtime
            opened_time = pathlib.Path(path).stat().st_atime

            # パスの文字列からハッシュタグを生成し、ファイルに追記する
            tag_name = '#' + os.path.dirname(path).lstrip(self.destination + '/').replace(' ', '_')
            with open(path, 'a') as file:
                file.write('\n\n')
                file.write(tag_name)

            # ファイルの更新日、最後に開いた日を追記前の日付に戻す
            os.utime(path, (opened_time, update_time))


    def check_exists(self, source, destination):
        """出力先に同名のファイル名があるかチェックし、あればファイル名に番号を付けたものを返す

        Args:
            source (str): 入力元のパス
            destination (str): 出力先のパス

        Returns:
            str: 元のファイル名 or 最新の番号がついたファイル名
        """
        file_name = os.path.splitext(source)[0]
        file_extension = os.path.splitext(source)[1]
        re_contain_number = r' \((\d+)\)$'

        if os.path.isfile(source):
            logging.debug('同名ファイルがある')

            if re.search(re_contain_number, file_name):
                logging.debug('ファイルに番号が振られている')
                # ファイルに振られた番号に1を足して、もう一度同名ファイルがあるか確認する
                file_number = int(re.search(re_contain_number, file_name).group(1))
                new_file_number = ' (' + str(file_number+1) + ')'
                new_path = re.sub(re_contain_number, new_file_number, file_name) + file_extension
                return (self.check_exists(new_path, destination))

            else:
                logging.debug('ファイルに番号が振られていない')
                # ファイルに番号を振って、もう一度同名ファイルがあるか確認する
                new_path = file_name + ' (1)' + file_extension
                return (self.check_exists(new_path, destination))

        else:
            logging.debug('同名ファイルがない')
            return source


    def collect_file(self):
        """入力ディレクトリに含まれる全てのファイルを、１つのディレクトリに集める
        """
        temporary_directory = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(20)])
        os.mkdir(temporary_directory)

        dest_paths = glob.glob(self.destination + '/**', recursive=True)
        for dest_path in dest_paths:

            # ファイル以外、対象外の拡張子の場合は次のループに移る
            if not os.path.isfile(dest_path):
                continue
            if not os.path.splitext(dest_path)[1] in self.extensions:
                continue
            
            # ディレクトリ階層を維持せず、ファイルを一箇所に集める
            file_name = os.path.basename(dest_path)
            temp_path = temporary_directory + '/' + file_name
            unique_temp_path = self.check_exists(temp_path, temporary_directory)
            shutil.copy2(dest_path, unique_temp_path)


        shutil.rmtree(self.destination)
        os.rename(temporary_directory, self.destination)