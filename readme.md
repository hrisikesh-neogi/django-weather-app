## Django Weather App

![image](https://github.com/user-attachments/assets/4f1bc4fb-bf80-4e90-8245-e19e3f23aac5)

## To run

1. Create a conda environment

```bash
conda create -p ./env python=3.10 -y
```

2. Activate the environment and install the requirements.txt

```bash
conda activate ./env 
pip install -r requirements.txt
```

3. Create a `.env` file in root directory and add the following

```bash
GEOCODE_API_KEY=<geocode_api_key>
```

4. Run the following commands to configure django

```bash
python manage.py makemigrations 
python manage.py migrate 
```

5. Run the application

```bash
python manage.py runserver 
```

6. [Hit the url](http://127.0.0.1:8000/) - http://127.0.0.1:8000/


