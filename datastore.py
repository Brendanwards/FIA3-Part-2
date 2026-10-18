import sqlite3
from datetime import datetime

class Datastore:

    def __init__(self, path):
        self.connection = sqlite3.connect(path)
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()



    def get_catalogue(self):
        self.cursor.execute(
            """
            SELECT games.game_id, games.name, categories.name, min_playes, max_players, min_age, hold, loans.loan_date 
            FROM games
            LEFT JOIN games_loaned ON games.game_id = games_loaned.game_id
                                AND games_loaned.return_date IS NULL
            LEFT JOIN loans ON games_loaned.loan_id = loans.loan_id
            LEFT JOIN categories ON games.cat_id = categories.cat_id
            """
        )

        results = self.cursor.fetchall()
        actual_results = []
        for result in results:
            status = f"Loaned on {result[7]}" if result[7] is not None else "Now"
            actual_results.append((*result[:6], status, result[6] is not None))
    

        return actual_results

    def get_game_name(self ,name):
        self.cursor.execute(
            """
            SELECT games.game_id, games.name, categories.name, min_playes, max_players, min_age, hold, loans.loan_date 
            FROM games
            LEFT JOIN games_loaned ON games.game_id = games_loaned.game_id
                                AND games_loaned.return_date IS NULL
            LEFT JOIN loans ON games_loaned.loan_id = loans.loan_id
            LEFT JOIN categories ON games.cat_id = categories.cat_id
            WHERE games.name LIKE :name
            """,
            {
                'name':f"{name}%"
            }
        )

        results = self.cursor.fetchall()
        actual_results = []
        for result in results:
            status = f"Loaned on {result[7]}" if result[7] is not None else "Now"
            actual_results.append((*result[:6], status, result[6] is not None))
        return actual_results
    def get_games_players(self, num_players):
        self.cursor.execute(
            """
            SELECT games.game_id, games.name, categories.name, min_playes, max_players, min_age, hold, loans.loan_date 
            FROM games
            LEFT JOIN games_loaned ON games.game_id = games_loaned.game_id
                                AND games_loaned.return_date IS NULL
            LEFT JOIN loans ON games_loaned.loan_id = loans.loan_id
            LEFT JOIN categories ON games.cat_id = categories.cat_id
            WHERE min_playes <= :num_player
            AND max_players >= :num_player
            """,
            {
                'num_player': num_players
            }
        )

        results = self.cursor.fetchall()
        actual_results = []
        for result in results:
            status = f"Loaned on {result[7]}" if result[7] is not None else "Now"
            actual_results.append((*result[:6], status, result[6] is not None))
        return actual_results




    def get_games_age(self, age):
        self.cursor.execute(
            """
            SELECT games.game_id, games.name, categories.name, min_playes, max_players, min_age, hold, loans.loan_date 
            FROM games
            LEFT JOIN games_loaned ON games.game_id = games_loaned.game_id
                                AND games_loaned.return_date IS NULL
            LEFT JOIN loans ON games_loaned.loan_id = loans.loan_id
            LEFT JOIN categories ON games.cat_id = categories.cat_id
            WHERE min_age <= :age
 
            """,
            {
                'age':age
            }
        )

        results = self.cursor.fetchall()
        actual_results = []
        for result in results:
            status = f"Loaned on {result[7]}" if result[7] is not None else "Now"
            actual_results.append((*result[:6], status, result[6] is not None))
        return actual_results


    def get_games_available(self, ):
        
        self.cursor.execute(
            """
            SELECT games.game_id, games.name, categories.name, min_playes, max_players, min_age, hold, loans.loan_date 
            FROM games
            LEFT JOIN games_loaned ON games.game_id = games_loaned.game_id
                                AND games_loaned.return_date IS NULL
            LEFT JOIN loans ON games_loaned.loan_id = loans.loan_id
            LEFT JOIN categories ON games.cat_id = categories.cat_id
            WHERE loan_date IS null
 
            """
        )
        results = self.cursor.fetchall()
        actual_results = []
        for result in results:
            status = f"Loaned on {result[7]}" if result[7] is not None else "Now"
            actual_results.append((*result[:6], status, result[6] is not None))
        return actual_results

    def get_games_on_hold(self, ):
        self.cursor.execute(
            """
            SELECT games.game_id, games.name, categories.name, min_playes, max_players, min_age, hold, loans.loan_date
            FROM games
            LEFT JOIN games_loaned ON games.game_id = games_loaned.game_id
                                AND games_loaned.return_date IS NULL
            LEFT JOIN loans ON games_loaned.loan_id = loans.loan_id
            LEFT JOIN categories ON games.cat_id = categories.cat_id
            WHERE hold IS NOT NULL
 
            """
        )

        results = self.cursor.fetchall()
        actual_results = []
        for result in results:
            status = f"Loaned on {result[7]}" if result[7] is not None else "Now"
            actual_results.append((*result[:6], status, result[6] is not None))
        return actual_results



    def get_members(self, ): 

        self.cursor.execute(
                """
                SELECT mem_id, first_name, last_name
                FROM members
                WHERE active IS 1
                """
            )
            
        results = self.cursor.fetchall()
        actual_results = []
        for result in results:
            actual_results.append((result[0], result[1] + " " + result[2]))
        return actual_results




    def get_all_members(self, ): 

        self.cursor.execute(
                """
                SELECT mem_id, first_name, last_name, active, admin
                FROM members
                """
            )
            
        results = self.cursor.fetchall()
        actual_results = []
        for result in results:
            actual_results.append((result[0], result[1] + " " + result[2], result[3], result[4]))
        return actual_results







    def get_member_by_email(self,email): 
        #do later

        self.cursor.execute(
                """
                SELECT mem_id, first_name, last_name, email, password, phone, active, admin
                FROM members
                WHERE email LIKE :email 
                """,
                {
                    "email":email
                }
            )
            
        results = self.cursor.fetchone()
        return results




    def get_games(self, ): 

        self.cursor.execute(
                """
                SELECT game_id, name
                FROM games
                """

            
            )
            
        results = self.cursor.fetchall()
        actual_results = []
        for result in results:
            actual_results.append((result[0], result[1]))
        return actual_results


    def get_games_on_loan(self): 

        self.cursor.execute(
                """
                SELECT name, loans.loan_date, members.first_name, members.last_name
                FROM games
                INNER JOIN games_loaned ON games.game_id = games_loaned.game_id
                                AND games_loaned.return_date IS NULL
                INNER JOIN loans ON games_loaned.loan_id = loans.loan_id
                INNER JOIN members ON loans.mem_id = members.mem_id
                WHERE games_loaned.return_date IS NULL
                """

            
            )
            
        results = self.cursor.fetchall()
        actual_results = []
        for result in results:
            actual_results.append((result[0], result[1], result[2] + " " + result[3]))
        return actual_results



    def get_categories(self, ): 

        self.cursor.execute(
                """
                SELECT cat_id, name
                FROM categories
                """
            )
            
        results = self.cursor.fetchall()
        actual_results = []
        for result in results:
            actual_results.append((result[0], result[1]))
        return actual_results



    def get_members_games(self, mem_id): 

        self.cursor.execute(
                """
                SELECT games.game_id, games.name
                FROM games
                JOIN games_loaned ON games.game_id = games_loaned.game_id
                JOIN loans ON games_loaned.loan_id = loans.loan_id
                
                WHERE loans.mem_id = :mem_id AND games_loaned.return_date IS NULL
                """,
                {
                    "mem_id":mem_id
                }
 
            )
            
        results = self.cursor.fetchall()
        return results



    def get_fees(self, mem_id,): 

        self.cursor.execute(
                """
                SELECT amt, paid, year
                FROM fees
                """
 
            )
            
        results = self.cursor.fetchall()
        actual_results = []
        for result in results:
            actual_results.append((result[2], result[1]))
        return actual_results

    

    def get_latest_loan_id(self): 

        self.cursor.execute(
                """
                SELECT MAX(loan_id)
                FROM loans
                """
 
            )
            
        results = self.cursor.fetchone()[0]
        return results


    
    def get_mem_held_games(self): 

        self.cursor.execute(
                """
                SELECT game_id, hold
                FROM games
                WHERE hold IS NOT NULL
                """
 
            )
            
        results = self.cursor.fetchall()
        return results





    def add_annual_fees(self, year, amt): 
        members = self.get_members()
        for member in  members:
            mem_id = member[0]
            self.cursor.execute(
                    """
                    INSERT INTO fees(year, amt, mem_id, paid)
                    VALUES (:year, :amt, :mem_id, 0)
                    """,
                {
                    "year":year, 
                    "amt":amt,
                    "mem_id":mem_id
                }

    
                )
            self.connection.commit()


    def add_loan(self, mem_id): 
            self.cursor.execute(
                    """
                    INSERT INTO loans(mem_id, loan_date)
                    VALUES (:mem_id, :date_today)
                    """,
                {
                    "mem_id":mem_id,
                    "date_today":self.date_today()
                }

    
                )
            self.connection.commit()
            return self.cursor.lastrowid



    def add_game_to_loan(self, loan_id, game_id): 
            self.cursor.execute(
                    """
                    INSERT INTO games_loaned(loan_id, game_id)
                    VALUES (:loan_id, :game_id)
                    """,
                {
                    "loan_id":loan_id,
                    "game_id":game_id
                }
                )
            
            self.connection.commit()
      



    def add_members(self, first_name, last_name, email, password, phone, admin): 
            self.cursor.execute(
                    """
                    INSERT INTO members(first_name, last_name, email, password, phone, active, admin)
                    VALUES (:first_name, :last_name, :email, :password, :phone, :active, :admin)
                    """,
                {
                    "first_name":first_name,
                    "last_name":last_name,
                    "email":email,
                    "password":password,
                    "phone":phone,
                    "active":1,
                    "admin":admin
                    
                    
                }

    
                )
            self.connection.commit()




    def add_game(self, name, cat_id, min_playes, max_players, min_age, owner): 
            self.cursor.execute(
                    """
                    INSERT INTO games(name, cat_id, min_playes, max_players, min_age, owner)
                    VALUES (:name, :cat_id, :min_playes, :max_players, :min_age, :owner)
                    """,
                {
                    "name":name,
                    "cat_id":cat_id,
                    "min_playes":min_playes,
                    "max_players":max_players,
                    "min_age":min_age,
                    "owner":owner
                    
                    
                }

    
                )
            self.connection.commit()




    def update_hold(self ,mem_id, game_id):
        self.cursor.execute(
        
        """
        SELECT hold
        FROM games
        WHERE game_id = :game_id
        """,
        {
            "game_id":game_id
        }
        )
        results = self.cursor.fetchall()
        hold = results[0][0]

        if hold == None:

            self.cursor.execute(
            """
            UPDATE games
            SET hold = :mem_id
            WHERE :game_id
            """,
            {
                "mem_id":mem_id,
                "game_id":game_id
            }
           
            )

        elif hold == mem_id:
            self.cursor.execute(

                """
                UPDATE games
                SET hold = NULL
                WHERE :game_id
                """,
            {
                "mem_id":mem_id,
                "game_id":game_id
            }

            )
            self.connection.commit()


    def update_loan(self, game_id):
        self.cursor.execute(

            """
            UPDATE games_loaned
            SET return_date = :date
            WHERE return_date IS NULL 
            AND game_id = :game_id

            """,
        {
            "game_id":game_id,
            "date":self.date_today()
        }
        )
        self.connection.commit()


    def date_today(self):
        return datetime.now().strftime("%Y-%m-%d")



    def update_member_status(self, mem_id):
        self.cursor.execute(
        
        """
        SELECT active
        FROM members
        WHERE mem_id = :mem_id
        """,
        {
            "mem_id":mem_id
        }
        )
        results = self.cursor.fetchall()
        hold = results[0][0]

        if hold == 0:

            self.cursor.execute(
            """
            UPDATE members
            SET active = 1
            WHERE mem_id = :mem_id
            """,
            {
                "mem_id":mem_id
             
            }
           
            )

        elif hold == 1:
            self.cursor.execute(

                """
            UPDATE members
            SET active = 0
            WHERE mem_id = :mem_id
                """,
            {
                "mem_id":mem_id,
                
            }

            )
            self.connection.commit()




    def update_fees(self, year, mem_id):
        self.cursor.execute(

            """
            UPDATE fees
            SET paid = 1
            WHERE mem_id = :mem_id
            AND year = :year

            """,
        {
            "year":year,
            "mem_id":mem_id
        }
        )
        self.connection.commit()




    def update_password(self, mem_id, password):
        self.cursor.execute(

            """
            UPDATE members
            SET password = :password
            WHERE mem_id = :mem_id
    

            """,
        {
            "password":password,
            "mem_id":mem_id
        }
        )
        self.connection.commit()



    def delete_game(self, game_id):
        self.cursor.execute(
        """
        DELETE FROM games
        WHERE game_id = :game_id

        """,

        {
            "game_id":game_id
        }

        )
        self.connection.commit()