push: 
	git add .
	git commit -m "commit em $(shell date +%d-%m-%Y)"
	git push
