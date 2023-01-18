import datetime

from config_func import get_config
import psycopg2
from decorators import intvaluecheck


class Bank:

    def __init__(self):
        self.params = get_config()


    def _add_transfer_query(self, id_tup, amunt, cur):
        date_transfer = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query = f"""
                insert into transactions (coustomer_id, ts, amnt, tr_types, sender, receiver)
                values ({id_tup[2]},'{date_transfer}',{amunt},'transfer',{id_tup[0]},{id_tup[1]});
                """
        cur.execute(query)

    def _id_query(self, table, column, num, cur):
        query = f"""
                select id
                from {table}
                where {column} = %s;
                """
        cur.execute(query, (num,))
        result = cur.fetchall()
        return result

    def _balance_check(self, num, amunt, cur):
        """
        The function checks if the sender has enough money to make a transfer
        """
        query = f"""
                select balance, max_limit
                from account
                where id={num};
                """
        cur.execute(query, (num,))
        result = cur.fetchall()
        if amunt > result[0][0] or result[0][0] - amunt < result[0][1]:
            raise Exception()

    def _account_holder_check(self, account1, customer_passport, cur):
        """
        The function checks if the sender and the customer passport are in the same account
        """

        query = f"""
                select c.passport_num, a.account_num
                from account_holders ah 
                join customer c on ah.customer_id = c.id
                join account a on ah.account_id = a.id ;
                """
        cur.execute(query)
        result = cur.fetchall()
        for i in result:
            if customer_passport in i and account1 in i:
                return True
        return False

    def _sender(self, amunt, id_account, cur):
        """
        Updates the account with the amount he transferred
        """
        query = f"""
                update account set balance = balance - {amunt} where id = {id_account};
                """
        cur.execute(query)

    def _receiver(self, amunt, id_account, cur):
        """
        Updates the account with the amount of the transfer
        """
        query = f"""
                update account set balance = balance + {amunt} where id = {id_account};
                """
        cur.execute(query)

    def get_id_from_db(self, count1: int, count2: int, customer_passport: int) -> tuple:
        """
        The function get the sql id for each variable
        :param count1: sender
        :param count2: receiver
        :param customer_passport: of the sender
        :return: tuple -> id sql
        """
        return self._sent_query('account', 'account_num', count1, self._id_query, 'get_id'), \
               self._sent_query('account', 'account_num', count2, self._id_query, 'get_id'), \
               self._sent_query('customer', 'passport_num', customer_passport, self._id_query, 'get_id')

    def _sent_query(self, table: str = None, column: str = None, num: int = None, func: callable = None,
                    from_func: str = None, id_tup: tuple = None, amunt: int = None, num2: int = None):
        """
        Main function of sending sql query
        """
        conn: psycopg2._psycopg.connection = None
        try:
            with psycopg2.connect(**self.params) as conn:
                with conn.cursor() as cur:

                    # Returns the sql id of all values entered by the user
                    if from_func == 'get_id':
                        return func(table, column, num, cur)

                    # Checks if there is enough money to transfer
                    elif from_func == 'balance':
                        func(num, amunt, cur)

                    # Checks that the person who wants to transfer money and the bank account for the transfer are equal
                    elif from_func == 'account_holder':
                        if not func(num, num2, cur):
                            raise Exception()

                    # # Updates the request in the accounts
                    # elif from_func in ('sender', 'receiver'):
                    #     func(amunt, num, cur)
                    #
                    # # add transfer to db
                    # elif from_func == 'add_trans':
                    #     func(id_tup, amunt, cur)

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.commit()
                conn.close()

    def _transfer(self, amunt, sender, func_send, receiver, func_reci, id_tup, func_tran):
        """
        Main transfer sending insert
        """
        conn: psycopg2._psycopg.connection = None
        try:
            with psycopg2.connect(**self.params) as conn:
                with conn.cursor() as cur:

                    # Updates the request in the accounts
                    func_send(amunt, sender, cur)
                    func_reci(amunt, receiver, cur)

                    # add transfer to db
                    func_tran(id_tup, amunt, cur)

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.commit()
                conn.close()

    @intvaluecheck
    def run(self, count1: int, count2: int, customer_passport: int, amunt: int):
        """
        Thr function run transfer action
        """
        # get sql id
        id_tuple = self.get_id_from_db(count1, count2, customer_passport)
        id_list = []
        for inx, i_d in enumerate(id_tuple):
            if len(i_d) == 0:
                raise Exception()
            id_list.append(i_d[0][0])

        self._sent_query(num=id_list[0], amunt=amunt, func=self._balance_check, from_func='balance')
        self._sent_query(num=count1, num2=customer_passport, func=self._account_holder_check, from_func='account_holder')
        self._transfer(amunt=amunt, sender=id_list[0], func_send=self._sender, receiver=id_list[1],
                         func_reci=self._receiver, id_tup=tuple(id_list), func_tran=self._add_transfer_query)
        # self._sent_query(amunt=amunt, num=id_list[1], func=self._receiver, from_func='receiver')
        # self._sent_query(id_tup=tuple(id_list), amunt=amunt, func=self._add_transfer_query, from_func='add_trans')

        print('the transaction completed successfully')



if __name__ == '__main__':
    b = Bank()
    t = b.run(123, 456, 153462, 10000)

    # def _sent_query(customer_passport, account1):
    #     params = get_config()
    #     conn: psycopg2._psycopg.connection = None
    #     try:
    #         with psycopg2.connect(**params) as conn:
    #             with conn.cursor() as cur:
    #                 query = f"""
    #                         select c.passport_num, a.account_num
    #                         from account_holders ah
    #                         join customer c on ah.customer_id = c.id
    #                         join account a on ah.account_id = a.id ;
    #                         """
    #                 cur.execute(query)
    #                 result = cur.fetchall()
    #                 for i in result:
    #                     if customer_passport in i and account1 in i:
    #                         return True
    #                 return False
    #
    #     except (Exception, psycopg2.DatabaseError) as error:
    #         print(error)
    #     finally:
    #         if conn is not None:
    #             conn.commit()
    #             conn.close()
    #
    # print(_sent_query(153462, 123))
    # from_func = 'sender'
    # print(from_func in ('sender', 'receiver'))



    # for i in t:
    #     if len(i) == 0:
    #         print(False)
    #     else:
    #         print(i[0][0])
    #
    # li = [1, 2, 3]
    # print(li)
    # print(tuple(li))


    # def add_transfer(self, id_tup: tuple, amunt: int):
    #     conn: psycopg2._psycopg.connection = None
    #     try:
    #         with psycopg2.connect(**self.params) as conn:
    #             with conn.cursor() as cur:
    #                 query = f"""
    #                         insert into transactions (coustomer_id, ts, amnt, tr_types, sender, receiver)
    #                         values ({id_tup[2]},{datetime.datetime.now()},{amunt},'transfer',{id_tup[0]},{id_tup[1]});
    #                         """
    #                 cur.execute(query)
    #     except (Exception, psycopg2.DatabaseError) as error:
    #         print(error)
    #     finally:
    #         if conn is not None:
    #             conn.commit()
    #             conn.close()



