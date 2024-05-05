install:
	pip install -r requirements.txt

init-dvc:
	dvc init
	dvc remote add -d myremote gdrive://1VaMJ5z7q12ffns-hUcs5bQ0X46T3iWwO
	git add .
	git commit -m "init repo and dvc"
	git push

get-data:
	python3 src/get_data_v2.py

track-data:
	dvc add src/data
	dvc commit -m "track data"

track-code-and-metadata:
	git add .
	git commit -m "track metadata"
	git push

push-data:
	dvc push

track : init-dvc get-data track-data track-code-and-metadata push-data