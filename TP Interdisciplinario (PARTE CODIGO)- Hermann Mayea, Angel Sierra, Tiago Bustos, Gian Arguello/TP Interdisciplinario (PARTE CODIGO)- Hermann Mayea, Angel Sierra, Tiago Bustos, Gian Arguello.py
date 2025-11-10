import pandas as pd
import matplotlib.pyplot as plt
import os 
import numpy as np

import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt

def cargar_datos(archivo):
    """Carga los datos desde un archivo CSV y realiza limpieza básica."""
    print(f"Cargando datos desde: {archivo}")
    try:
        
        df = pd.read_csv(archivo)

        
        columnas_numericas = ['Jugadores Actuales', 'Jugadores Pico', 'Horas Jugadas']

        for col in columnas_numericas:
    
            df[col] = pd.to_numeric(df[col].astype(str).str.replace(r'[.,]', '', regex=True), errors='coerce')

        
        df['Media Horas por Jugador'] = df.apply(
            lambda row: (row['Horas Jugadas'] / row['Jugadores Pico']) if row['Jugadores Pico'] > 0 else 0,
            axis=1
        )
        
        
        df.dropna(subset=columnas_numericas, inplace=True)
 
        for col in columnas_numericas:
             df[col] = df[col].astype(int)

        return df

    except FileNotFoundError:
        print(f" Error: El archivo '{archivo}' no se encontró. Asegúrate de que esté en la misma carpeta.")
        return None
    except pd.errors.EmptyDataError:
        print(f" Error: El archivo '{archivo}' está vacío.")
        return None
    except Exception as e:
        print(f" Ocurrió un error al cargar o procesar los datos: {e}")
        return None

def mostrar_top_10(df):
    """Muestra la tabla del Top 10."""
    print("\n" + "="*50)
    print(" TOP 10 JUEGOS POR JUGADORES ACTUALES")
    print("="*50)
 
    columnas_top = ['Nombre', 'Jugadores Actuales', 'Jugadores Pico', 'Horas Jugadas', 'Media Horas por Jugador']
    print(df[columnas_top].to_string(index=False, float_format="{:.2f}".format))
    
def graficar_datos(df):
    """Genera y muestra gráficos según la opción elegida por el usuario."""
    print("\n" + "!"*50)
    print(" MENÚ DE GENERACIÓN DE GRÁFICOS")
    print("!"*50)
    print("1. **Gráfico de Barras** (Comparación de Jugadores Actuales en el Top 10)")
    print("2. **Gráfico de Tarta** (Distribución de Horas Jugadas para un Juego Específico)")
    print("3. Volver al Menú Principal")
    print("-" * 50)
    
    opcion_grafico = input("Elige una opción de gráfico (1, 2, o 3): ")
    
    if opcion_grafico == '1':
       
        df_top = df.sort_values(by='Jugadores Actuales', ascending=False).head(10)
        
        nombres = df_top['Nombre']
        actuales = df_top['Jugadores Actuales']
        pico = df_top['Jugadores Pico']
        
        x = np.arange(len(nombres)) 
        width = 0.35 

        fig, ax = plt.subplots(figsize=(14, 8))
        rects1 = ax.bar(x - width/2, actuales, width, label='Jugadores Actuales', color='skyblue')
        rects2 = ax.bar(x + width/2, pico, width, label='Jugadores Pico', color='salmon')

    
        ax.set_xlabel('Juego', fontsize=12)
        ax.set_ylabel('Cantidad de Jugadores (Millones)', fontsize=12)
        ax.set_title('Comparación de Jugadores Actuales vs. Pico (Top 10)', fontsize=16)
        ax.set_xticks(x)
        ax.set_xticklabels(nombres, rotation=45, ha="right", fontsize=10)
        ax.legend()
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()
        
    elif opcion_grafico == '2':
        
        print("\n" + "-"*50)
        nombre_juego = input(" Ingresa el **nombre completo** del juego para el Gráfico de Tarta: ").strip()

        juego_encontrado = df[df['Nombre'].str.lower() == nombre_juego.lower()]
        
        if not juego_encontrado.empty:
            datos = juego_encontrado.iloc[0]
            horas_jugadas = datos['Horas Jugadas']
            
            
            total_horas = df['Horas Jugadas'].sum()
            horas_restantes = total_horas - horas_jugadas
            
            if total_horas > 0:
                labels = [datos['Nombre'] + ' (Horas)', 'Resto del Top 10 (Horas)']
                sizes = [horas_jugadas, horas_restantes]
                colors = ['gold', 'lightcoral']
                explode = (0.1, 0)  
                
                plt.figure(figsize=(9, 9))
                plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                        autopct='%1.1f%%', shadow=True, startangle=140)
                plt.title(f'Distribución de Horas Jugadas: {datos["Nombre"]} vs. el Resto del Top 10', fontsize=14)
                plt.axis('equal')  
                plt.show()
            else:
                print(" No hay datos de 'Horas Jugadas' disponibles para graficar.")
        else:
            print(f" El juego '{nombre_juego}' no se encontró.")

    elif opcion_grafico == '3':
        return
    else:
        print(" Opción no válida. Por favor, intenta de nuevo.")
        
    

def consultar_juego(df):
    """Permite al usuario consultar los datos detallados de un juego específico."""
    print("\n" + "-"*50)
    nombre_juego = input(" Ingresa el **nombre completo** del juego a consultar (o 'salir' para volver): ").strip()

    if nombre_juego.lower() == 'salir':
        return

    
    juego_encontrado = df[df['Nombre'].str.lower() == nombre_juego.lower()]

    if not juego_encontrado.empty:
        datos = juego_encontrado.iloc[0] 
        print("\n" + "*"*50)
        print(f" DATOS DETALLADOS: {datos['Nombre']}")
        print("*"*50)
    
        print(f"  - Jugadores Actuales: {datos['Jugadores Actuales']:,}")
        print(f"  - Jugadores Pico:    {datos['Jugadores Pico']:,}")
        print(f"  - Horas Jugadas Totales: {datos['Horas Jugadas']:,}")
        print("-" * 25)
        
        print(f"  - **Media de Horas por Jugador (Pico):** **{datos['Media Horas por Jugador']:.2f} horas**")
        print("*"*50)
    else:
        print(f" El juego '{nombre_juego}' no se encontró en el Top 10.")

def menu_principal(df):
    """Función principal que maneja el menú de interacción con el usuario."""
    while True:
        print("\n" + "#"*50)
        print(" MENÚ DE CONSULTA DE DATOS DE JUEGOS")
        print("#"*50)
        print("1. Ver el **Top 10** (Lista Completa)")
        print("2. **Consultar Datos** de un Juego Específico")
        print("3. **Generar Gráficos** 📊")
        print("4. Salir")
        print("-" * 50)

        opcion = input("Elige una opción (1, 2, 3 o 4): ")

        if opcion == '1':
            mostrar_top_10(df)
        elif opcion == '2':
            consultar_juego(df)
        elif opcion == '3':
            graficar_datos(df)
        elif opcion == '4':
            print(" Gracias por usar el programa. ¡Hasta pronto!")
            break
        else:
            print(" Opción no válida. Por favor, intenta de nuevo.")


if __name__ == "__main__":
 
    ARCHIVO_DATOS = 'archivo_juegos.csv'

    df_juegos = cargar_datos(ARCHIVO_DATOS)

    if df_juegos is not None:
        menu_principal(df_juegos)