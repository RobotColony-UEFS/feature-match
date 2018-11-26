#!/bin/bash
# kernprof -l -v soa.py ls >> ArquivosTxt/arquivo2.txt
# python -m memory_profiler soa.py ls >> ArquivosTxt/arquivo2.txt

# Teste realizado para apenas uma imagem

detectores=("FAST" "HARRIS" "ORB" "SHITOMASI" "STAR" "SURF")
descritores=("brief" "brisk" "freak" "orb" "sift")

for detect in ${detectores[@]};
 do
 		for desc in ${descritores[@]};
 		do
   			algoritmo="$detect/$detect"_"$desc"
   			# echo "$algoritmo"".py"
   			endTxt="ArquivosTxt/"$algoritmo.txt""
   			# echo $endTxt
   			
   			python -m memory_profiler "$algoritmo"".py" ls >> $endTxt
   			kernprof -l -v "$algoritmo"".py" ls >> $endTxt 
   			
   		done
 done



