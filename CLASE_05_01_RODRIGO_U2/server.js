import express from "express";
import mysql from "mysql2";
import cors from "cors";

const app = express();
app.use(express.json());
app.use(cors());
app.use(express.static("public")); // sirve tu carpeta con el HTML

// Configuración de conexión
const conexion = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",   // 🔒 tu contraseña
  database: "sis_notas"
});

// Probar conexión
conexion.connect(err => {
  if (err) {
    console.error("❌ Error al conectar a MySQL:", err);
  } else {
    console.log("✅ Conectado a la base de datos MySQL");
  }
});

// Ruta de login
app.post("/login", (req, res) => {
  const { email, password } = req.body;
  const sql = "SELECT * FROM Docentes WHERE email = ? AND password = ?";

  conexion.query(sql, [email, password], (err, results) => {
    if (err) {
      console.error("Error en la consulta:", err);
      res.status(500).json({ ok: false, mensaje: "Error interno" });
    } else if (results.length > 0) {
      res.json({ ok: true, mensaje: "✅ Acceso concedido", docente: results[0] });
    } else {
      res.json({ ok: false, mensaje: "❌ Credenciales incorrectas" });
    }
  });
});

// Servidor
const PORT = 3000;
app.listen(PORT, () => console.log(`🚀 Servidor corriendo en http://localhost:${PORT}`));
