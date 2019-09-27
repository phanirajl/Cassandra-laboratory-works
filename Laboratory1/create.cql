CREATE KEYSPACE dbbuilder WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 3 };

CREATE TABLE IF NOT EXISTS dbbuilder.users (
	username TEXT,
	password TEXT,
	PRIMARY KEY(username)	
);

CREATE TYPE IF NOT EXISTS dbbuilder.file_column(
	name TEXT,
	type TEXT
);

// 2nd query --> information about file
CREATE TABLE IF NOT EXISTS dbbuilder.files (
	id UUID,
	name TEXT,
	created_on TIMESTAMP,
	columns MAP<TEXT,FROZEN<LIST<file_column>>>,
	PRIMARY KEY(id)
);

// 1st query --> select all files of specific user
CREATE TABLE IF NOT EXISTS dbbuilder.files_by_username (
	username TEXT,
	file_id UUID,
	file_name TEXT,
	PRIMARY KEY((username), file_id)
);

CREATE TYPE IF NOT EXISTS dbbuilder.entity_column(
	name TEXT,
	type TEXT,
	is_null BOOLEAN,
	primary_key BOOLEAN
);

CREATE TYPE IF NOT EXISTS dbbuilder.entity_model (
	id uuid,
	name TEXT
);

// 4th query --> select information about schema
CREATE TABLE IF NOT EXISTS dbbuilder.schemas (
	id UUID,
	name TEXT,
	created_on TIMESTAMP,
	entities_quantity int,
	entities SET<FROZEN<entity_model>>,
	PRIMARY KEY(id)
);

// 3rd query --> select all schemas of specific user
CREATE TABLE IF NOT EXISTS dbbuilder.schemas_by_username (
	username TEXT,
	schema_id UUID,
	schema_name TEXT,
	created_on TIMESTAMP,
	PRIMARY KEY((username), schema_id)
);

// 5th query --> select information about entity
CREATE TABLE IF NOT EXISTS dbbuilder.entities (
	id UUID, 
	name TEXT STATIC,
	column_id UUID,
	column FROZEN<entity_column>,
	PRIMARY KEY (id, column_id) 
);
