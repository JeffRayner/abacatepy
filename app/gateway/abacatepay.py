from os import getenv
import abacatepay

client = abacatepay.AbacatePay(getenv("ABACATEPAY_API_KEY"))
