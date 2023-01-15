import psycopg2
import requests
from config_func import get_config

# tuple[str, list[tuple]]
def is_in_top_250(movie_name: list) -> list:
    params = get_config()
    movies_re = []

    conn: psycopg2._psycopg.connection = None
    try:
        for movie in movie_name:
            with psycopg2.connect(**params) as conn:

                    with conn.cursor() as cur:
                        query = f"""
                        select release_date, rating
                        from imdb_top
                        where movie_name ilike '{movie}'
                        """
                        cur.execute(query)
                        result = cur.fetchall()
                        # print(result)
                        movies_re.append((movie, result))
        return movies_re
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def rating_more_then(num: int) -> list[tuple]:
    params = get_config()

    conn: psycopg2._psycopg.connection = None
    try:
        with psycopg2.connect(**params) as conn:

            with conn.cursor() as cur:
                query = f"""
                    select * 
                    from imdb_top it 
                    where it.rating > {num}
                    """
                cur.execute(query)
                result = cur.fetchall()
                # print(result)
                return result
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def func(movie_name: int) -> list[tuple]:
    params = get_config()

    conn: psycopg2._psycopg.connection = None
    try:
        with psycopg2.connect(**params) as conn:

            with conn.cursor() as cur:
                query = f"""
                        select *
                        from imdb
                        where movie_name ilike %s;
                        """
                print(query)
                cur.execute(query, (movie_name,))
                result = cur.fetchall()
                return result

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.commit()
            conn.close()

    # conn.close()



# connection string
# conn = psycopg2.connect("dbname=bank_db user=postgres password=postgres")
# print(conn)
# conn.close()
# print(conn)

# as params
# conn = psycopg2.connect(
#     host="localhost",
#     port=5432,
#     database="bank_db",
#     user="postgres",
#     password="Avia@1601")
# print(conn)
# conn.close()
# print(conn)








