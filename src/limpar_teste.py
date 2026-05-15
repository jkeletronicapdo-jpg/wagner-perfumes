import sqlite3
DB = r'C:\Dev\_SISTEMAS\WagnerPerfumes\src\database.sqlite'
conn = sqlite3.connect(DB)
conn.execute("DELETE FROM categorias WHERE id IN ('kids', 'teste')")
conn.execute("DELETE FROM marcas WHERE id IN ('testmarca', 'teste')")
conn.commit()
conn.close()

# Verificar
conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cats = conn.execute("SELECT id, nome FROM categorias ORDER BY nome").fetchall()
marcs = conn.execute("SELECT id, nome FROM marcas ORDER BY nome").fetchall()
conn.close()
print("Categorias:")
for c in cats: print(f"  - {c['id']}: {c['nome']}")
print(f"\nMarcas:")
for m in marcs: print(f"  - {m['id']}: {m['nome']}")
print("\nLimpeza OK")
