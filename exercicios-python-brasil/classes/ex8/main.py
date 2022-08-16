from macaco import Macaco

macaco1 = Macaco("Douglas")

macaco1.comer("melancia")
macaco1.verBucho()

macaco1.comer("banana")
macaco1.verBucho()

macaco1.comer("maçã")
macaco1.verBucho()

macaco2 = Macaco("João")

macaco2.comer("melancia")
macaco2.verBucho()

macaco2.comer("banana")
macaco2.verBucho()

macaco2.comer(macaco1)
macaco2.verBucho()

