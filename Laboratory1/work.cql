// 3.1 CREATE DATA
insert into dbbuilder.users (username, password) values ('artemkovtun',  '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5');
insert into dbbuilder.users (username, password) values ('supermario',   '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5');
insert into dbbuilder.users (username, password) values ('jamesmartins', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5');

select json * from dbbuilder.users; 

insert into dbbuilder.files (id, name, created_on, columns) values (E001222E-8AD9-49F2-BB1A-C0B6A54A6A77, 'data.xlsx', toTimestamp(now()), {
	'main' : [
		{name:'id', type: 'integer'},
		{name:'birthdate', type :'datetime'}
	]
});
insert into dbbuilder.files (id, name, created_on, columns) values (9353E549-21D6-40CC-A61E-CEADA0187C69, 'awesome table.xlsx', toTimestamp(now()),{
	'users': [
		{name:'firstname', type: 'varchar2'},
		{name:'middlename', type: 'varchar2'},
		{name:'lastname', type :'varchar2'}
	],
	'companies': [
		{name:'id', type:'guid'},
		{name:'name', type:'varchar2(300)'}
	]
});
insert into dbbuilder.files (id, name, created_on, columns) values (382EF0BB-22E9-4BF8-836B-2C24D4E2CD1D, 'customers.xlsx', toTimestamp(now()),{ 
	'main':[
		{name:'id', type: 'integer'},
		{name:'fullname', type :'varchar2'},
		{name:'email', type :'texvarchar2t'}
	]
});

select json * from dbbuilder.files; 


insert into dbbuilder.files_by_username(username, file_id, file_name) values ('artemkovtun', 9353E549-21D6-40CC-A61E-CEADA0187C69, 'awesome table.xlsx');
insert into dbbuilder.files_by_username(username, file_id, file_name) values ('jamesmartins', 382EF0BB-22E9-4BF8-836B-2C24D4E2CD1D, 'customers.xlsx');
insert into dbbuilder.files_by_username(username, file_id, file_name) values ('supermario', E001222E-8AD9-49F2-BB1A-C0B6A54A6A77, 'data.xlsx');

select json * from dbbuilder.files_by_username;

insert into dbbuilder.schemas(id, name, created_on, entities_quantity, entities) values (61D59D93-850A-465A-91F0-F3C73B89555C, 'university', toTimestamp(now()), 2, {
	{id: 695A73AE-AC2F-43EF-BED5-924E6E22ED85, name:'users'},
	{id: 79584579-A4E0-4B27-A35B-419307097B98, name:'groups' }
});
insert into dbbuilder.schemas(id, name, created_on, entities_quantity, entities) values (D211043E-4C09-4572-BE5F-A2A214B0E942, 'library', toTimestamp(now()), 3, {
	{id: 8EBD06CE-FE15-4D1F-AC36-0E58A1A0A1AE, name:'books'},
	{id: BC4885AF-B47A-4C0B-8D06-EC37F759F3FD, name:'authors' },
	{id: 5420D537-AC6C-4298-B69B-3E7B42B0D7C4, name:'bookAuthor' }
});
insert into dbbuilder.schemas(id, name, created_on, entities_quantity, entities) values (D31C14B0-775B-4821-A26C-5D15553156B0, 'messenger', toTimestamp(now()), 1, {
	{id: 3BC764D3-33F9-4588-AC10-0001B668B2F1, name:'messages'  }
});
select json * from dbbuilder.schemas;

insert into dbbuilder.schemas_by_username (username, schema_id, schema_name, created_on) values ('artemkovtun',61D59D93-850A-465A-91F0-F3C73B89555C, 'university', toTimestamp(now()));
insert into dbbuilder.schemas_by_username (username, schema_id, schema_name, created_on) values ('supermario', D211043E-4C09-4572-BE5F-A2A214B0E942, 'library', toTimestamp(now()));
insert into dbbuilder.schemas_by_username (username, schema_id, schema_name, created_on) values ('jamesmartins', D31C14B0-775B-4821-A26C-5D15553156B0, 'messenger', toTimestamp(now()));

select json * from dbbuilder.schemas_by_username;

insert into dbbuilder.entities (id, name, column_id, column) values (695A73AE-AC2F-43EF-BED5-924E6E22ED85, 'users', A6499336-21CE-4636-BCD6-984977A67FA0 ,{name: 'username', type:'nvarchar2(50)', is_null:false, primary_key:true});
insert into dbbuilder.entities (id, name, column_id, column) values (695A73AE-AC2F-43EF-BED5-924E6E22ED85, 'users', DE8E898D-1F23-4AE8-8A51-ED5BAF2EB86E ,{name: 'password', type:'nvarchar2(32)', is_null:false, primary_key:false});
insert into dbbuilder.entities (id, name, column_id, column) values (695A73AE-AC2F-43EF-BED5-924E6E22ED85, 'users', 23E48255-37EB-40AF-8EED-D49BF338A221, {name: 'email',    type:'nvarchar2(50)', is_null:true,  primary_key:false});
insert into dbbuilder.entities (id, name, column_id, column) values (79584579-A4E0-4B27-A35B-419307097B98, 'groups', 1EB57115-75F8-4315-9CC9-0FB274582FC3, {name: 'id',   type: 'uuid', is_null: false, primary_key: true});
insert into dbbuilder.entities (id, name, column_id, column) values (79584579-A4E0-4B27-A35B-419307097B98, 'groups', F1AB7475-7AE6-41D3-A6CA-AB1DB79572DE , {name: 'title',type: 'nvarchar2(50)', is_null:false, primary_key:false});
insert into dbbuilder.entities (id, name, column_id, column) values (8EBD06CE-FE15-4D1F-AC36-0E58A1A0A1AE, 'books', 692F9E36-D9EB-45AC-9C47-9307AB82AF10, {name: 'id',    type:'uuid', 		  is_null:false,  primary_key:true});
insert into dbbuilder.entities (id, name, column_id, column) values (8EBD06CE-FE15-4D1F-AC36-0E58A1A0A1AE, 'books', 4880C220-E623-486F-BCA7-4E979A5523ED , {name: 'title', type:'nvarchar2(32)', is_null: false, primary_key:false});
insert into dbbuilder.entities (id, name, column_id, column) values (8EBD06CE-FE15-4D1F-AC36-0E58A1A0A1AE, 'books', 27E93BB3-7E80-4728-90D7-F6F2733AD3B8 , {name: 'email', type:'nvarchar2(50)', is_null: true,  primary_key:false});
insert into dbbuilder.entities (id, name, column_id, column) values (BC4885AF-B47A-4C0B-8D06-EC37F759F3FD, 'authors' , 86A3F24B-5003-474E-A743-230467CADC06 , {name: 'id', type: 'uuid', is_null: false, primary_key: true});
insert into dbbuilder.entities (id, name, column_id, column) values (BC4885AF-B47A-4C0B-8D06-EC37F759F3FD, 'authors' , 2964CFDF-569F-496F-8EB8-7666CD658149 , {name: 'firstname', type: 'nvarchar2(50)', is_null: true,  primary_key:false});
insert into dbbuilder.entities (id, name, column_id, column) values (BC4885AF-B47A-4C0B-8D06-EC37F759F3FD, 'authors' , 5FECA1EB-09C3-47A0-920E-07182604F168 , {name: 'lastname',  type: 'nvarchar2(50)', is_null: false, primary_key:false});
insert into dbbuilder.entities (id, name, column_id, column) values (5420D537-AC6C-4298-B69B-3E7B42B0D7C4, 'bookAuthor', 181278EE-04BE-45BB-B6F7-6755A6D259B1 , {name: 'bookId',   type: 'uuid', is_null: false, primary_key: true});
insert into dbbuilder.entities (id, name, column_id, column) values (5420D537-AC6C-4298-B69B-3E7B42B0D7C4, 'bookAuthor', 76F33DA5-0796-4AC5-B8F6-F6654D685D77 , {name: 'authorId',type: 'uuid', is_null: false, primary_key: true});
insert into dbbuilder.entities (id, name, column_id, column) values (3BC764D3-33F9-4588-AC10-0001B668B2F1, 'messages', D481E06C-9736-43B0-94E7-91A41379F64A , {name: 'id', 	   type:'uuid', 		 is_null:false,  primary_key:true});
insert into dbbuilder.entities (id, name, column_id, column) values (3BC764D3-33F9-4588-AC10-0001B668B2F1, 'messages', 80CC1591-5381-4378-BF12-FCA68C19B507 , {name: 'text', 	   type:'nvarchar2', is_null:false,  primary_key:false});
insert into dbbuilder.entities (id, name, column_id, column) values (3BC764D3-33F9-4588-AC10-0001B668B2F1, 'messages', 4A4266CF-AA9C-47CD-9282-BDE3CB2E895F, {name: 'sender',   type:'uuid', 		 is_null:false,  primary_key:false});
insert into dbbuilder.entities (id, name, column_id, column) values (3BC764D3-33F9-4588-AC10-0001B668B2F1, 'messages', A2EA5220-E2B4-4CA4-A00E-7D124D971A2C , {name: 'receiver', type:'uuid', 		 is_null:false,  primary_key:false});

select json * from entities;

//3.2 UPDATE DATA
update dbbuilder.users set password = '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92' where username = 'artemkovtun';
update dbbuilder.users set password = '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92' where username = 'supermario';
update dbbuilder.users set password = '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92' where username = 'jamesmartins';
select json * from dbbuilder.users;

update dbbuilder.files set name = 'new_name.xlsx' where id = E001222E-8AD9-49F2-BB1A-C0B6A54A6A77;
update dbbuilder.files set columns['users'] = [
		{name:'firstname', type: 'nvarchar2'},
		{name:'middlename', type: 'nvarchar2'},
		{name:'lastname', type :'timestamp'}
	] where id = 9353E549-21D6-40CC-A61E-CEADA0187C69;
update dbbuilder.files set created_on = toTimestamp(now()) where id = 382EF0BB-22E9-4BF8-836B-2C24D4E2CD1D;
select json * from dbbuilder.files;

update files_by_username set file_name = 'super awesome table.xlsx' where username = 'artemkovtun' and file_id = 9353e549-21d6-40cc-a61e-ceada0187c69;
update files_by_username set file_name = 'nodata.xlsx' where username = 'supermario' and file_id = e001222e-8ad9-49f2-bb1a-c0b6a54a6a77;
update files_by_username set file_name = 'my_customers.xlsx' where username = 'jamesmartins' and file_id = 382ef0bb-22e9-4bf8-836b-2c24d4e2cd1d;

select json * from files_by_username;

update schemas set entities = entities + {{id: 6E587581-F9D1-469A-AEA6-7445052895AC, name:'userGroups' }} where id = 61D59D93-850A-465A-91F0-F3C73B89555C;
update schemas set entities = entities - {{id: 5420D537-AC6C-4298-B69B-3E7B42B0D7C4, name:'bookAuthor' }} where id = D211043E-4C09-4572-BE5F-A2A214B0E942;
update schemas set name = 'superMessenger' where id = D31C14B0-775B-4821-A26C-5D15553156B0;

select json * from schemas;

update schemas_by_username set schema_name = 'superMessenger' where username = 'jamesmartins' and schema_id = D31C14B0-775B-4821-A26C-5D15553156B0;
update schemas_by_username set created_on = toTimestamp(now()) where username = 'artemkovtun' and schema_id = 61D59D93-850A-465A-91F0-F3C73B89555C;
update schemas_by_username set schema_name = 'mylibrary' where username = 'supermario' and schema_id = D31C14B0-775B-4821-A26C-5D15553156B0;

select json * from schemas_by_username;

update entities set name = 'usersinfo' where id = 695A73AE-AC2F-43EF-BED5-924E6E22ED85;
update entities set column = {name: 'lastname',  type: 'nvarchar2(100)', is_null: false, primary_key:false} where id = BC4885AF-B47A-4C0B-8D06-EC37F759F3FD and column_id = 5feca1eb-09c3-47a0-920e-07182604f168;
update entities set column = {name: 'name', type: 'nvarchar2(50)', is_null: false, primary_key: false} where id =79584579-a4e0-4b27-a35b-419307097b98 and column_id = f1ab7475-7ae6-41d3-a6ca-ab1db79572de;

select json * from entities;

//3.3 CUSTOM DEFINED QUERIES
select json file_id, file_name from files_by_username where username = 'artemkovtun';
select json name, columns from files where id = 9353E549-21D6-40CC-A61E-CEADA0187C69;
select json schema_id, schema_name, created_on from schemas_by_username where username = 'artemkovtun';
select json name, created_on, entities from schemas where id = 61D59D93-850A-465A-91F0-F3C73B89555C;


//3.4 DELETE DATA
delete from users where username = 'artemkovtun';
delete from users where username = 'supermario';
delete from users where username = 'jamesmartins';

delete from files where id = E001222E-8AD9-49F2-BB1A-C0B6A54A6A77;
delete from files where id = 9353E549-21D6-40CC-A61E-CEADA0187C69;
delete from files where id = 382EF0BB-22E9-4BF8-836B-2C24D4E2CD1D;

delete from files_by_username where username = 'artemkovtun';
delete from files_by_username where username = 'supermario'; 
delete from files_by_username where username = 'jamesmartins'; 

delete from schemas where id = 61D59D93-850A-465A-91F0-F3C73B89555C; 
delete from schemas where id = D211043E-4C09-4572-BE5F-A2A214B0E942; 
delete from schemas where id = D31C14B0-775B-4821-A26C-5D15553156B0; 

delete from schemas_by_username where username = 'artemkovtun'; 
delete from schemas_by_username where username = 'supermario'; 
delete from schemas_by_username where username = 'jamesmartins'; 

delete from entities where id = 695A73AE-AC2F-43EF-BED5-924E6E22ED85; 
delete from entities where id = 79584579-A4E0-4B27-A35B-419307097B98; 
delete from entities where id = 8EBD06CE-FE15-4D1F-AC36-0E58A1A0A1AE;
delete from entities where id = BC4885AF-B47A-4C0B-8D06-EC37F759F3FD;
delete from entities where id = 5420D537-AC6C-4298-B69B-3E7B42B0D7C4;  
delete from entities where id = 3BC764D3-33F9-4588-AC10-0001B668B2F1;    