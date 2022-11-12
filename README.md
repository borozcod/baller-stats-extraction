# baller-stats-extraction
Easiest way to run is with docker

```shell
docker build -t baller-stats-extraction .
docker run -it --rm -e SHEET_ID='YOUR_SHEET' baller-stats-extraction
```