[[05.1 - Linguagens Funcionais - Funções Parciais.pdf]]

# Função Parcial 

(defn somar [a b c]
  (+ a b c))

(def somar-parcial (partial somar 1)) ; Preenche o primeiro argumento com 1
(somar-parcial 2 3) ; Retorna 6

# Currying 
(defn somar-curried [a]
  (fn [b]
    (fn [c]
      (+ a b c))))

((somar-curried 1) 2 3) ; Retorna 6

