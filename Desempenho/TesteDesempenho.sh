#!/bin/bash
# kernprof -l -v soa.py ls >> ArquivosTxt/arquivo2.txt
# python -m memory_profiler soa.py ls >> ArquivosTxt/arquivo2.txt
  
detectores=("FAST" "HARRIS" "ORB" "SHITOMASI" "STAR" "SURF")
descritores=("brief" "brisk" "freak" "orb" "sift")

for detect in ${detectores[@]};
 do
 		for desc in ${descritores[@]};
 		do
 			nImg=1
 			while [ $nImg -ne 14 ]; do
 				cont=1
	   			while [ $cont -ne 11 ]; do
					algoritmo="$detect"_"$desc"

		   			endTxt="Arquivos_Desempenho/""$detect/"$algoritmo/"img""$nImg/"teste$cont.txt""	
					echo $endTxt			   			
					python -m memory_profiler "$detect/""$algoritmo"".py" "$nImg" ls >> $endTxt
		   			kernprof -l -v "$detect/""$algoritmo"".py" "$nImg" ls >> $endTxt 
		   			cont=$(($cont+1))
	   			done
 				nImg=$(($nImg+1))
	   		done	
   		done
 done



