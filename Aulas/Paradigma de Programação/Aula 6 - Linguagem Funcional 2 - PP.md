- Funções de alta ordem aceitam outras funções como argumentos ou retornam funções.
	- `map`: aplica uma função a cada elemento de uma lista e retorna uma nova lista com os resultados.
	- `filter`: retorna uma lista contendo apenas os elementos que satisfazem uma condição.
	- `reduce`: combina os elementos de uma lista usando uma função binária, acumulando os valores em um único resultado.

			Exemplo de map
			(def numeros [1 2 3 4 5])
			(defn quadrado [x] (* x x))
			(map quadrado numeros) ;; Resultado: (1 4 9 16 25)
			
			;; Exemplo de filter
			(defn par? [x] (zero? (mod x 2)))
			(filter par? numeros) ;; Resultado: (2 4)
			
			;; Exemplo de reduce
			(defn soma [a b] (+ a b))
			(reduce soma numeros) ;; Resultado: 15`

5! = 5 x 4 x 3 x 2 x 1 = 120 
5 x 4 x 3

pares -> fat -> mut