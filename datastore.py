import sqlite3

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


    