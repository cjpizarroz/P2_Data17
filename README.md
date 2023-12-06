

<h2>PROYECTO INDIVIDUAL Nº2 - Pizarro Carlos Javier</h2>
<h3>Siniestros viales</h3>
<br>
Los siniestros viales, que comprenden desde choques entre vehículos hasta atropellos, representan una preocupación significativa en ciudades como Buenos Aires debido al intenso tráfico y su impacto en la seguridad de los residentes y la infraestructura. Reducir las tasas de mortalidad relacionadas con estos incidentes es clave para mejorar la seguridad vial. Esto implica acciones como educación, cumplimiento de normativas, infraestructura segura y políticas eficaces para proteger vidas y mejorar la circulación en la ciudad.

<h3>Contexto</h3><br>
Los siniestros viales continúan siendo una preocupación en Argentina, con aproximadamente 4.000 muertes anuales, siendo la principal causa de muertes violentas en el país. Entre 2018 y 2022, se registraron 19.630 fallecimientos debido a estos incidentes, con un promedio de 11 muertes diarias. En 2022, se contabilizaron 3.828 muertes, evidenciando una alta probabilidad de fatalidad en accidentes viales en comparación con incidentes de inseguridad delictiva.




![imagen_portada](https://github.com/cjpizarroz/P2_Data17/assets/90941874/0dec32f1-e5dd-417f-99f2-04e371ebc105)


<h3>Rol a desarrollar</h3><br>
El Observatorio de Movilidad y Seguridad Vial (OMSV), dependiente de la Secretaría de Transporte de Buenos Aires, nos ha encargado un proyecto de análisis de datos. El objetivo es proporcionar información clave para que las autoridades locales puedan tomar medidas efectivas y reducir el número de víctimas fatales en siniestros viales. Nos han facilitado un archivo en formato xlsx con datos sobre homicidios en siniestros viales entre 2016 y 2021 en Buenos Aires. El archivo contiene dos hojas con información sobre hechos y víctimas, además de dos hojas adicionales con diccionarios de datos para facilitar su comprensión.

<h3>ETL (Extracción y Transformación de Datos)</h3><br>
Inicialmente, se manejó un archivo anidado "homicidios.xlsx" con múltiples páginas, organizándolas en dataframes separados.
Se normalizaron nombres de columnas.
Se cambiaron algunos tipos de datos
Se eliminaron duplicados e columnas irrelevantes.
Datos Nulos:<br>
Los valores nulos estaban representados como "SD" (Sin Dato). En algunos casos pudo asignarseles un valor y en otros se eliminaron los registros.
Se lleno los datos faltantes en "FECHA_FALLECIMIENTO" con información de "FECHA_SINIESTRO", asumiendo el fallecimiento en el accidente.<br>

Duplicados:<br>
No se encontraron datos duplicados en el análisis de los conjuntos de datos.<br>
Valores Atípicos:<br>
No se detectaron valores atípicos.<br>

<h3>Análisis</h3><br>


![grafico1](https://github.com/cjpizarroz/P2_Data17/assets/90941874/bf7b51cc-5259-49c6-a11f-3f04cec9f6f6)


En este grafico observamos la cantidad de accidentes por cada comuna. No se observa valores atipicos.<br>


![grafico2](https://github.com/cjpizarroz/P2_Data17/assets/90941874/14e953df-d758-471c-97b5-33bb85109b60)


Aqui observamos la cantidad fallecidos por accidente en cada comuna. Es un grafico muy similar al anterior en la distribucion, con algunas pequeñas diferencias en sus valores.<br>


![grafico3](https://github.com/cjpizarroz/P2_Data17/assets/90941874/309c057d-f0bd-4184-91e2-019eab03a22e)


Aqui observamos como se distribuyeron en el tiempo los accidentes, con un marcado descenso en los tiempos de pandemia.<br>


![grafico4](https://github.com/cjpizarroz/P2_Data17/assets/90941874/97af3f5d-05cf-4d8c-9bf0-742a71165927)


Observamos una marcada diferencia entre los fallecimientos de hombres en comparación con las mujeres.<br>


![grafico5](https://github.com/cjpizarroz/P2_Data17/assets/90941874/8bbe63bb-8154-4399-a2ed-6e02b94bc40d)


Vemos es este grafico, como la gran mayoria de los fallecimientos se encuentran englobados en los roles de conductores y peatones.<br>


![grafico6](https://github.com/cjpizarroz/P2_Data17/assets/90941874/72580cb1-478f-417d-8058-92cc8423713b)


Aqui observamos como tanto las motos como los peatones tienen los mayores porcentajes de fallecimientos de personas<br>

Dashboard<br>
Se confecciono Dashboard, con una portada, una introduccion, dos KPI y un tooltip<br>

![portada](https://github.com/cjpizarroz/P2_Data17/assets/90941874/cdbc5785-79bd-4511-b7c9-54b827783226)<br>

![introduccion](https://github.com/cjpizarroz/P2_Data17/assets/90941874/1e0c9edc-6e3e-4a52-b2c5-dc6f732b00df)<br>

![kpi1](https://github.com/cjpizarroz/P2_Data17/assets/90941874/d36db71c-50b9-4eaa-962a-3c7015f6787e)<br>

![kpi2](https://github.com/cjpizarroz/P2_Data17/assets/90941874/7f22b0e6-d44a-460d-851a-10d7e904b6ef)<br>


Fuente de datos
Obligatorio:

Buenos Aires Data : datasets denominado Homicidios

Complementarios:
Buenos Aires Data : dataset de Lesiones
Buenos Aires Data : nombre comunas
Censo 2022
mapas geojson
