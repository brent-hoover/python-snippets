import psycopg2


def main():
    connection = create_connection('pim', 'brent', 'weasel')
    get_user(connection, 'brent@parkme.com')


def create_connection(database_name, user, password):
    conn = psycopg2.connect(database=database_name, user=user, password=password)
    connection = conn.cursor()
    return connection


def get_user(conn, email):
    conn.execute("select username from auth_user where email = %(email)s;", {"email": email})
    for record in conn:
        print(record)

if __name__ == '__main__':
    main()
