from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# 🔗 Conexión a la base de datos
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Horarios_Marello"
    )

@app.route('/')
def home():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    # 🔍 Obtener columnas de la tabla personas
    cursor.execute("DESCRIBE personas")
    columnas = cursor.fetchall()

    campos_personas = [
        {
            "Field": col["Field"],
            "Type": col["Type"],
            "Null": col["Null"],
            "Key": col["Key"],
            "Default": col["Default"],
            "Extra": col["Extra"]
        } for col in columnas
    ]

    # 📦 Obtener todos los registros de personas
    cursor.execute("SELECT * FROM personas")
    registros = cursor.fetchall()

    # JSON principal
    data = {
        "message": "API - Sistema de Gestión de Horarios Marello",
        "version": "1.0",
        "base_url": "http://localhost:5000",
        "database": {
            "name": "Horarios_Marello",
            "engine": "MySQL",
            "host": "localhost",
            "user": "root",
            "tables": {
                "personas": {
                    "primary_key": "persona_id",
                    "fields": campos_personas,
                    "data": registros
                },
                "usuarios": {"primary_key": "usuario_id"},
                "docentes": {"primary_key": "docente_id"},
                "cursos": {"primary_key": "curso_id"},
                "aulas": {"primary_key": "aula_id"},
                "ciclos": {"primary_key": "ciclo_id"},
                "especialidades": {"primary_key": "especialidad_id"},
                "horarios_base": {"primary_key": "horario_id"},
                "semanas": {"primary_key": "semana_id"},
                "estructura_curricular": {"primary_key": "estructura_id"},
                "asignaciones_semanales": {"primary_key": "asignacion_id"}
            }
        },
        "documentation": "Este JSON muestra la estructura y los datos de la tabla personas de la base de datos Horarios_Marello"
    }

    cursor.close()
    db.close()

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
