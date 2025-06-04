import qrcode

# 🔗 Link do QR Code
matricula = "12345"  # ou qualquer matrícula fixa que desejar
url = f"http://127.0.0.1:5000/validar_qrcode/{matricula}"

# 📷 Gerando o QR Code
qr = qrcode.make(url)

# 💾 Salvando a imagem na pasta correta do Flask
qr.save("static/img/qr_lixeira.png")

print("QR Code gerado com sucesso!")
