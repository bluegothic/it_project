# it_project team kkpp

<https://github.com/bluegothic/it_project>

## Deployment sets

### look requirements.txt (need go in the dir)

 `cat requirements.txt`

### set envronment

```sh
conda create -n rango python=3.7.5
conda activate rango
conda install django==2.1.5
conda install pillow
```

### set db

run script below to fresh or new db, and set superuser username and password.

 `./freshDb.sh`

may need change mod frist

 `chmod a+x xxx.sh`

run contain data script

 `python polls_dbitems.py`

### Can run it
