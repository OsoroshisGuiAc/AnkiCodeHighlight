'''
This program in thesis is receiving the input text from Q text edit "self.qTextEdit" and being processed by the method self.mainQTextEditLogic
 what this program do is the following:
    Receive the code and store the data into the PROGRAM PASTE.
        if the data is equal to another data in the computer memory the program should not storage the code in the computer memory.
        if the quantity of data in the computer memory is greater than 10 the program will erase the most old data.
    The program exit the data storage in the database of the same if a function be called

    Receive the data and storage to a config file that will be read by another program when the same execs
'''

import sqlite3

class DataBaseLogicHistory():
    def resetDatabase(self): #Deletes everything to start again when the program close
        rootMemory = sqlite3.connect("data_base.db")
        cursor = rootMemory.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS code_history(
                        data TEXT
            )
            ''')
        
        cursor.execute("""DROP TABLE code_history""")

        cursor.close()
         
    def insertIntoDatabase(self, dataToProcess):
            
            rootMemory = sqlite3.connect("data_base.db")
            self.cursor = rootMemory.cursor()


            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS code_history(
                        data TEXT
            )
            ''')

            #GAMBIARRA Evita o placement de 2 itens iguais no banco de dados
            #GAMBIARRA está funcionando não do que era para funcionar mas está funcionando.

            self.dataBaseOverWrite = self.cursor.execute ("""SELECT rowid FROM code_history WHERE data = ?""", (dataToProcess,))
            self.dataBaseOverWrite.lastrowid
            
            for i in self.dataBaseOverWrite:
                self.cursor.execute ("""INSERT INTO code_history (?) WHERE = ?""", (dataToProcess , i,))

            #GAMBIARRA
            #GAMBIARRA


            #Create the table (remover os valores ao implementar e trocar o banco de dados para memoria)
            self.cursor.execute(""" INSERT INTO code_history (data) VALUES (?) """, (dataToProcess,))
            rootMemory.commit()

            #Show all values in the table
            recovery = self.cursor.execute("SELECT rowid, * FROM code_history")
            for i in recovery:
                print(i)
                
            #Deletes everything greatter than X
            rowNumber = self.cursor.lastrowid
            x = 9
            if rowNumber > x:
                oldestValueToKeep = rowNumber - 9
                self.cursor.execute("DELETE FROM code_history WHERE rowid <= (?) ", (oldestValueToKeep,))

                rootMemory.commit()
                rootMemory.close()
            else:
                rootMemory.close()
                pass


"""class PullDataBaseItens (DataBaseLogicHistory):
     def pullStuff(self, rowidToPull):
          dataBaseLogicHistory = DataBaseLogicHistory()
          #self.dataBaseOverWrite
          '''
                    Vou ter que utilizar uma variavel atrelado a uma RowId da QComboBox e puxar esse código do banco de dados
                '''
          rootMemory = sqlite3.connect("data_base.db")
          cursor = rootMemory.cursor()
          exitPoint = cursor.execute("SELECT data FROM code_history WHERE rowid = (?)", (rowidToPull,))
          #print (str(exitPoint))
          return (str(exitPoint))"""

class PullDataBaseItens (DataBaseLogicHistory):
     def pullStuff(self, rowidToPull):
          dataBaseLogicHistory = DataBaseLogicHistory()
          #self.dataBaseOverWrite
          '''
                    Vou ter que utilizar uma variavel atrelado a uma RowId da QComboBox e puxar esse código do banco de dados
                '''
          rootMemory = sqlite3.connect("data_base.db")
          cursor = rootMemory.cursor()
          cursor.execute("SELECT data FROM code_history WHERE rowid = (?)", (rowidToPull,))
          exitPoint = cursor.fetchone()
          #print (str(exitPoint))
          return exitPoint[0]
        