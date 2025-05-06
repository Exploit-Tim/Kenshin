def get_arg(message):
    """
    Fungsi untuk mengambil argumen dari pesan command.
    Argumen biasanya berupa teks setelah perintah.
    """
    text = message.text or message.caption
    return " ".join(text.split()[1:]) if text else ""

