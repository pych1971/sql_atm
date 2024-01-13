from sql_query import SQL_atm


class ATM():

    def atm_logic(self):
        SQL_atm.create_table()
        # SQL_atm.insert_users((1234, 1111, 10000))
        number_card = input('Введите пожалуйста номер карты: ')

        while True:
            if SQL_atm.input_card(number_card):
                print('1111')
            else:
                break


start = ATM()
start.atm_logic()
