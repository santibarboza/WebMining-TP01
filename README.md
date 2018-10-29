# WebMining-TP01
Practico 01 de Mineria de la Web- Analisis Similitud en Busqueda Tematica

La carpeta contiene 2 ejecutables. El primero llamado './alex.py', que solo realiza el analisis lexico sobre los
tweets almacenados en './tweets.txt', creando las tablas ARFF's necesarias para el practico. El segundo es './mineria.py'
que se encarga de obtener tweets desde la Streaming API de Twitter, añadirlos en el archivo './tweets.txt' y ejecutar el analizador lexico. El tiempo de escucha esta seteado a mano a 45 segundos donde en promedio escucha 120 tweets. Otro dato a tomar en cuenta es que añade tweets, por lo que por cada vez que se ejecute mineria, se puede agrandar la base de tweets.

Temas:
	Futbol
	Macri
	Justicia
Tweets:
	Ver en './tweets.txt'

	Ademas se entrega en la carpeta un modulo llamado './stopws' que almacena los stopwords en una lista denomida stopwords, permitiendo cambiar el archivo y ver como se modifica el comportamiento segun el nivel de stopwords que se tengan. Las elegidas por mi provienen de http://googleseo.marketing/lista-de-stop-words-o-palabras-vacias-en-espanol/ pero se normalizaron y se escribieron sin tildes para reducir los casos de pruebas, ya que lo primero qe se hace con el texto es llevarlo a minuscula y sacarle las tildes.
	Se eliminaron los links, los @usuario, letras entre dos espacios y los simbolos de puntuacion, dejando #hastags y palabras.
