from cassandra import ConsistencyLevel
from uuid import UUID
from datetime import datetime
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement


class Column:

    def __init__(self, name, type, is_null=True, primary_key=False):
        self.name = name
        self.type = type
        self.is_null = is_null,
        self.primary_key = primary_key


class EntityModel:

    def __init__(self, id, name):
        self.id = id
        self.name = name


cluster = Cluster(['127.0.0.1'])
session = cluster.connect('dbbuilder')

cluster.register_user_type('dbbuilder', 'entity_column', Column)
cluster.register_user_type('dbbuilder', 'file_column', Column)
cluster.register_user_type('dbbuilder', 'entity_model', EntityModel)

""" DATA INSERT  """

insert_user_command = SimpleStatement("INSERT INTO users (username, password) VALUES (%s, %s)")

session.execute(insert_user_command,
                ('artemkovtun', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5'),
                ConsistencyLevel.EACH_QUORUM)
session.execute(insert_user_command,
                ('supermario', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5'),
                ConsistencyLevel.ALL)
session.execute(insert_user_command,
                ('jamesmartins', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5'),
                ConsistencyLevel.THREE)

users = session.execute("SELECT * FROM users", [], ConsistencyLevel.ONE)

insert_file_command = SimpleStatement("INSERT INTO files (id, name, created_on, columns) VALUES (%s, %s, %s, %s)")

session.execute(insert_file_command, (UUID('E001222E-8AD9-49F2-BB1A-C0B6A54A6A77'), 'data.xlsx', datetime.now(), {
    "main": [
        Column("id", "integer"),
        Column("birthdate", "datetime")
    ]
}), ConsistencyLevel.ANY)
session.execute(insert_file_command,
                (UUID('9353E549-21D6-40CC-A61E-CEADA0187C69'), 'awesome table.xlsx', datetime.now(), {
                    "users": [
                        Column("firstname", "varchar2"),
                        Column("middlename", "varchar2"),
                        Column("lastname", "varchar2")
                    ],
                    "companies": [
                        Column("id", "guid"),
                        Column("name", "varchar2")
                    ]
                }), ConsistencyLevel.TWO)
session.execute(insert_file_command, (UUID('382EF0BB-22E9-4BF8-836B-2C24D4E2CD1D'), 'customers.xlsx', datetime.now(), {
    "main": [
        Column('id', 'integer'),
        Column('fullname', 'varchar2'),
        Column('email', 'varchar2')
    ]
}), ConsistencyLevel.LOCAL_QUORUM)

files = session.execute("SELECT * FROM files", [], ConsistencyLevel.SERIAL)

insert_files_by_username_command = SimpleStatement("INSERT INTO files_by_username "
                                                   "(username, file_id, file_name) VALUES (%s, %s, %s)")

session.execute(insert_files_by_username_command,
                ('artemkovtun', UUID('9353E549-21D6-40CC-A61E-CEADA0187C69'), 'awesome table.xlsx'),
                ConsistencyLevel.LOCAL_ONE)
session.execute(insert_files_by_username_command,
                ('jamesmartins', UUID('382EF0BB-22E9-4BF8-836B-2C24D4E2CD1D'), 'customers.xlsx'),
                ConsistencyLevel.ONE)
session.execute(insert_files_by_username_command,
                ('supermario', UUID('E001222E-8AD9-49F2-BB1A-C0B6A54A6A77'), 'data.xlsx'),
                ConsistencyLevel.QUORUM)

files_by_username = session.execute("SELECT * FROM files_by_username", [], ConsistencyLevel.THREE)

insert_schema_command = SimpleStatement("INSERT INTO schemas (id, name, created_on, entities_quantity, entities) "
                                        "VALUES (%s, %s, %s, %s, %s)")

session.execute(insert_schema_command, (UUID('61D59D93-850A-465A-91F0-F3C73B89555C'), 'university', datetime.now(), 2, {
    EntityModel(UUID('695A73AE-AC2F-43EF-BED5-924E6E22ED85'), 'users'),
    EntityModel(UUID('79584579-A4E0-4B27-A35B-419307097B98'), 'groups')
}), ConsistencyLevel.LOCAL_QUORUM)
session.execute(insert_schema_command, (UUID('D211043E-4C09-4572-BE5F-A2A214B0E942'), 'library', datetime.now(), 3, {
    EntityModel(UUID('8EBD06CE-FE15-4D1F-AC36-0E58A1A0A1AE'), 'books'),
    EntityModel(UUID('BC4885AF-B47A-4C0B-8D06-EC37F759F3FD'), 'authors'),
    EntityModel(UUID('5420D537-AC6C-4298-B69B-3E7B42B0D7C4'), 'bookAuthor')
}), ConsistencyLevel.ALL)
session.execute(insert_schema_command, (UUID('D31C14B0-775B-4821-A26C-5D15553156B0'), 'messenger', datetime.now(), 1, {
    EntityModel(UUID('3BC764D3-33F9-4588-AC10-0001B668B2F1'), 'messages')
}), ConsistencyLevel.TWO)

schemas = session.execute("SELECT * FROM schemas", [], ConsistencyLevel.LOCAL_ONE)

insert_schema_by_username_command = SimpleStatement("INSERT INTO schemas_by_username "
                                                    "(username, schema_id, schema_name, created_on) VALUES (%s, %s, %s, %s)")

session.execute(insert_schema_by_username_command,
                ('artemkovtun', UUID('61D59D93-850A-465A-91F0-F3C73B89555C'), 'university', datetime.now()),
                ConsistencyLevel.ONE)
session.execute(insert_schema_by_username_command,
                ('supermario', UUID('D211043E-4C09-4572-BE5F-A2A214B0E942'), 'library', datetime.now()),
                ConsistencyLevel.TWO)
session.execute(insert_schema_by_username_command,
                ('jamesmartins', UUID('D31C14B0-775B-4821-A26C-5D15553156B0'), 'messenger', datetime.now()),
                ConsistencyLevel.THREE)

schemas_by_username = session.execute("SELECT * FROM schemas_by_username", [], ConsistencyLevel.LOCAL_SERIAL)

insert_entity_command = SimpleStatement("INSERT INTO entities (id, name, column_id, column) VALUES (%s, %s, %s, %s)")

session.execute(insert_entity_command, (UUID('695A73AE-AC2F-43EF-BED5-924E6E22ED85'), 'users',
                                        UUID('A6499336-21CE-4636-BCD6-984977A67FA0'),
                                        Column('username', 'nvarchar2(50)', False, True)), ConsistencyLevel.ALL)
session.execute(insert_entity_command, (UUID('695A73AE-AC2F-43EF-BED5-924E6E22ED85'), 'users',
                                        UUID('DE8E898D-1F23-4AE8-8A51-ED5BAF2EB86E'),
                                        Column('password', 'nvarchar2(32)', False, False)),
                ConsistencyLevel.EACH_QUORUM)
session.execute(insert_entity_command, (UUID('695A73AE-AC2F-43EF-BED5-924E6E22ED85'), 'users',
                                        UUID('23E48255-37EB-40AF-8EED-D49BF338A221'),
                                        Column('email', 'nvarchar2(50)', True, False)), ConsistencyLevel.QUORUM)
session.execute(insert_entity_command, (UUID('79584579-A4E0-4B27-A35B-419307097B98'), 'groups',
                                        UUID('1EB57115-75F8-4315-9CC9-0FB274582FC3'),
                                        Column('id', 'uuid', False, True)), ConsistencyLevel.LOCAL_QUORUM)
session.execute(insert_entity_command, (UUID('79584579-A4E0-4B27-A35B-419307097B98'), 'groups',
                                        UUID('F1AB7475-7AE6-41D3-A6CA-AB1DB79572DE'),
                                        Column('title', 'nvarchar2(50)', False, False)), ConsistencyLevel.ONE)
session.execute(insert_entity_command, (UUID('8EBD06CE-FE15-4D1F-AC36-0E58A1A0A1AE'), 'books',
                                        UUID('692F9E36-D9EB-45AC-9C47-9307AB82AF10'),
                                        Column('id', 'uuid', False, True)), ConsistencyLevel.TWO)
session.execute(insert_entity_command, (UUID('8EBD06CE-FE15-4D1F-AC36-0E58A1A0A1AE'), 'books',
                                        UUID('4880C220-E623-486F-BCA7-4E979A5523ED'),
                                        Column('title', 'nvarchar2(50)', False, False)), ConsistencyLevel.THREE)
session.execute(insert_entity_command, (UUID('8EBD06CE-FE15-4D1F-AC36-0E58A1A0A1AE'), 'books',
                                        UUID('27E93BB3-7E80-4728-90D7-F6F2733AD3B8'),
                                        Column('email', 'nvarchar2(50)', True, False)), ConsistencyLevel.LOCAL_ONE)
session.execute(insert_entity_command, (UUID('BC4885AF-B47A-4C0B-8D06-EC37F759F3FD'), 'authors',
                                        UUID('86A3F24B-5003-474E-A743-230467CADC06'),
                                        Column('id', 'uuid', False, True)), ConsistencyLevel.ANY)
session.execute(insert_entity_command, (UUID('BC4885AF-B47A-4C0B-8D06-EC37F759F3FD'), 'authors',
                                        UUID('2964CFDF-569F-496F-8EB8-7666CD658149'),
                                        Column('firstname', 'nvarchar2(50)', True, False)), ConsistencyLevel.TWO)
session.execute(insert_entity_command, (UUID('BC4885AF-B47A-4C0B-8D06-EC37F759F3FD'), 'authors',
                                        UUID('5FECA1EB-09C3-47A0-920E-07182604F168'),
                                        Column('lastname', 'nvarchar2(50)', False, False)), ConsistencyLevel.ANY)
session.execute(insert_entity_command, (UUID('5420D537-AC6C-4298-B69B-3E7B42B0D7C4'), 'bookAuthor',
                                        UUID('181278EE-04BE-45BB-B6F7-6755A6D259B1'),
                                        Column('bookId', 'uuid', False, True)), ConsistencyLevel.LOCAL_ONE)
session.execute(insert_entity_command, (UUID('5420D537-AC6C-4298-B69B-3E7B42B0D7C4'), 'bookAuthor',
                                        UUID('76F33DA5-0796-4AC5-B8F6-F6654D685D77'),
                                        Column('authorId', 'uuid', False, True)), ConsistencyLevel.QUORUM)
session.execute(insert_entity_command, (UUID('3BC764D3-33F9-4588-AC10-0001B668B2F1'), 'messages',
                                        UUID('D481E06C-9736-43B0-94E7-91A41379F64A'),
                                        Column('id', 'uuid', False, True)), ConsistencyLevel.ALL)
session.execute(insert_entity_command, (UUID('3BC764D3-33F9-4588-AC10-0001B668B2F1'), 'messages',
                                        UUID('80CC1591-5381-4378-BF12-FCA68C19B507'),
                                        Column('text', 'nvarchar2(', False, False)), ConsistencyLevel.LOCAL_QUORUM)
session.execute(insert_entity_command, (UUID('3BC764D3-33F9-4588-AC10-0001B668B2F1'), 'messages',
                                        UUID('4A4266CF-AA9C-47CD-9282-BDE3CB2E895F'),
                                        Column('sender', 'uuid', False, False)), ConsistencyLevel.ANY)
session.execute(insert_entity_command, (UUID('3BC764D3-33F9-4588-AC10-0001B668B2F1'), 'messages',
                                        UUID('A2EA5220-E2B4-4CA4-A00E-7D124D971A2C'),
                                        Column('receiver', 'uuid', False, False)), ConsistencyLevel.ANY)

entities = session.execute("SELECT * FROM entities", [], ConsistencyLevel.LOCAL_QUORUM)

""" DATA UPDATE  """

session.execute("UPDATE users SET password = '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92' "
                "WHERE username = 'artemkovtun'", [], ConsistencyLevel.QUORUM)
session.execute("UPDATE users SET password = '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92' "
                "WHERE username = 'supermario'", [], ConsistencyLevel.ONE)
session.execute("UPDATE users SET password = '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92' "
                "WHERE username = 'jamesmartins'", [], ConsistencyLevel.LOCAL_QUORUM)

updated_users = session.execute("SELECT * FROM users")

session.execute("UPDATE files SET name = 'new_name.xlsx' WHERE id = E001222E-8AD9-49F2-BB1A-C0B6A54A6A77", [],
                ConsistencyLevel.THREE)
session.execute("UPDATE files SET columns['users'] = [ "
                "   {name:'firstname', type: 'nvarchar2'},"
                "   {name:'middlename', type: 'nvarchar2'},"
                "   {name:'lastname', type :'timestamp'}"
                "] WHERE id = 9353E549-21D6-40CC-A61E-CEADA0187C69", [], ConsistencyLevel.ANY)
session.execute("UPDATE files SET created_on = toTimestamp(now()) WHERE id = 382EF0BB-22E9-4BF8-836B-2C24D4E2CD1D", [],
                ConsistencyLevel.LOCAL_ONE)

updated_files = session.execute("SELECT * FROM FILES")

session.execute("UPDATE files_by_username SET file_name = 'super awesome table.xlsx' "
                "WHERE username = 'artemkovtun' AND file_id = 9353e549-21d6-40cc-a61e-ceada0187c69", [],
                ConsistencyLevel.LOCAL_QUORUM)
session.execute("UPDATE files_by_username SET file_name = 'nodata.xlsx' "
                "WHERE username = 'supermario' AND file_id = e001222e-8ad9-49f2-bb1a-c0b6a54a6a77", [],
                ConsistencyLevel.TWO)
session.execute("UPDATE files_by_username SET file_name = 'my_customers.xlsx' "
                "WHERE username = 'jamesmartins' AND file_id = 382ef0bb-22e9-4bf8-836b-2c24d4e2cd1d;", [],
                ConsistencyLevel.ANY)

updated_files_by_username = session.execute("SELECT * FROM files_by_username")

session.execute("UPDATE schemas SET entities = entities + {{"
                "   id: 6E587581-F9D1-469A-AEA6-7445052895AC, "
                "   name:'userGroups' }} "
                "WHERE id = 61D59D93-850A-465A-91F0-F3C73B89555C", [], ConsistencyLevel.QUORUM)
session.execute("UPDATE schemas SET entities = entities - {{"
                "   id: 5420D537-AC6C-4298-B69B-3E7B42B0D7C4, "
                "   name:'bookAuthor' }} "
                "WHERE id = D211043E-4C09-4572-BE5F-A2A214B0E942", [], ConsistencyLevel.LOCAL_QUORUM)
session.execute("UPDATE schemas SET name = 'superMessenger' WHERE id = D31C14B0-775B-4821-A26C-5D15553156B0;", [],
                ConsistencyLevel.LOCAL_ONE)

updated_schemas = session.execute("SELECT * FROM schemas")

session.execute("UPDATE schemas_by_username SET schema_name = 'superMessenger' "
                "WHERE username = 'jamesmartins' AND schema_id = D31C14B0-775B-4821-A26C-5D15553156B0", [],
                ConsistencyLevel.ONE)
session.execute("UPDATE schemas_by_username SET created_on = toTimestamp(now()) "
                "WHERE username = 'artemkovtun' AND schema_id = 61D59D93-850A-465A-91F0-F3C73B89555C", [],
                ConsistencyLevel.TWO)
session.execute("UPDATE schemas_by_username SET schema_name = 'mylibrary' "
                "WHERE username = 'supermario' AND schema_id = D31C14B0-775B-4821-A26C-5D15553156B0", [],
                ConsistencyLevel.THREE)

updated_schemas_by_username = session.execute("SELECT * FROM schemas_by_username")

session.execute("UPDATE entities SET name = 'usersinfo' WHERE id = 695A73AE-AC2F-43EF-BED5-924E6E22ED85", [],
                ConsistencyLevel.LOCAL_ONE)
session.execute("UPDATE entities SET column = {"
                "   name: 'lastname',  "
                "   type: 'nvarchar2(100)', "
                "   is_null: false, "
                "   primary_key:false"
                "} WHERE id = BC4885AF-B47A-4C0B-8D06-EC37F759F3FD AND "
                "        column_id = 5feca1eb-09c3-47a0-920e-07182604f168", [], ConsistencyLevel.ALL)
session.execute("UPDATE entities SET column = {"
                "   name: 'name', "
                "   type: 'nvarchar2(50)', "
                "   is_null: false, "
                "   primary_key: false"
                "} WHERE id =79584579-a4e0-4b27-a35b-419307097b98 AND "
                "        column_id = f1ab7475-7ae6-41d3-a6ca-ab1db79572de", [], ConsistencyLevel.ANY)

updated_entities = session.execute("SELECT * FROM entities")

""" CUSTOM QUERIES """

artemkovtun_files = session.execute("SELECT json file_id, file_name FROM files_by_username "
                                    "WHERE username = 'artemkovtun'", [], ConsistencyLevel.LOCAL_QUORUM)
file = session.execute("SELECT json name, columns FROM files WHERE id = 9353E549-21D6-40CC-A61E-CEADA0187C69", [],
                       ConsistencyLevel.LOCAL_ONE)
artemkovtun_schemas = session.execute("SELECT json schema_id, schema_name, created_on FROM schemas_by_username "
                                      "WHERE username = 'artemkovtun'", [], ConsistencyLevel.SERIAL)
schema = session.execute("SELECT json name, created_on, entities FROM schemas "
                         "WHERE id = 61D59D93-850A-465A-91F0-F3C73B89555C", [], ConsistencyLevel.ALL)

""" DATA DELETE  """

delete_user_command = session.prepare("DELETE FROM users WHERE username = ?")

session.execute(delete_user_command, ['artemkovtun'])
session.execute(delete_user_command, ['supermario'])
session.execute(delete_user_command, ['jamesmartins'])

delete_file_command = session.prepare("DELETE FROM files WHERE id = ?")

session.execute(delete_file_command, [UUID('E001222E-8AD9-49F2-BB1A-C0B6A54A6A77')])
session.execute(delete_file_command, [UUID('9353E549-21D6-40CC-A61E-CEADA0187C69')])
session.execute(delete_file_command, [UUID('382EF0BB-22E9-4BF8-836B-2C24D4E2CD1D')])

delete_file_by_username_command = session.prepare("DELETE FROM files_by_username WHERE username = ?")

session.execute(delete_file_by_username_command, ['artemkovtun'])
session.execute(delete_file_by_username_command, ['supermario'])
session.execute(delete_file_by_username_command, ['jamesmartins'])

delete_schema_command = session.prepare("DELETE FROM schemas WHERE id = ?")

session.execute(delete_schema_command, [UUID('61D59D93-850A-465A-91F0-F3C73B89555C')])
session.execute(delete_schema_command, [UUID('D211043E-4C09-4572-BE5F-A2A214B0E942')])
session.execute(delete_schema_command, [UUID('D31C14B0-775B-4821-A26C-5D15553156B0')])

delete_schema_by_username_command = session.prepare("DELETE FROM schemas_by_username WHERE username = ?")

session.execute(delete_schema_by_username_command, ['artemkovtun'])
session.execute(delete_schema_by_username_command, ['supermario'])
session.execute(delete_schema_by_username_command, ['jamesmartins'])

delete_entity_by_username = session.prepare("DELETE FROM entities WHERE id = ?")

session.execute(delete_schema_command, [UUID('695A73AE-AC2F-43EF-BED5-924E6E22ED85')])
session.execute(delete_schema_command, [UUID('79584579-A4E0-4B27-A35B-419307097B98')])
session.execute(delete_schema_command, [UUID('8EBD06CE-FE15-4D1F-AC36-0E58A1A0A1AE')])
session.execute(delete_schema_command, [UUID('BC4885AF-B47A-4C0B-8D06-EC37F759F3FD')])
session.execute(delete_schema_command, [UUID('5420D537-AC6C-4298-B69B-3E7B42B0D7C4')])
session.execute(delete_schema_command, [UUID('3BC764D3-33F9-4588-AC10-0001B668B2F1')])
