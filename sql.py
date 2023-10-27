import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    port='3308',
    user='root',
    password='1234',
    database='G2S',
)
cursor = conexao.cursor()

dicio = [
    {
        "car": "mercedes",
        "wheel": 18
    },
    {
        "car" : "audi"
    }
]

# for i in range(0, len(dicio[0])):
#     print(dicio[0].get(f'{i}'))
#     comando = f'INSERT INTO veiculos(car,wheel) VALUES ("{dicio[i].car}", "{dicio[i].wheel}")'
#     cursor.execute(comando);

comandoSelect = f'SELECT * FROM veiculos'
cursor.execute(comandoSelect)
resultado = cursor.fetchall() # ler o banco de dados

print(resultado)

comandoDelete = f'DELETE FROM veiculos'
# cursor.execute(comandoDelete)

# conexao.commit()# edita o banco de dados

cursor.close()
conexao.close()
