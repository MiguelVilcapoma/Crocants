from flask import Flask, render_template, redirect, url_for
 
# Crocants Pollería — Sistema de gestión interno
app = Flask(__name__)
 
# ── Página principal ──────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html")
 
 
# ── Atención al Cliente ───────────────────────────────────────
@app.route("/atencion")
def atencion():
    """Módulo de atención al cliente: consultas, reclamos y soporte."""
    return render_template("atencion.html")
 
 
# ── Pedidos ───────────────────────────────────────────────────
@app.route("/pedidos")
def pedidos():
    """Módulo de pedidos: registro y seguimiento."""
    return render_template("pedidos.html")
 
 
# ── Pagos ─────────────────────────────────────────────────────
@app.route("/pagos")
def pagos():
    """Módulo de pagos: cobros, historial y reembolsos."""
    return render_template("pagos.html")
 
 
# ── Verificación de Calidad ───────────────────────────────────
@app.route("/calidad")
def calidad():
    """Módulo de verificación de calidad: inspecciones y reportes."""
    return render_template("calidad.html")
 
 
# ── Redirección a WhatsApp ────────────────────────────────────
@app.route("/whatsapp")
def whatsapp():
    """Redirige al número de WhatsApp configurado."""
    numero = "51924535494"          
    mensaje = "Hola, quiero hacer un pedido en Crocants"
    return redirect(
        f"https://wa.me/{numero}?text={mensaje.replace(' ', '%20')}"
    )
 
 
# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True)