from os import getenv
import abacatepay

client = abacatepay.AbacatePay(getenv("ABACATEPAY_API_KEY"))

def criarPix(amount=100):
    client.pixQrCode.create({
        "amount": amounts
    })