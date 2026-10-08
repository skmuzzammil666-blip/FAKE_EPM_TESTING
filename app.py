from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}


@app.get("/Fake_epm_testing")
def get_fake_data():
    return [
        {
            "id":1,
            "name":"John Doe"
        },
        {
            "id":1,
            "name":"John Doe"
        },
                
        {
            "id":1,
             "name":"John Doe"
                        
        }
    ]
