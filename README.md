# farmer-dvc
Use DVC for farmer prediction.

The purpose of this repo is to show how to compare metrics accross different git branches with DVC.

## Data source

Find the data from this source (this source of data is not working anymore): https://ars.els-cdn.com/content/image/1-s2.0-S2352340920303048-mmc1.zip

The data comes from this study : https://www.sciencedirect.com/science/article/pii/S2352340920303048

Based on this video : https://www.youtube.com/watch?v=xPncjKH6SPk

## Setup

1. create a venv :

```sh
# activate the venv
source .venv/bin/activate

# install lib
make install
```

2. Create a folder in your drive and get the folder ID. It should look like `1VaMJ5z7q12ffns-hUcs5bQ0X46T3iWwO`

3. Get data and init dvc tracking

```sh
# ini dvc
make init-dvc

# get data
make get-data

# track data
make track-raw-data

# track-metadata
make track-git-change

# push data
make push-data
```

4. (Optional) if you want to retrieve the data

```sh
git clone https://github.com/ssime-git/farmer-dvc.git
dvc pull data
```

## Apply the preprocessing

```sh
make process-data
```

## Train the model

```sh
make train
```

After the training, you will see 2 files in the report folder.

## Initaite and run the pipeline

```sh
# remove tracking on data folder
dvc remove data.dvc

# init the pipeline : this will create a file dvc.yml
make init-pipeline
```

Then you need to update the pipeline with the `process`and `train`stages, then run the command : `dvc repro` to run the pipeline.

take a snapshot :

````sh
git add .
git commit -m "setting up the dvc pipeline"
git push
```