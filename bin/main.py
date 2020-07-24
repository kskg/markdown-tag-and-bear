import configparser

import tandb


# 設定の読み込み
settings = configparser.ConfigParser()
settings.read('settings.ini')

source = settings.get('DEFAULT', 'source')
destination = settings.get('DEFAULT', 'destination')
extensions = settings.get('DEFAULT', 'extensions').split(', ')
keep_directory_structure = settings.get('DEFAULT', 'keep_directory_structure') in ['True']

# 対象にタグを追加し、条件が合えばファイルを一箇所に集める
tandb = tandb.Tag(source, destination, extensions)
tandb.add_tag()
if keep_directory_structure == False:
    tandb.collect_file()

print('🐻< Done!')
