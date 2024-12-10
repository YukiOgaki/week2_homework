import datetime
import logging
import os
import sys
from dotenv import load_dotenv
from peewee import Model, IntegerField, CharField, TextField, TimestampField
from playhouse.db_url import connect

# .envの読み込み
load_dotenv(override=True)

# 実行したSQLをログで出力する設定
logger = logging.getLogger("peewee")
logger.addHandler(logging.StreamHandler())
# logger.setLevel(logging.DEBUG)

# データベースへの接続設定
db = connect(os.environ.get("DATABASE"))  # 環境変数に合わせて変更する場合


# メッセージのモデル
class User(Model):

    id = IntegerField(primary_key=True)  # idは自動で追加されるが明示
    user = CharField()
    age = IntegerField()
    pub_date = TimestampField(default=datetime.datetime.now())  # 何も指定しない場合は現在時刻が入る

    class Meta:
        database = db
        table_name = "SQLtool"


db.create_tables([User])
