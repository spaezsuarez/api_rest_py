from app import init_app

app = init_app()

@app.route('/')
def main():
    return 'Hola mundo'

if __name__ == '__main__':
    app.run(port = 4000, debug = True)