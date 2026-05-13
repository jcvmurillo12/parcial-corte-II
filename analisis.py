import pandas as pd

df_red = pd.read_csv('Wine/winequality-red.csv', sep=';')
df_white = pd.read_csv('Wine/winequality-white.csv', sep=';')

df_red['type'] = 'red'
df_white['type'] = 'white'

df = pd.concat([df_red, df_white], ignore_index=True)

print("Shape del DataFrame:")
print(df.shape)
print("\n" + "="*50)
print("\nPrimeros registros (head):")
print(df.head())
print("\n" + "="*50)
print("\nCantidad de registros por tipo:")
print(df['type'].value_counts())

# ===== INSPECCIÓN INICIAL DEL DATAFRAME =====

# Mostrar los tipos de datos de cada columna
print("\n" + "="*50)
print("\nTipos de datos de cada columna:")
print(df.dtypes)

# Mostrar estadísticas descriptivas (media, desviación estándar, min, max, etc.)
print("\n" + "="*50)
print("\nEstadísticas descriptivas:")
print(df.describe())

# Mostrar información general del DataFrame (columnas, tipos, memoria, valores nulos)
print("\n" + "="*50)
print("\nInformación general del DataFrame:")
df.info()

# ===== ANÁLISIS DE VALORES NULOS =====

# Contar valores nulos por columna
print("\n" + "="*50)
print("\nCuenta de valores nulos por columna:")
nulos_por_columna = df.isnull().sum()
print(nulos_por_columna)

# Calcular porcentaje de nulos por columna
print("\n" + "="*50)
print("\nPorcentaje de valores nulos por columna:")
total_filas = len(df)
porcentaje_nulos = (nulos_por_columna / total_filas) * 100
print(porcentaje_nulos)

# Conclusión sobre valores nulos
print("\n" + "="*50)
print("\nCONCLUSIÓN - Manejo de Valores Nulos:")
if nulos_por_columna.sum() == 0:
    print("✓ El Dataset NO contiene valores nulos en ninguna columna.")
    print("✓ DECISIÓN: No se requiere imputación ni eliminación de registros.")
    print("✓ El dataset está completo y listo para análisis exploratorio.")
else:
    print(f"⚠ Se encontraron {nulos_por_columna.sum()} valores nulos en total.")
    columnas_con_nulos = nulos_por_columna[nulos_por_columna > 0]
    print(f"\nColumnas afectadas: {columnas_con_nulos.index.tolist()}")
    print("DECISIÓN: Aplicar estrategia de imputación o eliminación según corresponda.")

# ===== DETECCIÓN Y ELIMINACIÓN DE FILAS DUPLICADAS =====

# Guardar el shape original para comparación
shape_original = df.shape
print("\n" + "="*50)
print("\nShape del DataFrame ANTES de eliminar duplicados:")
print(f"Filas: {shape_original[0]}, Columnas: {shape_original[1]}")

# Contar el número total de filas duplicadas
duplicados_count = df.duplicated().sum()
print(f"\nNúmero de filas duplicadas encontradas: {duplicados_count}")

# Eliminar filas duplicadas y resetear el índice
df = df.drop_duplicates().reset_index(drop=True)

# Mostrar el shape después de eliminar duplicados
shape_final = df.shape
print(f"\nShape del DataFrame DESPUÉS de eliminar duplicados:")
print(f"Filas: {shape_final[0]}, Columnas: {shape_final[1]}")

# Calcular la diferencia
filas_eliminadas = shape_original[0] - shape_final[0]
print(f"\nFilas eliminadas: {filas_eliminadas}")

# Conclusión sobre duplicados
print("\n" + "="*50)
print("\nCONCLUSIÓN - Manejo de Duplicados:")
if duplicados_count == 0:
    print("✓ El Dataset NO contiene filas duplicadas.")
    print("✓ DECISIÓN: No se requiere eliminación de duplicados.")
    print("✓ El dataset mantiene su integridad sin cambios.")
else:
    print(f"⚠ Se encontraron {duplicados_count} filas duplicadas.")
    print(f"✓ DECISIÓN: Se eliminaron {filas_eliminadas} registros duplicados.")
    print(f"✓ El dataset ahora contiene {shape_final[0]} registros válidos y únicos.")
