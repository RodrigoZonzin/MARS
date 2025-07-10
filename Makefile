push: 
	git add .
	git commit -m 'upload feito por $(USER) em $(shell date %d-%m-%Y)'
	git push
