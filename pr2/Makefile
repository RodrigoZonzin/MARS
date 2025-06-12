push: 
	git add .
	git commit -m "commit em $(shell date +%d-%m-%Y)"
	git push

clean: 
	rm *.png *.gml *.txt
	
run: 
	python3 analiseResults2.py results1.json ufsjbr
	python3 analiseResults2.py resultsPopNews.json popnewsjdr
	python3 analiseResults2.py resultsUaiRango.json uairango