# Official Depictions

Datenbank der offiziellen Postkarten zugunsten von Rotem Kreuz, Kriegsfürsorgeamt und Kriegshilfsbüro 1914 – 1918 

## docker

### building the image

* `docker build -t depictions:latest .`
* `docker build -t depictions:latest --no-cache .`

### running the image

To run the image you should provide an `.env` file to pass in needed environment variables; see example below:

* `docker run -it -p 8020:8020 --env-file env.secret --name depictions depictions:latest`
