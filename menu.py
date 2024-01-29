from modulo_1.modulo1 import Cliente


cliente1 = Cliente("Lucas", "Beccarini", "40492629","Admin","#1",["tecnologia", "celulares"],"lucas@hotmail.com","hugo wast 1370")
cliente2 = Cliente("franco", "Beccarini","34044600","Usuario","#2",["Training","Ropa"], "franco@hotmail.com", "Guardia nacional 126")

cliente1.comprar("Laptop","carrefour")
print(cliente1)
cliente1.login()
cliente2.login()