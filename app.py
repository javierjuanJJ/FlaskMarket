#Checks if the run.py file has executed directly and not imported
from market import app

if __name__ == '__main__':
    app.run(debug=True)
