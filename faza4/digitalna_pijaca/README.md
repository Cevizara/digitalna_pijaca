# instalacija paketa

pip install -r requirements.txt

# popunjavanje baze

python manage.py shell
exec(open("seed.py").read())