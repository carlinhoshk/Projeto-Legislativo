import face_recognition
import cv2
import numpy as np

known_face_encodings =[]

def face_encoda(img):
    img = face_recognition.face_encodings(img)
    #print(img)
    return img

#def    
obama_image = face_recognition.load_image_file("carometro_legislatura56/image-279.jpg")

c = known_face_encodings.append(face_encoda(obama_image))
print(known_face_encodings)


#obama_face_encoding = face_recognition.face_encodings(obama_image)[0]



#face_recognition.face_encodings(img)[0]
#print(obama_face_encoding)




"""a=0
known_face_encodings =[]
while a == 10:
    a = a + 1"""


# Create arrays of known face encodings and their names
#known_face_encodings = [
   # kim_kataguiri_face_encoding,
    #abou_anni_encoding
#]












"""known_face_names = [
    "Abílio Santana-PL-BA",
    "Abou Anni-UNIÃO-SP",
    "Acácio Favacho-PROS-AP",
    "Adolfo Viana-PSDB-BA",
    "Adriana Ventura-NOVO-SP",
    "Adriano do Baldy-PP-GO",
    "Aécio Neves-PSDB-MG",
    "Aelton Freitas-PP-MG",
    "Afonso Florence-PT-BA",
    "Afonso Hamm-PP-RS",
    "Afonso Motta-PDT-RS",
    "Aguinaldo Ribeiro-PP-PB",
    "Airton Faleiro-PT-PA",
    "AJ Albuquerque-PP-CE",
    "Alan Rick-UNIÃO-AC",
    "Alceu Moreira-MDB-RS",
    "Alcides Rodrigues-PATRIOTA-GO",
    "Alê Silva-REPUBLICANOS-MG",
    "Alencar Santana-PT-SP",
    "Alessandro Molon-PSB-RJ",
    "Alex Manente-CIDADANIA-SP",
    "Alex Santana-REPUBLICANOS-BA",
    "Alexandre Frota-PSDB-SP",
    "Alexandre Leite-UNIÃO-SP",
    "Alexandre Padilha-PT-SP",
    "Alexis Fonteyne-NOVO-SP",
    "Alice Portugal-PCdoB-BA",
    "Aliel Machado-PV-PR",
    "Aline Gurgel-REPUBLICANOS-AP",
    "Aline Sleutjes-UNIÃO-PR",
    "Altineu Côrtes-PL-RJ",
    "Aluisio Mendes-PSC-MA",
    "Amaro Neto-REPUBLICANOS-ES",
    "André Abdon-PP-AP",
    "André de Paula-PSD-PE",
    "André Ferreira-PSC-PE",
    "André Figueiredo-PDT-CE",
    "André Fufuca-PP-MA",
    "André Janones-AVANTE-MG",
    "Angela Amin-PP-SC",
    "Antonio Brito-PSD-BA",
    "Arlindo Chinaglia-PT-SP",
    "Arnaldo Jardim-CIDADANIA-SP",
    "Aroldo Martins-REPUBLICANOS-PR",
    "Arthur Lira-PP-AL",
    "Arthur Oliveira Maia-UNIÃO-BA",
    "Átila Lins-PSD-AM",
    "Átila Lira-PP-PI",
    "Augusto Coutinho-REPUBLICANOS-PE",
    "Áurea Carolina-PSOL-MG",
    "Aureo Ribeiro-SOLIDARIEDADE-RJ",
    "Bacelar-PV-BA",
    "Baleia Rossi-MDB-SP",
    "Benedita da Silva-PT-RJ",
    "Benes Leocádio-UNIÃO-RN",
    "Beto Faro-PT-PA",
    "Beto Pereira-PSDB-MS",
    "Beto Rosado-PP-RN",
    "Bia Kicis-PL-DF",
    "Bibo Nunes-PL-RS",
    "Bilac Pinto-UNIÃO-MG",
    "Bira do Pindaré-PSB-MA",
    "Bohn Gass-PT-RS",
    "Bosco Costa-PL-SE",
    "Bosco Saraiva-SOLIDARIEDADE-AM",
    "Bozzella-UNIÃO-SP",
    "Bruna Furlan-PSDB-SP",
    "Cacá Leão-PP-BA",
    "Camilo Capiberibe-PSB-AP",
    "Capitão Alberto Neto-PL-AM",
    "Capitão Augusto-PL-SP",
    "Capitão Derrite-PL-SP",
    "Capitão Fábio Abreu-PSD-PI",
    "Carla Dickson-PROS-RN",
    "Carla Zambelli-PL-SP",
    "Carlos Chiodini-MDB-SC",
    "Carlos Gomes-REPUBLICANOS-RS",
    "Carlos Henrique Gaguim-UNIÃO-TO",
    "Carlos Jordy-PL-RJ",
    "Carlos Sampaio-PSDB-SP",
    "Carlos Veras-PT-PE",
    "Carlos Zarattini-PT-SP",
    "Carmen Zanotto-CIDADANIA-SC",
    "Caroline de Toni-PL-SC",
    "Cássio Andrade-PSB-PA",
    "Celina Leão-PP-DF",
    "Célio Moura-PT-TO",
    "Célio Silveira-MDB-GO",
    "Célio Studart-PSD-CE",
    "Celso Maldaner-MDB-SC",
    "Celso Russomanno-REPUBLICANOS-SP",
    "Celso Sabino-UNIÃO-PA",
    "Cezinha de Madureira-PSD-SP",
    "Charles Fernandes-PSD-BA",
    "Charlles Evangelista-PP-MG",
    "Chico D'Angelo-PDT-RJ",
    "Chiquinho Brazão-AVANTE-RJ",
    "Chris Tonietto-PL-RJ",
    "Christiane de Souza Yared-PP-PR",
    "Christino Aureo-PP-RJ",
    "Clarissa Garotinho-UNIÃO-RJ",
    "Claudio Cajado-PP-BA",
    "Cleber Verde-REPUBLICANOS-MA",
    "Coronel Armando-PL-SC",
    "Coronel Chrisóstomo-PL-RO",
    "Coronel Tadeu-PL-SP",
    "Covatti Filho-PP-RS",
    "Cristiano Vale-PP-PA",
    "Da Vitoria-PP-ES",
    "Dagoberto Nogueira-PSDB-MS",
    "Damião Feliciano-PDT-PB",
    "Daniel Almeida-PCdoB-BA",
    "Daniel Coelho-CIDADANIA-PE",
    "Daniel Freitas-PL-SC",
    "Daniel Silveira-PTB-RJ",
    "Daniel Trzeciak-PSDB-RS",
    "Daniela do Waguinho-UNIÃO-RJ",
    "Danilo Cabral-PSB-PE",
    "Danilo Forte-PSDB-CE",
    "Danrlei de Deus Hinterholz-PSD-RS",
    "Darci de Matos-PSD-SC",
    "David Miranda-PDT-RJ",
    "David Soares-UNIÃO-SP",
    "Delegado Antônio Furtado-UNIÃO-RJ",
    "Delegado Éder Mauro-PL-PA",
    "Delegado Marcelo Freitas-UNIÃO-MG",
    "Delegado Pablo-UNIÃO-AM",
    "Delegado Waldir-UNIÃO-GO",
    "Denis Bezerra-PSB-CE",
    "Diego Andrade-PSD-MG",
    "Diego Garcia-REPUBLICANOS-PR",
    "Dimas Fabiano-PP-MG",
    "Domingos Neto-PSD-CE",
    "Domingos Sávio-PL-MG",
    "Dr. Frederico-PATRIOTA-MG",
    "Dr. Jaziel-PL-CE",
    "Dr. Leonardo-REPUBLICANOS-MT",
    "Dr. Luiz Antonio Teixeira Jr.-PP-RJ",
    "Dr. Luiz Ovando-PP-MS",
    "Dr. Zacharias Calil-UNIÃO-GO",
    "Dra. Soraya Manato-PTB-ES",
    "Dra. Vanda Milani-SOLIDARIEDADE-AC",
    "Dulce Miranda-MDB-TO",
    "Edilázio Júnior-PSD-MA",
    "Edio Lopes-PL-RR",
    "Eduardo Barbosa-PSDB-MG",
    "Eduardo Bismarck-PDT-CE",
    "Eduardo Bolsonaro-PL-SP",
    "Eduardo Costa-PSD-PA",
    "Eduardo Cury-PSDB-SP",
    "Eduardo da Fonte-PP-PE",
    "Efraim Filho-UNIÃO-PB",
    "Elcione Barbalho-MDB-PA",
    "Eli Borges-SOLIDARIEDADE-TO",
    "Eli Corrêa Filho-UNIÃO-SP",
    "Elias Vaz-PSB-GO",
    "Elmar Nascimento-UNIÃO-BA",
    "Emanuel Pinheiro Neto-MDB-MT",
    "Emidinho Madeira-PL-MG",
    "Enio Verri-PT-PR",
    "Enrico Misasi-MDB-SP",
    "Erika Kokay-PT-DF",
    "Eros Biondini-PL-MG",
    "Euclydes Pettersen-PSC-MG",
    "Evair Vieira de Melo-PP-ES",
    "Expedito Netto-PSD-RO",
    "Fábio Henrique-UNIÃO-SE",
    "Fábio Mitidieri-PSD-SE",
    "Fábio Ramalho-MDB-MG",
    "Fabio Reis-PSD-SE",
    "Fabio Schiochet-UNIÃO-SC",
    "Fábio Trad-PSD-MS",
    "Fausto Pinato-PP-SP",
    "Felício Laterça-PP-RJ",
    "Felipe Carreras-PSB-PE",
    "Felipe Francischini-UNIÃO-PR",
    "Felipe Rigoni-UNIÃO-ES",
    "Félix Mendonça Júnior-PDT-BA",
    "Fernanda Melchionna-PSOL-RS",
    "Fernando Coelho Filho-UNIÃO-PE",
    "Fernando Monteiro-PP-PE",
    "Fernando Rodolfo-PL-PE",
    "Filipe Barros-PL-PR",
    "Flávia Arruda-PL-DF",
    "Flávia Morais-PDT-GO",
    "Flaviano Melo-MDB-AC",
    "Flávio Nogueira-PT-PI",
    "Francisco Jr.-PSD-GO",
    "Franco Cartafina-PP-MG",
    "Fred Costa-PATRIOTA-MG",
    "Frei Anastacio Ribeiro-PT-PB",
    "Gelson Azevedo-PL-RJ",
    "Genecias Noronha-PL-CE",
    "General Girão-PL-RN",
    "General Peternelli-UNIÃO-SP",
    "Geninho Zuliani-UNIÃO-SP",
    "Geovania de Sá-PSDB-SC",
    "Gervásio Maia-PSB-PB",
    "Giacobo-PL-PR",
    "Gil Cutrim-REPUBLICANOS-MA",
    "Gilberto Abramo-REPUBLICANOS-MG",
    "Gilberto Nascimento-PSC-SP",
    "Gilson Marques-NOVO-SC",
    "Giovani Cherini-PL-RS",
    "Giovani Feltes-MDB-RS",
    "Glauber Braga-PSOL-RJ",
    "Glaustin da Fokus-PSC-GO",
    "Gleisi Hoffmann-PT-PR",
    "Gonzaga Patriota-PSB-PE",
    "Greyce Elias-AVANTE-MG",
    "Guiga Peixoto-UNIÃO-SP",
    "Guilherme Mussi-PP-SP",
    "Gurgel-UNIÃO-RJ",
    "Gustavo Fruet-PDT-PR",
    "Gustinho Ribeiro-REPUBLICANOS-SE",
    "Gutemberg Reis-MDB-RJ",
    "Haroldo Cathedral-PSD-RR",
    "Heitor Freire-UNIÃO-CE",
    "Heitor Schuch-PSB-RS",
    "Helder Salomão-PT-ES",
    "Hélio Costa-PSD-SC",
    "Hélio Leite-UNIÃO-PA",
    "Helio Lopes-PL-RJ",
    "Henrique Fontana-PT-RS",
    "Hercílio Coelho Diniz-MDB-MG",
    "Herculano Passos-REPUBLICANOS-SP",
    "Hermes Parcianello-MDB-PR",
    "Hildo Rocha-MDB-MA",
    "Hiran Gonçalves-PP-RR",
    "Hugo Leal-PSD-RJ",
    "Hugo Motta-REPUBLICANOS-PB",
    "Idilvan Alencar-PDT-CE",
    "Igor Kannário-UNIÃO-BA",
    "Igor Timo-PODE-MG",
    "Isnaldo Bulhões Jr.-MDB-AL",
    "Ivan Valente-PSOL-SP",
    "Jandira Feghali-PCdoB-RJ",
    "Jaqueline Cassol-PP-RO",
    "Jefferson Campos-PL-SP",
    "Jerônimo Goergen-PP-RS",
    "Jéssica Sales-MDB-AC",
    "Jesus Sérgio-PDT-AC",
    "Jhonatan de Jesus-REPUBLICANOS-RR",
    "João Campos-REPUBLICANOS-GO",
    "João Carlos Bacelar-PL-BA",
    "João Daniel-PT-SE",
    "João Maia-PL-RN",
    "João Roma-PL-BA",
    "Joaquim Passarinho-PL-PA",
    "Joenia Wapichana-REDE-RR",
    "Joice Hasselmann-PSDB-SP",
    "Jones Moura-PSD-RJ",
    "Jorge Braz-REPUBLICANOS-RJ",
    "Jorge Solla-PT-BA",
    "Jorielson-PL-AP",
    "José Airton Félix Cirilo-PT-CE",
    "José Guimarães-PT-CE",
    "Jose Mario Schreiner-MDB-GO",
    "José Medeiros-PL-MT",
    "José Nelto-PODE-GO",
    "José Nunes-PSD-BA",
    "José Priante-MDB-PA",
    "José Ricardo-PT-AM",
    "José Rocha-UNIÃO-BA",
    "Joseildo Ramos-PT-BA",
    "Josias Gomes-PT-BA",
    "Josimar Maranhãozinho-PL-MA",
    "Josivaldo JP-PSD-MA",
    "Juarez Costa-MDB-MT",
    "Julian Lemos-UNIÃO-PB",
    "Júlio Cesar-PSD-PI",
    "Julio Cesar Ribeiro-REPUBLICANOS-DF",
    "Júlio Delgado-PV-MG",
    "Juninho do Pneu-UNIÃO-RJ",
    "Junio Amaral-PL-MG",
    "Júnior Ferrari-PSD-PA",
    "Junior Lourenço-PL-MA",
    "Júnior Mano-PL-CE",
    "Juscelino Filho-UNIÃO-MA",
    "Kim Kataguiri-UNIÃO-SP",
    "Laercio Oliveira-PP-SE",
    "Lafayette de Andrada-REPUBLICANOS-MG",
    "Lauriete-PSC-ES",
    "Leandre-PSD-PR",
    "Leda Sadala-AVANTE-AP",
    "Leo de Brito-PT-AC",
    "Léo Moraes-PODE-RO",
    "Léo Motta-REPUBLICANOS-MG",
    "Leonardo Gadelha-PSC-PB",
    "Leonardo Monteiro-PT-MG",
    "Leônidas Cristino-PDT-CE",
    "Leur Lomanto Júnior-UNIÃO-BA",
    "Lídice da Mata-PSB-BA",
    "Lincoln Portela-PL-MG",
    "Liziane Bayer-REPUBLICANOS-RS",
    "Loester Trutis-PL-MS",
    "Lourival Gomes-UNIÃO-RJ",
    "Lucas Gonzalez-NOVO-MG",
    "Lucas Redecker-PSDB-RS",
    "Lucas Vergilio-SOLIDARIEDADE-GO",
    "Luciano Bivar-UNIÃO-PE",
    "Luciano Ducci-PSB-PR",
    "Lucio Mosquini-MDB-RO",
    "Luis Miranda-REPUBLICANOS-DF",
    "Luis Tibé-AVANTE-MG",
    "Luisa Canziani-PSD-PR",
    "Luiz Antônio Corrêa-PP-RJ",
    "Luiz Carlos-PSDB-AP",
    "Luiz Carlos Motta-PL-SP",
    "Luiz Lima-PL-RJ",
    "Luiz Nishimori-PSD-PR",
    "Luiz Philippe de Orleans e Bragança-PL-SP",
    "Luiza Erundina-PSOL-SP",
    "Luizão Goulart-SOLIDARIEDADE-PR",
    "Luizianne Lins-PT-CE",
    "Magda Mofatto-PL-GO",
    "Major Fabiana-PL-RJ",
    "Mara Rocha-MDB-AC",
    "Marcel van Hattem-NOVO-RS",
    "Marcelo Álvaro Antônio-PL-MG",
    "Marcelo Aro-PP-MG",
    "Marcelo Calero-PSD-RJ",
    "Marcelo Freixo-PSB-RJ",
    "Marcelo Moraes-PL-RS",
    "Marcelo Nilo-REPUBLICANOS-BA",
    "Marcelo Ramos-PSD-AM",
    "Marcelo Squassoni-REPUBLICANOS-SP",
    "Marcio Alvino-PL-SP",
    "Márcio Biolchi-MDB-RS",
    "Márcio Jerry-PCdoB-MA",
    "Márcio Labre-PL-RJ",
    "Márcio Marinho-REPUBLICANOS-BA",
    "Marco Bertaiolli-PSD-SP",
    "Marcon-PT-RS",
    "Marcos Aurélio Sampaio-PSD-PI",
    "Marcos Pereira-REPUBLICANOS-SP",
    "Marcos Soares-UNIÃO-RJ",
    "Margarete Coelho-PP-PI",
    "Maria do Rosário-PT-RS",
    "Mariana Carvalho-PSDB-RO",
    "Marília Arraes-PT-PE",
    "Marina Santos-REPUBLICANOS-PI",
    "Mário Heringer-PDT-MG",
    "Mário Negromonte Jr.-PP-BA",
    "Marlon Santos-PL-RS",
    "Marreca Filho-PATRIOTA-MA",
    "Marx Beltrão-PP-AL",
    "Maurício Dziedricki-PODE-RS",
    "Mauro Benevides Filho-PDT-CE",
    "Mauro Lopes-PP-MG",
    "Mauro Nazif-PSB-RO",
    "Merlong Solano-PT-PI",
    "Miguel Lombardi-PL-SP",
    "Milton Coelho-PSB-PE",
    "Milton Vieira-REPUBLICANOS-SP",
    "Misael Varella-PSD-MG",
    "Moses Rodrigues-MDB-CE",
    "Natália Bonavides-PT-RN",
    "Nelho Bezerra-PROS-CE",
    "Nelson Barbudo-PL-MT",
    "Nereu Crispim-PSD-RS",
    "Neri Geller-PP-MT",
    "Neucimar Fraga-PP-ES",
    "Newton Cardoso Jr-MDB-MG",
    "Ney Leprevost-PSD-PR",
    "Nicoletti-UNIÃO-RR",
    "Nilson Pinto-PSDB-PA",
    "Nilto Tatto-PT-SP",
    "Nivaldo Albuquerque-REPUBLICANOS-AL",
    "Norma Ayub-PP-ES",
    "Odair Cunha-PT-MG",
    "Olival Marques-MDB-PA",
    "Onyx Lorenzoni-PL-RS",
    "Orlando Silva-PCdoB-SP",
    "Osires Damaso-PSC-TO",
    "Osmar Serraglio-PP-PR",
    "Osmar Terra-MDB-RS",
    "Ossesio Silva-REPUBLICANOS-PE",
    "Otoni de Paula-MDB-RJ",
    "Ottaci Nascimento-SOLIDARIEDADE-RR",
    "Otto Alencar Filho-PSD-BA",
    "Padre João-PT-MG",
    "Paes Landim-PTB-PI",
    "Pastor Eurico-PL-PE",
    "Pastor Gil-PL-MA",
    "Pastor Sargento Isidório-AVANTE-BA",
    "Patrick Dorneles-PSD-PB",
    "Patrus Ananias-PT-MG",
    "Paula Belmonte-CIDADANIA-DF",
    "Paulão-PT-AL",
    "Paulinho da Força-SOLIDARIEDADE-SP",
    "Paulo Abi-Ackel-PSDB-MG",
    "Paulo Azi-UNIÃO-BA",
    "Paulo Bengtson-PTB-PA",
    "Paulo Eduardo Martins-PL-PR",
    "Paulo Foletto-PSB-ES",
    "Paulo Freire Costa-PL-SP",
    "Paulo Ganime-NOVO-RJ",
    "Paulo Guedes-PT-MG",
    "Paulo Pimenta-PT-RS",
    "Paulo Ramos-PDT-RJ",
    "Paulo Teixeira-PT-SP",
    "Pedro Augusto Bezerra-PDT-CE",
    "Pedro Augusto Palareti-PP-RJ",
    "Pedro Lucas Fernandes-UNIÃO-MA",
    "Pedro Lupion-PP-PR",
    "Pedro Paulo-PSD-RJ",
    "Pedro Uczai-PT-SC",
    "Pedro Vilela-PSDB-AL",
    "Pedro Westphalen-PP-RS",
    "Perpétua Almeida-PCdoB-AC",
    "Pinheirinho-PP-MG",
    "Policial Katia Sastre-PL-SP",
    "Pompeo de Mattos-PDT-RS",
    "Pr. Marco Feliciano-PL-SP",
    "Professor Alcides-PL-GO",
    "Professor Israel Batista-PV-DF",
    "Professor Joziel-UNIÃO-RJ",
    "Professora Dayane Pimentel-UNIÃO-BA",
    "Professora Dorinha Seabra Rezende-UNIÃO-TO",
    "Professora Marcivania-PCdoB-AP",
    "Professora Rosa Neide-PT-MT",
    "Rafael Motta-PSB-RN",
    "Raimundo Costa-PODE-BA",
    "Raul Henry-MDB-PE",
    "Reginaldo Lopes-PT-MG",
    "Rejane Dias-PT-PI",
    "Renata Abreu-PODE-SP",
    "Renildo Calheiros-PCdoB-PE",
    "Ricardo Barros-PP-PR",
    "Ricardo da Karol-PSC-RJ",
    "Ricardo Guidi-PSD-SC",
    "Ricardo Izar-REPUBLICANOS-SP",
    "Ricardo Silva-PSD-SP",
    "Ricardo Teobaldo-PODE-PE",
    "Robério Monteiro-PDT-CE",
    "Roberto Alves-REPUBLICANOS-SP",
    "Roberto de Lucena-REPUBLICANOS-SP",
    "Rodrigo Agostinho-PSB-SP",
    "Rodrigo Coelho-PODE-SC",
    "Rodrigo de Castro-UNIÃO-MG",
    "Rogério Correia-PT-MG",
    "Rogério Peninha Mendonça-MDB-SC",
    "Ronaldo Carletto-PP-BA",
    "Rosana Valle-PL-SP",
    "Rosangela Gomes-REPUBLICANOS-RJ",
    "Rose Modesto-PSDB-MS",
    "Rossoni-PSDB-PR",
    "Rubens Bueno-CIDADANIA-PR",
    "Rubens Otoni-PT-GO",
    "Rubens Pereira Júnior-PT-MA",
    "Rui Falcão-PT-SP",
    "Ruy Carneiro-PSDB-PB",
    "Sâmia Bomfim-PSOL-SP",
    "Samuel Moreira-PSDB-SP",
    "Sanderson-PL-RS",
    "Sandro Alex-PSD-PR",
    "Sargento Fahur-PSD-PR",
    "Sebastião Oliveira-AVANTE-PE",
    "Sérgio Brito-PSD-BA",
    "Sergio Souza-MDB-PR",
    "Sergio Toledo-PL-AL",
    "Severino Pessoa-MDB-AL",
    "Shéridan-PSDB-RR",
    "Sidney Leite-PSD-AM",
    "Silas Câmara-REPUBLICANOS-AM",
    "Silvia Cristina-PL-RO",
    "Silvio Costa Filho-REPUBLICANOS-PE",
    "Soraya Santos-PL-RJ",
    "Sóstenes Cavalcante-PL-RJ",
    "Stefano Aguiar-PSD-MG",
    "Subtenente Gonzaga-PSD-MG",
    "Tabata Amaral-PSB-SP",
    "Tadeu Alencar-PSB-PE",
    "Talíria Petrone-PSOL-RJ",
    "Tereza Cristina-PP-MS",
    "Tereza Nelma-PSD-AL",
    "Tiago Dimas-PODE-TO",
    "Tiago Mitraud-NOVO-MG",
    "Tiririca-PL-SP",
    "Tito-AVANTE-BA",
    "Toninho Wandscheer-PROS-PR",
    "Túlio Gadêlha-REDE-PE",
    "Uldurico Junior-MDB-BA",
    "Vaidon Oliveira-PROS-CE",
    "Valdevan Noventa-PL-SE",
    "Valmir Assunção-PT-BA",
    "Valtenir Pereira-MDB-MT",
    "Vander Loubet-PT-MS",
    "Vanderlei Macris-PSDB-SP",
    "Vavá Martins-REPUBLICANOS-PA",
    "Vermelho-PL-PR",
    "Vicentinho-PT-SP",
    "Vicentinho Júnior-PP-TO",
    "Victor Mendes-MDB-MA",
    "Vilson da Fetaemg-PSB-MG",
    "Vinicius Carvalho-REPUBLICANOS-SP",
    "Vinicius Farah-MDB-RJ",
    "Vinicius Poit-NOVO-SP",
    "Vitor Hugo-PL-GO",
    "Vitor Lippi-PSDB-SP",
    "Vivi Reis-PSOL-PA",
    "Waldenor Pereira-PT-BA",
    "Walter Alves-MDB-RN",
    "Weliton Prado-PROS-MG",
    "Wellington Roberto-PL-PB",
    "Wilson Santiago-REPUBLICANOS-PB",
    "Wolney Queiroz-PDT-PE",
    "Zé Carlos-PT-MA",
    "Zé Neto-PT-BA",
    "Zé Silva-SOLIDARIEDADE-MG",
    "Zé Vitor-PL-MG",
    "Zeca Dirceu-PT-PR"]"""