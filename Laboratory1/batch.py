from uuid import uuid4
from datetime import datetime
from cassandra.cluster import Cluster
from cassandra.query import BatchStatement

cluster = Cluster(['127.0.0.1'])
session = cluster.connect('dbbuilder')

insert_file_command = session.prepare(
    "INSERT INTO files (id, name, created_on, columns) VALUES (?, ?, ?, ?)")
insert_files_by_username_command = session.prepare(
    "INSERT INTO files_by_username (username, file_id, file_name) VALUES (?, ?, ?)")

insert_file_batch = BatchStatement()

username = 'artemkovtun'
file_id = uuid4()
file_name = 'test.xlsx'
creation_date = datetime.now()
columns = {}


insert_file_batch.add(insert_file_command, (file_id, file_name, creation_date, columns))
insert_file_batch.add(insert_files_by_username_command, (username, file_id, file_name))

session.execute(insert_file_batch)
