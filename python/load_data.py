import duckdb

path_db = r"D:\Microsoft\DuckDB\notebook\ma_librairie.db"
con = duckdb.connect(path_db, read_only=True)

df_livres = con.execute("SELECT * FROM livres;").fetchdf()

df_auteurs = con.execute("SELECT * FROM auteurs;").fetchdf()