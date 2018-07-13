 # -*- coding: utf-8 -*-

import sqlite3

from House import House

def initDB():

    table_housedetail = '''
        CREATE TABLE IF NOT EXISTS house_detail (
            id                   integer PRIMARY KEY AUTOINCREMENT,
            estate_name          varchar(100),
            proportion           double,
            deal_date            date,
            deal_price           integer,
            sell_price           integer,
            unit_price           integer,
            deal_cycle           integer,
            house_direction      varchar(50),
            build_date           varchar(10),
            property_right       varchar(10)
            )
    '''
    conn =  sqlite3.connect('house.db')
    cursor = conn.cursor()
    cursor.execute(table_housedetail)
    cursor.close()
    conn.commit()
    return conn

def insert(house,conn):
    insert_sql = '''
        INSERT INTO house_detail (estate_name,proportion,deal_date,deal_price,sell_price,unit_price,deal_cycle,house_direction,build_date,property_right)
        VALUES (?,?,?,?,?,?,?,?,?,? )
    '''
    cursor = conn.cursor()
    cursor.execute(insert_sql,(house.estate_name,house.proportion,house.deal_date,house.deal_price,house.sell_price,house.unit_price,house.deal_cycle,house.house_direction,house.build_date,house.property_right))
    cursor.close()
    conn.commit()

if __name__ == '__main__':
    conn = initDB()
    house = House(estate_name='dasd')
    insert(house,conn)
    conn.close()
   
