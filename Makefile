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

track-raw-data:
	dvc add data

track-metadata:
	git add .
	git commit -m "track data metadata"
	git push

push-data:
	dvc push

