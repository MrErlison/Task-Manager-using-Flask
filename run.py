from todo_project import app

# Adicionar os cabeçalhos de segurança
@app.after_request
def add_security_headers(response):
    response.headers['X-Frame-Options'] = 'DENY'  # Para evitar que a página seja carregada em iframes
    response.headers['Content-Security-Policy'] = (
        "frame-ancestors 'none';"  # Usando CSP para evitar o embutimento
        "default-src 'self'; "  # Permitir recursos apenas do próprio domínio
        "script-src 'self' https://code.jquery.com https://cdn.jsdelivr.net; "  # JavaScript do próprio site e de fontes confiáveis
        "style-src 'self' https://cdn.jsdelivr.net; "  # CSS apenas do próprio domínio e de fontes confiáveis
        "img-src 'self' data:; "  # Permitir imagens do próprio domínio e inline (base64)
        "font-src 'self' https://fonts.googleapis.com https://fonts.gstatic.com; "  # Permitir fontes do Google Fonts
    )
    return response

if __name__ == '__main__':
    app.run(debug=True)
