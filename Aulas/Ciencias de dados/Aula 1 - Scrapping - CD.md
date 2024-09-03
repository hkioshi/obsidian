# Extração de dados
- ## Banco de dados e Mensageria
- ## Documentos
- ## API
- ## Scraping(Raspagem)

# Scrapping
- ## Obtenção de dados de páginas web
- ## O robô scraper navega pelas páginas ou faz uma busca específica
- ## Captura de dados que sao armazenados em uma base
- ## Problemas legais: Pode nao ser permitido a cópia de dados
- ## Velocidade: Scraping da internet é um processo demorado


# Tipos
- ## Baixo nivel
	- Robô de scraping anda por texto apenas
	- Busca por tags HTML
	- Busca links importantes para navegaçao
	- Baixo nivel: envia comandos HTTP e trabalha com HTML. Difícil
	- quando a página tem mais iterações com o usuário
	- Programação mais complexa, mas é veloz
- ## Alto Nivel
	- Robô navega pelas páginas
	- Alto nível: Simula iteração do usuário: Clique, digita, espera, visualiza
	- Buscar por trechos, meta informaçoes e recursos visuais da página
	- Alto nivel: envia comandos HTTP e trabalha com HTML
	- Programação mais intuitiva, porém é mais lento

# Como fazer Scrapper do Python(exemplo)
	class PokemonScrapper(scrapy.Spider):
	  name = 'pokemon_scrapper'
	  domain = "https://pokemondb.net/"
	
	  start_urls = ["https://pokemondb.net/pokedex/all"]
	
	  def parse(self, response):
	    pokemons = response.css('#pokedex > tbody > tr')
	    #for pokemon in pokemons:
	    pokemon = pokemons[0]
	    link = pokemon.css("td.cell-name > a::attr(href)").extract_first()
	    yield response.follow(self.domain + link, self.parse_pokemon)
	
	  def parse_pokemon(self, response):
	    yield {
	      'pokedex_number': response.css('.vitals-table > tbody > tr:nth-child(1) > td > strong::text').get(),
	      'pokemon_name': response.css('#main > h1::text').get(),
	          'next_evolution': response.css('#main > div.infocard-list-evo > div:nth-child(3) > span.infocard-lg-data.text-muted > a::text').get()}