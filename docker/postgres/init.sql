DO $$
BEGIN
    IF NOT EXISTS (SELECT FROM pg_catalog.pg_user WHERE usename = 'shopadmin') THEN
        -- Create user using env vars
        CREATE USER shopadmin WITH ENCRYPTED PASSWORD 'fill13rectfuckyoutoo';
        -- Create database and grants all privileges to user
        CREATE DATABASE shop;
        GRANT ALL PRIVILEGES ON DATABASE shop TO shopadmin;
    END IF;
END$$;
