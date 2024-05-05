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
	dvc add data/data_raw.csv

track-git-change:
	git add .
	git commit -m "track data metadata"
	git push

push-data:
	dvc push

process-data:
	python3 src/process_data_v2.py

track-processed-data:
	dvc add data/data_processed.csv

train:
	python3 src/train_v2.py

track-data-change: track-raw-data track-git-change push-data

init-pipeline:
	dvc stage add -n get_data -d src/get_data_v2.py -o data/data_raw.csv python3 src/get_data_v2.py